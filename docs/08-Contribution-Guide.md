# 08 - Contribution Guide

> **Last Updated:** March 20, 2026  
> **Version:** 0.1.0  
> **Status:** ✅ Active

Thank you for your interest in contributing to ALMS! This guide will help you get started.

## Getting Started

### 1. Fork the Repository

```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/alms.git
cd alms
```

### 2. Setup Development Environment

```bash
# Install dependencies
uv sync

# Setup environment
cp .env.example .env
# Edit .env with your settings

# Run tests to verify setup
uv run pytest src/tests
```

### 3. Create a Branch

```bash
# Create feature branch
git checkout -b feature/my-feature

# Or bugfix branch
git checkout -b fix/bug-description
```

## Development Workflow

### 1. Make Changes

- Follow ALMS layer rules (see `docs/02-Design-Patterns.md`)
- Write clean, documented code
- Add type hints to all functions
- Follow existing code style

### 2. Test Your Changes

```bash
# Run tests
uv run pytest src/tests -v

# Run specific test
uv run pytest src/tests/v1/test_agent.py -v

# Check coverage
uv run pytest src/tests --cov=src --cov-report=html
```

### 3. Check Code Quality

```bash
# Check linting
ruff check src/

# Fix auto-fixable issues
ruff check --fix src/

# Format code
ruff format src/

# Type checking (if using mypy)
mypy src/
```

### 4. Update Documentation

- Update relevant docs in `/docs/`
- Update `UPDATE-SUMMARY.md`
- Add changelog entry if needed

### 5. Commit Changes

```bash
# Stage changes
git add .

# Commit with conventional commit message
git commit -m "feat: add user authentication"
```

### 6. Push and Create PR

```bash
# Push to your fork
git push origin feature/my-feature

# Create Pull Request on GitHub
```

## Code Standards

### Python Style

We use **Ruff** for linting and formatting:

```bash
# Check all files
ruff check src/

# Check specific file
ruff check src/api/main.py

# Auto-fix issues
ruff check --fix src/

# Format code
ruff format src/
```

### Type Hints

**Required:** All function signatures must have type hints.

```python
# ✅ CORRECT
def get_user(user_id: int, db: AsyncSession) -> Optional[User]:
    """Get user by ID."""
    pass

# ❌ WRONG
def get_user(user_id, db):
    """Get user by ID."""
    pass
```

### Docstrings

Use Google-style docstrings:

```python
def create_user(email: str, password: str) -> User:
    """Create a new user.
    
    Args:
        email: User's email address.
        password: Plain text password (will be hashed).
    
    Returns:
        Created user object.
    
    Raises:
        ValidationException: If email is invalid.
        DuplicateException: If email already exists.
    """
    pass
```

### Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Variables | `snake_case` | `user_name` |
| Functions | `snake_case` | `get_user_by_id` |
| Classes | `PascalCase` | `UserRepository` |
| Constants | `UPPER_CASE` | `MAX_RETRY_COUNT` |
| Files | `snake_case.py` | `user_repository.py` |
| Directories | `snake_case` | `user_management` |

### ALMS Layer Rules

**Critical:** Follow ALMS architecture rules:

```
✅ CORRECT: Flow through layers
API Endpoint → Usecase → Action → Repository

❌ WRONG: Never skip layers
API Endpoint → Database  (Don't bypass execution layer)
Usecase → Redis         (Use provider abstraction)
```

See `docs/02-Design-Patterns.md` for detailed patterns.

## Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

### Format

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat: add user authentication` |
| `fix` | Bug fix | `fix: resolve login redirect issue` |
| `docs` | Documentation | `docs: update API documentation` |
| `style` | Code style | `style: format with ruff` |
| `refactor` | Refactoring | `refactor: simplify user service` |
| `test` | Adding tests | `test: add auth unit tests` |
| `chore` | Maintenance | `chore: update dependencies` |
| `perf` | Performance | `perf: optimize database queries` |
| `ci` | CI/CD | `ci: add GitHub Actions` |
| `build` | Build system | `build: update dockerfile` |

### Scopes

| Scope | Description |
|-------|-------------|
| `api` | API layer changes |
| `execution` | Execution layer changes |
| `agent` | Agent layer changes |
| `db` | Database changes |
| `config` | Configuration changes |
| `deps` | Dependencies |
| `docs` | Documentation |

### Examples

```bash
# Feature with scope
git commit -m "feat(api): add user registration endpoint"

