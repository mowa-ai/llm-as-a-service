from typing import Annotated

from fastapi import Depends
from llama import Llama

from laas import api_models, config

MODEL = None


def init_model():
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


def preprocess_message(engine_input: api_models.EngineInput) -> list[dict]:
    return engine_input.model_dump()["history"]


def process_message(dialog: Annotated[list[dict], Depends(preprocess_message)]) -> str:
    results = MODEL.chat_completion(
        [dialog],
        max_gen_len=config.MAX_GEN_LEN,
        temperature=config.TEMPERATURE,
        top_p=config.TOP_P,
    )
    return results[0]["generation"]["content"].strip()
