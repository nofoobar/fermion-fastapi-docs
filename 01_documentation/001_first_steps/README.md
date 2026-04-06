# FastAPI — First Steps

## What you'll build

In this lab, you'll create your very first FastAPI application from scratch.
By the end, you'll have a running web API with three endpoints.

---

## Background

**FastAPI** is a modern Python web framework for building APIs.
It uses standard Python type hints and generates interactive docs automatically.

A minimal FastAPI app looks like this:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"pong": True}
```

Key concepts:
- `FastAPI()` — creates the application instance
- `@app.get("/path")` — registers a **GET** route at that path
- The function below the decorator is called when someone hits that URL
- Returning a `dict` automatically becomes a JSON response

---

## Your Tasks

Open `main.py` and complete the following:

### Challenge 1 — Health check endpoint
Create a `GET /` route that returns:
```json
{"status": "ok"}
```

### Challenge 2 — Welcome message endpoint
Create a `GET /hello` route that returns:
```json
{"message": "Welcome to FastAPI"}
```

### Challenge 3 — Info endpoint
Create a `GET /info` route that returns:
```json
{"framework": "FastAPI", "language": "Python"}
```

---

## Running your server

Click the **Run Code** button, or run this in the terminal:

```bash
uvicorn main:app --reload --port 3000
```

Then check the browser preview on the right. You can also visit:
- `http://localhost:3000/docs` — interactive Swagger UI
- `http://localhost:3000/redoc` — ReDoc documentation

Once you're happy, click **Run Tests** to check your work!
