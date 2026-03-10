from langgraph.graph import StateGraph
from agents.orchestrator import route

class AgentState(dict):
    pass


async def run_agent(prompt):

    state = AgentState()
    state["prompt"] = prompt

    result = await route(prompt)

    return result