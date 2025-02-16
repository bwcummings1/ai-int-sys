# agents/memory_agent.py

from communication.agent_protocol import AgentCommunicationProtocol
from knowledge_base.knowledge_graph import KnowledgeGraph
from knowledge_base.persistent_memory import PersistentMemory

class MemoryAgent:
    """
    Responsible for retrieving, organizing, and refining stored knowledge.
    """

    def __init__(self, agent_name="MemoryAgent"):
        self.agent_name = agent_name
        self.memory = PersistentMemory()
        self.knowledge_graph = KnowledgeGraph()

    def retrieve_past_insights(self, query):
        """
        Retrieves relevant memory insights based on a given query.
        """
        past_memories = self.memory.retrieve_memory(query)
        graph_insights = self.knowledge_graph.query_knowledge(f"MATCH (n) WHERE n.name CONTAINS '{query}' RETURN n")

        return {
            "past_memories": past_memories,
            "graph_insights": graph_insights
        }

    def structure_knowledge(self, raw_data):
        """
        Organizes retrieved data into structured formats for agent consumption.
        """
        structured_data = {
            "summary": f"Structured information extracted from raw data: {raw_data}",
            "key_points": [item for item in raw_data]  # Extracting key elements
        }

        return structured_data
