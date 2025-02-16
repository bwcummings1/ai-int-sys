# agents/creative_agent.py

from communication.agent_protocol import AgentCommunicationProtocol
from knowledge_base.persistent_memory import PersistentMemory

class CreativeAgent:
    """
    Generates novel solutions and explores creative problem-solving approaches.
    """

    def __init__(self, agent_name="CreativeAgent"):
        self.agent_name = agent_name
        self.memory = PersistentMemory()

    def brainstorm_ideas(self, problem_statement):
        """
        Generates creative solutions for a given problem.
        """
        creative_solutions = [
            f"Reframing the problem differently: {problem_statement}",
            f"Applying a counter-intuitive approach to {problem_statement}",
            f"Leveraging an unrelated field to solve {problem_statement}"
        ]

        # Store creative solutions in memory
        for solution in creative_solutions:
            self.memory.store_memory(solution, metadata={"source": "CreativeAgent"})

        return creative_solutions
