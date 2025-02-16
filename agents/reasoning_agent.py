# agents/reasoning_agent.py

from communication.agent_protocol import AgentCommunicationProtocol
from knowledge_base.knowledge_graph import KnowledgeGraph
from knowledge_base.persistent_memory import PersistentMemory

class ReasoningAgent:
    """
    Handles logical reasoning, structured problem-solving, and inference.
    """

    def __init__(self, agent_name="ReasoningAgent"):
        self.agent_name = agent_name
        self.memory = PersistentMemory()
        self.knowledge_graph = KnowledgeGraph()

    def analyze_problem(self, problem_statement):
        """
        Analyzes a problem and retrieves relevant knowledge.
        """
        # Retrieve past relevant insights
        past_memories = self.memory.retrieve_memory(problem_statement)
        knowledge_insights = self.knowledge_graph.query_knowledge(f"MATCH (n) WHERE n.name CONTAINS '{problem_statement}' RETURN n")

        return {
            "problem": problem_statement,
            "past_memories": past_memories,
            "knowledge_insights": knowledge_insights
        }

    def generate_solution(self, problem_statement):
        """
        Generates a logical solution using retrieved insights.
        """
        insights = self.analyze_problem(problem_statement)
        solution = f"Based on prior knowledge and logical reasoning, a potential solution is: {insights}"

        # Store the generated solution in memory
        self.memory.store_memory(solution, metadata={"source": "ReasoningAgent"})

        return solution
