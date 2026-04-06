from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    # TODO: Return a dictionary with the key "hello" and the value "world"
    return {}