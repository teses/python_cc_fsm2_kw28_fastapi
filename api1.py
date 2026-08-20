

from fastapi import FastAPI

app = FastAPI(
    title="Meine API",
    description="""# Lange Beschreibung  die Markdown erlaubt
    
- Aufzählung
- Aufzählung
""",
    version="1.0.0"
)


@app.get(
    "/",
    summary="Meine Beschreibung",
    description="Lange Beschreibung",
    response_description="Beispiel JSON"
)
def startseite():
    return {"message": "Hallo FastAPI!"}


@app.get("/hallo")
def hallo():
    data = [1, 2, 3, 4]
    return data

