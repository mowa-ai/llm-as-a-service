"""Main entrypoint for the app."""


from fastapi import FastAPI


from llama import Llama
import config

MODEL = None

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    global MODEL
    if not MODEL:
        print("loading model")
        MODEL = Llama.build(
            ckpt_dir=config.CHECKPOINT_DIR,
            tokenizer_path=config.TOKENIZER_PATH,
            max_seq_len=config.MAX_SEQ_LEN,
            max_batch_size=config.MAX_BATCH_SIZE,
            model_parallel_size=config.MODEL_PARALLEL_SIZE,
        )
        print("model loaded")


@app.post("/process_message")
async def engine(prompt: str):
    dialog = [{"role": "user", "content": prompt}]

    results = MODEL.chat_completion(
        [dialog],
        max_gen_len=config.MAX_GEN_LEN,
        temperature=config.TEMPERATURE,
        top_p=config.TOP_P,
    )
    return results[0]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=config.HOST, port=config.PORT)
