# 03 - Database Design

> **Last Updated:** March 20, 2026  
> **Version:** 0.1.0  
> **Status:** ✅ Active

## Database Overview

- **Type:** PostgreSQL
- **ORM:** SQLAlchemy 2.0 (async)
- **Driver:** asyncpg (async PostgreSQL driver)
- **Migration Tool:** Alembic
- **Architecture:** Repository Pattern with async support

## Connection Configuration

Database connection is configured via environment variables in `src/config/settings.py`:

```python
DATABASE_HOST=localhost      # Database host
DATABASE_PORT=5432           # Database port  
DATABASE_NAME=db             # Database name
DATABASE_USER=postgres       # Database user
DATABASE_PASSWORD=postgres   # Database password
```

Or use a single connection string:
```python
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname
```

### Async Engine Setup

```python
# src/database/connection.py
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = f"postgresql+asyncpg://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

engine = create_async_engine(
    DATABASE_URL,
    echo=settings.DEBUG,        # Log SQL queries in debug mode
    future=True,                # Use SQLAlchemy 2.0 style
    pool_pre_ping=True,         # Verify connections before use
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,     # Don't expire objects after commit
    autocommit=False,
    autoflush=False,
)
```

## Schema Design

### Base Model

All database models inherit from the declarative base:

```python
# src/database/connection.py
class Base(DeclarativeBase):
    """Base class for all models"""
    pass
```

### Example Model Structure

```python
# src/models/user.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from src.database.connection import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
```

## Repository Pattern

Database access is abstracted through the Repository pattern:

### Base Repository

```python
# src/database/repositories/base.py
from typing import Any, Generic, List, Optional, Type, TypeVar
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

class BaseRepository(Generic[T]):
    """Base repository for CRUD operations"""
    
    def __init__(self, model: Type[T]):
        self.model = model
    
    async def get(self, id: Any) -> Optional[T]:
        raise NotImplementedError
    
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        raise NotImplementedError
    
    async def create(self, obj_in: T) -> T:
        raise NotImplementedError
    
    async def update(self, id: Any, obj_in: T) -> T:
        raise NotImplementedError
    
    async def delete(self, id: Any) -> bool:
        raise NotImplementedError
```

### Concrete Repository Example

```python
# src/database/repositories/user_repository.py
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.repositories.base import BaseRepository
from src.models.user import User, UserCreate, UserUpdate

class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User)
        self.session = session
    
    async def get(self, id: int) -> Optional[User]:
        result = await self.session.execute(
            select(User).where(User.id == id)
        )
        return result.scalar_one_or_none()
    
    async def get_by_email(self, email: str) -> Optional[User]:
        result = await self.session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()
    
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[User]:
        result = await self.session.execute(
            select(User).offset(skip).limit(limit)
        )
        return result.scalars().all()
    
    async def create(self, obj_in: UserCreate) -> User:
        db_obj = User(**obj_in.dict())
        self.session.add(db_obj)
        await self.session.flush()
        await self.session.refresh(db_obj)
        return db_obj
    
    async def update(self, id: int, obj_in: UserUpdate) -> User:
        db_obj = await self.get(id)
        if db_obj:
            for field, value in obj_in.dict(exclude_unset=True).items():
                setattr(db_obj, field, value)
            await self.session.flush()
            await self.session.refresh(db_obj)
        return db_obj
    
    async def delete(self, id: int) -> bool:
        db_obj = await self.get(id)
        if db_obj:
            await self.session.delete(db_obj)
            return True
        return False
```

## Database Session Management

### FastAPI Dependency Injection

```python
# src/database/connection.py
async def get_db():
    """Dependency for getting async database sessions"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
```

### Usage in Endpoints

```python
# src/api/endpoints/v1/users.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.connection import get_db
from src.database.repositories.user_repository import UserRepository

router = APIRouter()

@router.get("/users/{user_id}")
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    repo = UserRepository(db)
    user = await repo.get(user_id)
    if not user:
        raise NotFoundException("User not found")
    return user
```

## Migrations (Alembic)

