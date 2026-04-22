from fastapi import FastAPI

app = FastAPI(title="Path Parameters Lab", docs_url="/")


# TODO: Create a GET route at /items/{item_id}
# item_id should be typed as int
# Return {"item_id": item_id}


# TODO: Create a GET route at /users/{username}
# username should be typed as str
# Return {"username": username}