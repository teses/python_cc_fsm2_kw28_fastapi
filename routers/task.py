"""
Alle Endpunkte der Tasks
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

# /tasks/
@router.get("/")
def get_tasks():
    return {
        "message": "Alle Tasks"
    }

# todos/123
@router.get("/{task_id}")
def get_todo(task_id: int):
    return {
        "task_id": task_id,
        "task_title": "Mein Task"
    }
