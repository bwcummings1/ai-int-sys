# knowledge_base/knowledge_graph.py

from neo4j import GraphDatabase

class KnowledgeGraph:
    """
    Implements the Adaptive Knowledge Graph.
    """

    def __init__(self, uri="bolt://localhost:7687", user="neo4j", password="password"):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def add_knowledge(self, entity, category, properties):
        """
        Adds a new knowledge node to the graph.
        """
        with self.driver.session() as session:
            session.write_transaction(self._create_node, entity, category, properties)

    @staticmethod
    def _create_node(tx, entity, category, properties):
        query = (
            f"MERGE (n:{category} {{name: $entity}}) "
            f"SET n += $properties"
        )
        tx.run(query, entity=entity, properties=properties)

    def query_knowledge(self, query):
        """
        Queries the knowledge graph for insights.
        """
        with self.driver.session() as session:
            result = session.read_transaction(self._execute_query, query)
            return result

    @staticmethod
    def _execute_query(tx, query):
        return [record for record in tx.run(query)]
