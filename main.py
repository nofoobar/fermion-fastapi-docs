from fastapi import FastAPI

app = FastAPI(title="Query Params", docs_url="/")

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
    {"item_name": "Qux"},
    {"item_name": "Quux"},
]

# TODO: Add a GET /items/ route
# It should accept two optional query parameters:
#   skip: int (default 0)
#   limit: int (default 3)
# Return the sliced fake_items_db like: fake_items_db[skip : skip + limit]


# TODO: Add a GET /search/ route
# It should accept one required query parameter:
#   q: str
# Return {"query": q}