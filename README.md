# python_cc_fsm2_kw28_fastapi

Repository zum lernen und experemtieren mit der FastAPI Technologie

# Eingesetzte Python Module

- FastApi - Verarbeitet Routing, Requests und Responses
- Pydantic - Validiert und modelliert die Daten
- Uvicorn - Nimmt HTTP-Anfragen entgegen und startet die Python-Anwendung

**Installation der Module**

`pip install fastapi pydantic uvicorn`

# uvicorn

Starten des Servers mit automatischen reload
```
uvicorn main:app --reload
```

Dabei bedeutet:
```
uvicorn main:app
        │     │
        │     └── Variable "app" in main.py
        │
        └──────── Python-Datei main.py
```
**Aufruf der API im Browser**
```
http://127.0.0.1:8000
```

**Aufruf von Swagger im Browser**

```
http://127.0.0.1:8000/docs
```

**Aufruf der OpenAPI Spezifikation**

```
http://127.0.0.1:8000/openapi.json
```

