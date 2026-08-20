"""

api mit routern
"""

from fastapi import FastAPI

from routers import todo
from routers import task

app = FastAPI(
    title="Todo API",
    description="REST API zur Verwaltung von Todos",
    version="1.0.0"
)

app.include_router(todo.router)
app.include_router(task.router)
