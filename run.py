# run.py

import uvicorn
import threading
from api.main import app
from orchestrator.task_orchestrator import celery_app
from config.settings import SYSTEM_CONFIG
from agents.meta_agent import MetaAgentSupervisor
from version_control.version_manager import VersionManager

def start_api():
    """
    Starts the FastAPI server.
    """
    uvicorn.run(app, host=SYSTEM_CONFIG["API_HOST"], port=SYSTEM_CONFIG["API_PORT"])

def start_task_queue():
    """
    Starts the Celery task queue.
    """
    worker = celery_app.Worker(queues=["default"])
    worker.start()

def initialize_system():
    """
    Initializes and verifies system components before startup.
    """
    print("🔹 Initializing AI Intelligence System...")

    # Load system configuration
    print(f"🔹 Loading system config: {SYSTEM_CONFIG}")

    # Ensure knowledge base and memory system are initialized
    from knowledge_base.knowledge_graph import KnowledgeGraph
    from knowledge_base.persistent_memory import PersistentMemory

    kg = KnowledgeGraph()
    pm = PersistentMemory()

    print("✅ Knowledge Graph and Persistent Memory initialized.")

    # Load version control
    version_manager = VersionManager()
    print("✅ Version Control System initialized.")

    # Initialize Meta-Agent
    meta_agent = MetaAgentSupervisor()
    print("✅ Meta-Agent Supervisor is online.")

    print("🚀 System is fully initialized. Starting services...")

if __name__ == "__main__":
    initialize_system()

    # Start API and Task Queue in parallel
    api_thread = threading.Thread(target=start_api)
    queue_thread = threading.Thread(target=start_task_queue)

    api_thread.start()
    queue_thread.start()

    api_thread.join()
    queue_thread.join()
