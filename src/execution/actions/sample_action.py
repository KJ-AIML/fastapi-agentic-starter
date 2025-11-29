from src.config.logs_config import get_logger

logger = get_logger(__name__)

class SampleAction:
    def __init__(self, agent):
        self.agent = agent

    async def execute(self, query: str) -> str:
        logger.info(f"Executing SampleAction with query: {query}")
        result = await self.agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": query
                    }
                ]
            }
        )
        # Extract the last message content
        last_message = result["messages"][-1]
        return last_message.content
