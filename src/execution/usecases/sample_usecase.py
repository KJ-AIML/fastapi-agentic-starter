from src.config.logs_config import get_logger
from src.execution.actions.sample_action import SampleAction

logger = get_logger(__name__)


class SampleUseCase:
    def __init__(self, action: SampleAction):
        self.action = action

    async def execute(self, query: str) -> str:
        logger.info(f"Executing SampleUseCase with query: {query}")
        return await self.action.execute(query)
