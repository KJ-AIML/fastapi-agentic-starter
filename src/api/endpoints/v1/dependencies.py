from fastapi import Depends
from langgraph.prebuilt.chat_agent_executor import AgentExecutor

from src.agents.agent_manager.agent import sample_agent
from src.execution.actions.sample_action import SampleAction
from src.execution.usecases.sample_usecase import SampleUseCase

def get_sample_agent() -> AgentExecutor:
    return sample_agent

def get_sample_action(agent: AgentExecutor = Depends(get_sample_agent)) -> SampleAction:
    return SampleAction(agent=agent)

def get_sample_usecase(action: SampleAction = Depends(get_sample_action)) -> SampleUseCase:
    return SampleUseCase(action=action)
