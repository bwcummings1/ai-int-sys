# agents/execution_agent.py

from communication.agent_protocol import AgentCommunicationProtocol
from knowledge_base.persistent_memory import PersistentMemory

class ExecutionAgent:
    """
    Converts AI decisions into structured executable actions.
    """

    def __init__(self, agent_name="ExecutionAgent"):
        self.agent_name = agent_name
        self.memory = PersistentMemory()

    def execute_task(self, task_description):
        """
        Simulates the execution of a structured task.
        """
        execution_log = f"Executing task: {task_description}"

        # Store execution log in memory
        self.memory.store_memory(execution_log, metadata={"source": "ExecutionAgent"})

        return execution_log

    def confirm_execution(self, task_description):
        """
        Confirms whether a task was successfully executed.
        """
        return f"Task '{task_description}' has been successfully executed."
