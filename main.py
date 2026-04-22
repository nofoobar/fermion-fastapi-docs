from fastapi import FastAPI

app = FastAPI(title="FastAPITutorial.com", docs_url="/")


@app.get("/message")
def read_root():
    # TODO: Return a dictionary with the key "hello" and the value "world"
    return {"message": "give it a try"}