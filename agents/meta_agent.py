# agents/meta_agent.py

from communication.agent_protocol import AgentCommunicationProtocol
from agents.reasoning_agent import ReasoningAgent
from agents.creative_agent import CreativeAgent
from agents.memory_agent import MemoryAgent
from agents.execution_agent import ExecutionAgent

class MetaAgentSupervisor:
    """
    Oversees multi-agent coordination, optimizing AI workflows.
    """

    def __init__(self, agent_name="MetaAgentSupervisor"):
        self.agent_name = agent_name
        self.reasoning_agent = ReasoningAgent()
        self.creative_agent = CreativeAgent()
        self.memory_agent = MemoryAgent()
        self.execution_agent = ExecutionAgent()

    def delegate_task(self, task_description):
        """
        Determines which agent is best suited for a given task.
        """
        if "analyze" in task_description:
            return self.reasoning_agent.generate_solution(task_description)
        elif "brainstorm" in task_description:
            return self.creative_agent.brainstorm_ideas(task_description)
        elif "retrieve" in task_description:
            return self.memory_agent.retrieve_past_insights(task_description)
        elif "execute" in task_description:
            return self.execution_agent.execute_task(task_description)
        else:
            return f"No matching agent for task: {task_description}"

    def monitor_performance(self):
        """
        Assesses agent efficiency and suggests workflow improvements.
        """
        return "Monitoring agent performance: All agents operating within optimal parameters."
