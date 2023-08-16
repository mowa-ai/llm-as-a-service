"""Main entrypoint for the app."""


from typing import Annotated

from fastapi import Depends, FastAPI, status

from laas import api_models, config, engine

app = FastAPI()


@app.on_event("startup")
async def startup():
    engine.init_model()


@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=api_models.HealthCheck,
)
def get_health() -> api_models.HealthCheck:
    """
    ## Perform a Health Check
    Endpoint to perform a healthcheck on. This endpoint can primarily be used Docker
    to ensure a robust container orchestration and management is in place. Other
    services which rely on proper functioning of the API service will not deploy if this
    endpoint returns any other HTTP status code except 200 (OK).
    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return api_models.HealthCheck(status="OK")


@app.post("/process_message")
async def process_message(result: Annotated[str, Depends(engine.process_message)]) -> str:
    """
    ## Process message
    Endpoint to generate assistant answer to the chat history.
    Returns:
        str: Returns a string with generated answer by LLM
    """
    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=config.HOST, port=config.PORT)