# Bug fix
git commit -m "fix(db): resolve connection pool exhaustion"

# Breaking change
git commit -m "feat(api)!: change authentication flow

BREAKING CHANGE: JWT tokens now expire after 1 hour"

# With body
git commit -m "feat(agent): add weather tool

- Integrate with OpenWeather API
- Add caching for 5 minutes
- Update agent prompt template"
```

## Pull Request Process

### 1. Before Creating PR

- [ ] All tests pass
- [ ] Code is linted (`ruff check src/`)
- [ ] Code is formatted (`ruff format src/`)
- [ ] Type hints added
- [ ] Documentation updated
- [ ] Commit messages follow convention

### 2. PR Template

```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings

## Related Issues
Fixes #123
```

### 3. Review Process

1. **Automated Checks:**
   - CI must pass (tests, linting)
   - No merge conflicts

2. **Code Review:**
   - At least one maintainer approval
   - Address review comments
   - Request re-review if needed

3. **Merge:**
   - Squash and merge to keep history clean
   - Delete branch after merge

## Testing Guidelines

### Test Structure

```python
# src/tests/v1/test_user.py
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_user(client: AsyncClient):
    """Test user creation."""
    response = await client.post(
        "/api/v1/users",
        json={"email": "test@example.com", "password": "password123"}
    )
    assert response.status_code == 201
    assert response.json()["success"] is True
    assert response.json()["data"]["email"] == "test@example.com"

@pytest.mark.asyncio
async def test_create_user_invalid_email(client: AsyncClient):
    """Test user creation with invalid email."""
    response = await client.post(
        "/api/v1/users",
        json={"email": "invalid", "password": "password123"}
    )
    assert response.status_code == 422
    assert response.json()["success"] is False
```

### Test Categories

1. **Unit Tests:**
   - Test individual functions/classes
   - Mock dependencies
   - Fast execution

2. **Integration Tests:**
   - Test API endpoints
   - Test database interactions
   - Slower but comprehensive

3. **E2E Tests:**
   - Full user workflows
   - Rare, high-level tests

### Running Tests

```bash
# All tests
uv run pytest src/tests

# Specific file
uv run pytest src/tests/v1/test_agent.py

# With coverage
uv run pytest src/tests --cov=src

# Verbose output
uv run pytest src/tests -v

# Failed tests only
uv run pytest src/tests --lf
```

## Documentation Standards

### Code Documentation

- All public functions must have docstrings
- Complex logic needs inline comments
- Update docs when changing behavior

### External Documentation

Update these files when making changes:

| File | Update When |
|------|-------------|
| `README.md` | Major features, setup changes |
| `docs/01-System-Design.md` | Architecture changes |
| `docs/02-Design-Patterns.md` | New patterns |
| `docs/03-Database-Design.md` | Schema changes |
| `docs/04-Tech-Stack.md` | New dependencies |
| `docs/06-API-Documentation.md` | New endpoints |
| `docs/07-Setup-Installation.md` | Setup changes |
| `UPDATE-SUMMARY.md` | Any doc changes |

## Code Review Checklist

### For Authors

- [ ] Code is self-documenting
- [ ] Tests are comprehensive
- [ ] No commented-out code
- [ ] No debug print statements
- [ ] Error handling is appropriate
- [ ] No hardcoded values (use config)
- [ ] Follows ALMS layer rules

### For Reviewers

- [ ] Logic is correct
- [ ] Tests cover edge cases
- [ ] Performance is acceptable
- [ ] Security concerns addressed
- [ ] Follows project conventions
- [ ] Documentation is updated

## Release Process

### Versioning

We follow [Semantic Versioning](https://semver.org/):

- `MAJOR.MINOR.PATCH`
- `MAJOR`: Breaking changes
- `MINOR`: New features (backward compatible)
- `PATCH`: Bug fixes

### Creating a Release

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create git tag: `git tag v0.1.0`
4. Push tag: `git push origin v0.1.0`
5. Create GitHub release

## Getting Help

### Resources

- **Documentation:** `/docs/` directory
- **Issues:** GitHub Issues
- **Discussions:** GitHub Discussions

### Questions?

- Open a Discussion for questions
- Open an Issue for bugs
- Email maintainers: [TBD]

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to ALMS!**

**Updated:** v0.1.0 - Initial contribution guidelines
