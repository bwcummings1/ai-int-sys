# knowledge_base/persistent_memory.py

import weaviate
import json
import uuid

class PersistentMemory:
    """
    Implements a long-term AI memory system using Weaviate.
    """

    def __init__(self, url="http://localhost:8080"):
        self.client = weaviate.Client(url)

        # Ensure memory schema exists
        self._initialize_schema()

    def _initialize_schema(self):
        """
        Initializes the memory storage schema in Weaviate.
        """
        schema = {
            "classes": [
                {
                    "class": "Memory",
                    "description": "Long-term AI memory storage",
                    "properties": [
                        {
                            "name": "content",
                            "dataType": ["text"],
                            "description": "Stored knowledge content"
                        },
                        {
                            "name": "metadata",
                            "dataType": ["text"],
                            "description": "Metadata about stored knowledge"
                        }
                    ]
                }
            ]
        }
        try:
            self.client.schema.create(schema)
        except weaviate.exceptions.WeaviateBaseError:
            print("Memory schema already exists.")

    def store_memory(self, content, metadata=None):
        """
        Stores long-term AI memory as a vectorized document.
        """
        memory_data = {
            "content": content,
            "metadata": json.dumps(metadata) if metadata else "{}"
        }
        self.client.data_object.create(memory_data, "Memory")

    def retrieve_memory(self, query):
        """
        Retrieves relevant memory content based on semantic similarity.
        """
        query_result = self.client.query.get("Memory", ["content", "metadata"]).with_near_text({"concepts": [query]}).do()
        
        if query_result and "data" in query_result:
            return query_result["data"]["Get"]["Memory"]
        return []

    def clear_memory(self):
        """
        Deletes all stored memory.
        """
        self.client.schema.delete_all()

