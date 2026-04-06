# FastAPI — First Steps

## What you'll build

In this lab, you'll make your first FastAPI route return a proper JSON response.

---

## Background

**FastAPI** is a modern Python web framework for building APIs.
It uses standard Python type hints and generates interactive docs automatically.

A minimal FastAPI app looks like this:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Key concepts:
- `FastAPI()` — creates the application instance
- `@app.get("/")` — registers a **GET** route at the root path
- The function below the decorator runs when someone hits that URL
- Returning a `dict` automatically becomes a JSON response

---

## Your Task

Open `main.py`. The route and function are already defined — you just need to complete the return statement.

### Challenge — Return hello world

Make `GET /` return:
```json
{"hello": "world"}
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
