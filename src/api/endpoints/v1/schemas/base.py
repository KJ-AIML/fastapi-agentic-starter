from typing import Any, Generic, Optional, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class ErrorDetail(BaseModel):
    code: str = Field(..., description="Machine-readable error code")
    message: str = Field(..., description="Human-readable error message")
    details: Optional[Any] = Field(None, description="Additional error context")


class AppResponse(BaseModel, Generic[T]):
    success: bool = Field(..., description="Indicates if the request was successful")
    data: Optional[T] = Field(None, description="The response data")
    error: Optional[ErrorDetail] = Field(
        None, description="Error details if success is false"
    )
    request_id: Optional[str] = Field(
        None, description="Unique identifier for the request"
    )
