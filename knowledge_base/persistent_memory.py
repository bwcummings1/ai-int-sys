# knowledge_base/persistent_memory.py

import weaviate
from weaviate import WeaviateClient
from weaviate.connect import ConnectionParams  # Required for v4
import json

class PersistentMemory:
    """
    Implements a long-term AI memory system using Weaviate v4.0.
    """

    def __init__(self, url="http://localhost:8080"):
        # Fix: Use ConnectionParams.from_url() instead of from_http()
        connection_params = ConnectionParams.from_url(url)
        self.client = WeaviateClient(connection_params)

        # Ensure memory schema exists
        self._initialize_schema()

    def _initialize_schema(self):
        """
        Initializes the memory storage schema in Weaviate.
        """
        schema = {
            "class": "Memory",
            "description": "Long-term AI memory storage",
            "properties": [
                {"name": "content", "dataType": ["text"], "description": "Stored knowledge content"},
                {"name": "metadata", "dataType": ["text"], "description": "Metadata about stored knowledge"},
            ],
        }

        try:
            if "Memory" not in self.client.schema.get()["classes"]:
                self.client.schema.create_class(schema)
        except weaviate.WeaviateBaseError as e:
            print(f"Error initializing schema: {e}")

    def store_memory(self, content, metadata=None):
        """
        Stores long-term AI memory as a vectorized document.
        """
        memory_data = {
            "class": "Memory",
            "properties": {
                "content": content,
                "metadata": json.dumps(metadata) if metadata else "{}",
            },
        }
        try:
            self.client.data.insert(memory_data)
        except weaviate.WeaviateBaseError as e:
            print(f"Error storing memory: {e}")

    def retrieve_memory(self, query):
        """
        Retrieves relevant memory content based on semantic similarity.
        """
        try:
            response = (
                self.client.query
                .get("Memory", ["content", "metadata"])
                .with_near_text({"concepts": [query]})
                .do()
            )
            return response.get("data", {}).get("Get", {}).get("Memory", [])
        except weaviate.WeaviateBaseError as e:
            print(f"Error retrieving memory: {e}")
            return []

    def clear_memory(self):
        """
        Deletes all stored memory.
        """
        try:
            self.client.schema.delete_class("Memory")
        except weaviate.WeaviateBaseError as e:
            print(f"Error clearing memory: {e}")