Alembic is used for database schema migrations.

### Configuration

Configuration is in `alembic.ini` and `alembic/env.py`.

### Common Commands

```bash
# Create a new migration (auto-generate from models)
alembic revision --autogenerate -m "Add users table"

# Apply all pending migrations
alembic upgrade head

# Rollback one migration
alembic downgrade -1

# Rollback to specific revision
alembic downgrade <revision_id>

# Show current revision
alembic current

# Show migration history
alembic history --verbose

# Create empty migration (for manual SQL)
alembic revision -m "Manual data migration"
```

### Migration File Structure

```python
# alembic/versions/20240320_add_users_table.py
"""Add users table

Revision ID: 1234567890ab
Revises: 
Create Date: 2024-03-20 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1234567890ab'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('username')
    )
    op.create_index('ix_users_id', 'users', ['id'], unique=False)

def downgrade():
    op.drop_index('ix_users_id', table_name='users')
    op.drop_table('users')
```

## Query Patterns

### Basic Queries

```python
# Select all users
result = await session.execute(select(User))
users = result.scalars().all()

# Select with filter
result = await session.execute(
    select(User).where(User.is_active == True)
)
active_users = result.scalars().all()

# Select one by ID
result = await session.execute(
    select(User).where(User.id == user_id)
)
user = result.scalar_one_or_none()

# Select with multiple conditions
result = await session.execute(
    select(User)
    .where(User.is_active == True)
    .where(User.created_at > datetime.utcnow() - timedelta(days=7))
)
recent_active_users = result.scalars().all()
```

### Pagination

```python
# Offset-based pagination
result = await session.execute(
    select(User)
    .offset((page - 1) * page_size)
    .limit(page_size)
)
users = result.scalars().all()

# Get total count
count_result = await session.execute(
    select(func.count()).select_from(User)
)
total = count_result.scalar()
```

### Joins

```python
# Simple join
result = await session.execute(
    select(User, Post)
    .join(Post, User.id == Post.user_id)
    .where(User.id == user_id)
)

# Eager loading (avoid N+1)
from sqlalchemy.orm import selectinload

result = await session.execute(
    select(User)
    .options(selectinload(User.posts))
    .where(User.id == user_id)
)
user_with_posts = result.scalar_one_or_none()
```

### Transactions

```python
# Manual transaction
async with AsyncSessionLocal() as session:
    try:
        # Perform multiple operations
        user = User(email="user@example.com")
        session.add(user)
        
        post = Post(title="Hello", user_id=user.id)
        session.add(post)
        
        await session.commit()
    except Exception:
        await session.rollback()
        raise
```

## Indexes

### Best Practices

1. **Primary Keys:** Automatically indexed
2. **Foreign Keys:** Automatically indexed
3. **Search Fields:** Index fields used in WHERE clauses
4. **Unique Fields:** Use unique constraints for emails, usernames
5. **Composite Indexes:** For multi-column queries

```python
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)  # Unique + indexed
    username = Column(String, unique=True, index=True)
    
    # Composite index for common query patterns
    __table_args__ = (
        Index('ix_user_created_active', 'created_at', 'is_active'),
    )
```

## Performance Considerations

### 1. Connection Pooling

```python
engine = create_async_engine(
    DATABASE_URL,
    pool_size=10,              # Default connections in pool
    max_overflow=20,           # Extra connections when needed
    pool_pre_ping=True,        # Verify connections before use
    pool_recycle=3600,         # Recycle connections after 1 hour
)
```

### 2. Query Optimization

- Use `selectinload()` for relationships to avoid N+1 queries
- Add indexes for frequently queried columns
- Use `defer()` for large columns not always needed
- Implement pagination for large result sets

### 3. Async Patterns

- Always use async/await for database operations
- Don't block the event loop with sync DB calls
- Use `AsyncSession` throughout the application

## Docker Setup

PostgreSQL can be run locally via Docker Compose:

```yaml
# docker-compose.yml
services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: alms_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

**Updated:** v0.1.0 - Initial database design with SQLAlchemy 2.0, asyncpg, and Alembic
