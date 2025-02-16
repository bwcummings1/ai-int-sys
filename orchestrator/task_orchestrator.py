# orchestrator/task_orchestrator.py

from celery import Celery

# Define Celery application
celery_app = Celery(
    "task_orchestrator",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def process_agent_task(task_description):
    """
    Asynchronous task handler for AI agent execution.
    """
    from agents.meta_agent import MetaAgentSupervisor

    meta_agent = MetaAgentSupervisor()
    return meta_agent.delegate_task(task_description)
