from laas import api_models, config
import torch

MODEL = None
MODEL_CTRANSFORMERS = True


def load_transformers_model():
    from transformers import pipeline

    print("load_transformers_model")

    model = pipeline(
        "text-generation",
        model=config.MODEL_NAME,
        device=0,
        torch_dtype=torch.float16,
    )

    return model


def load_ctransformers_model():
    from ctransformers import AutoModelForCausalLM

    print("load_ctransformers_model")

    model = AutoModelForCausalLM.from_pretrained(
        "./models/34B/codellama-34b-instruct.Q3_K_M.gguf",
        model_type="llama",
        gpu_layers=100,
        context_length=config.MAX_LENGTH,
        temperature=0.0,
    )
    return model


def load_model():
    if MODEL_CTRANSFORMERS:
        return load_ctransformers_model()
    else:
        return load_transformers_model()


def get_model():
    global MODEL
    if not MODEL:
        print("loading model")
        MODEL = load_model()
    return MODEL


def process_message(engine_input: api_models.EngineInput) -> str:
    model = get_model()
    if MODEL_CTRANSFORMERS:
        return model(engine_input.message, max_new_tokens=512).strip()

    output = model(
        text_inputs=engine_input.message,
        max_length=config.MAX_LENGTH,
        return_full_text=False,
    )
    return output[0]["generated_text"].strip()
