# llm-as-a-service
Simple FastAPI service for LLAMA-2 7B chat model.

Current version supports only `7B-chat` model.

Tested on a single Nvidia L4 GPU (24GB) at GCP (machine type `g2-standard-8`).


# Docker
Install nvidia runtime for docker first: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

```
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
  && \
    sudo apt-get update

sudo apt-get install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```
## Building
```bash
docker build -t laas .
```

## Run
Save models in your home dir
```bash
docker run --runtime=nvidia -v $(pwd)/llama-2-7b-chat:/app/llama-2-7b-chat  -v {$HOME}/.cache/huggingface/hub/:/root/.cache/huggingface/hub/ --gpus all -p 8080:8080 laas 
```

# How to run

## Install all dependecies
Run:
```shell
poetry install
```

## Download llama-2 model
Download `llama-2-7b-chat` model accordingly to the instruction from [llama repository](https://github.com/facebookresearch/llama/tree/ea9f33d6d3ea8ed7d560d270986407fd6c2e52b7).

## Setup environment variables
```shell
export RANK="0"
export WORLD_SIZE="1"
export MASTER_ADDR="0.0.0.0"
export MASTER_PORT="2137"
export NCCL_P2P_DISABLE="1"
export OMP_NUM_THREADS=4  # optional
```


## Start the server
Run the following command:
```shell
python laas/main.py
```

## Use server
To learn more about endpoints go to http://0.0.0.0:8080/docs


# Tests

## pytest

### Without loading LLM
To run fast tests (no LLM loaded) run
```bash
pytest
```

### With loading LLM
For longer tests run
```bash
pytest --runslow
```



