from fastapi import Depends

from src.agents.agent_manager.agent import sample_agent
from src.execution.actions.sample_action import SampleAction
from src.execution.usecases.sample_usecase import SampleUseCase

def get_sample_agent():
    return sample_agent

def get_sample_action(agent = Depends(get_sample_agent)) -> SampleAction:
    return SampleAction(agent=agent)

def get_sample_usecase(action = Depends(get_sample_action)) -> SampleUseCase:
    return SampleUseCase(action=action)
