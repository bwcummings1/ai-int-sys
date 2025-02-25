# api/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.meta_agent import MetaAgentSupervisor

# Initialize FastAPI app
app = FastAPI(title="AI Intelligence System API")

# Initialize the Meta-Agent Supervisor
meta_agent = MetaAgentSupervisor()

class TaskRequest(BaseModel):
    """
    Defines the structure for incoming task requests.
    """
    task_description: str

@app.get("/")
def home():
    """
    Root endpoint to check if API is running.
    """
    return {"message": "AI Intelligence System is online."}

@app.post("/process-task/")
def process_task(request: TaskRequest):
    """
    Processes user-submitted tasks via the Meta-Agent.
    """
    try:
        response = meta_agent.delegate_task(request.task_description)
        return {"status": "success", "task": request.task_description, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/monitor-agents/")
def monitor_agents():
    """
    Retrieves agent performance monitoring data.
    """
    return {"status": "success", "message": meta_agent.monitor_performance()}
