"""Main entrypoint for the app."""


from fastapi import FastAPI


from llama import Llama

MODEL = None

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    ckpt_dir: str = "llama-2-7b-chat/"
    tokenizer_path: str = "tokenizer.model"
    max_seq_len: int = 512
    max_batch_size: int = 8
    global MODEL
    print("loading model")
    MODEL = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
        model_parallel_size=1,
    )
    print("model loaded")


@app.post("/process_message")
async def engine(prompt: str):
    temperature: float = 0.6
    top_p: float = 0.9
    max_gen_len: int = 64
    dialog = [{"role": "user", "content": prompt}]

    results = MODEL.chat_completion(
        [dialog],
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,
    )
    return results[0]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
    )
