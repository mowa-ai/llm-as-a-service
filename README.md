# llm-as-a-service
Simple FastAPI service for LLAMA-2 7B chat model.

Current version supports only `7B-chat` model.


# How to run

## Download llama-2 model
Download `llama-2-7b-chat` model accordingly to the instruction from [llama repository](https://github.com/facebookresearch/llama/tree/ea9f33d6d3ea8ed7d560d270986407fd6c2e52b7).

## Setup environment variables
```shell
export RANK="0"
export WORLD_SIZE="1"
export MASTER_ADDR="0.0.0.0"
export MASTER_PORT="2137"
export NCCL_P2P_DISABLE="1"
```


## Start the server
Run the following command:
```shell
python laas/main.py
```