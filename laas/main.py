"""Main entrypoint for the app."""


from typing import Annotated
from fastapi import Depends, FastAPI

from laas import config, engine


app = FastAPI()


@app.on_event("startup")
async def startup():
    engine.init_model()


@app.post("/process_message")
async def process_message(result: Annotated[str, Depends(engine.process_message)]) -> str:
    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=config.HOST, port=config.PORT)
