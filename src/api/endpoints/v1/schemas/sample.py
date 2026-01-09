from pydantic import BaseModel, Field


class SampleQueryRequest(BaseModel):
    query: str = Field(..., description="The query to send to the agent")


class SampleQueryResponse(BaseModel):
    response: str = Field(..., description="The response from the agent")
