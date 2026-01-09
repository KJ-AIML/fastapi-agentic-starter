from typing import Any, Generic, List, Optional, Type, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseRepository(Generic[T]):
    """
    Base repository implementation for CRUD operations.
    This can be subclassed for specific database backends (SQLAlchemy, Motor, etc.)
    """

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
