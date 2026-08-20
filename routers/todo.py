"""
Alle Endpunkte der Todos
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

# /todos/
@router.get("/")
def get_todos():
    return {
        "message": "Alle Todos"
    }

# todos/123
@router.get("/{todo_id}")
def get_todo(todo_id: int):
    return {
        "todo_id": todo_id,
        "todo_title": "Mein Todo"
    }
