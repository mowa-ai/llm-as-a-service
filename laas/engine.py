from laas import api_models, config
import torch
from transformers import pipeline

MODEL = None


def get_model():
    global MODEL
    if not MODEL:
        print("loading model")
        MODEL = pipeline(
            "text-generation",
            model=config.MODEL_NAME,
            device=0,
            torch_dtype=torch.float16,
        )
    return MODEL

def process_message(engine_input: api_models.EngineInput) -> str:
    model = get_model()
    output = model(
        text_inputs=engine_input.message,
        max_length=config.MAX_GEN_LEN,
    )
    return output[0]["generated_text"][len(engine_input.message):].strip()
