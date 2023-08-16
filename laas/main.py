"""Main entrypoint for the app."""


from fastapi import FastAPI

from laas import config, engine


app = FastAPI()


@app.on_event("startup")
async def startup():
    engine.init_model()


@app.post("/process_message")
async def process_message(prompt: str):
    return engine.process_message(prompt)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=config.HOST, port=config.PORT)
