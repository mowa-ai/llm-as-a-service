FROM nvidia/cuda:12.2.0-base-ubuntu22.04


WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*


RUN pip install "poetry==1.6.1"


COPY poetry.lock pyproject.toml /app/


COPY . /app


RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi


EXPOSE 8080
# ENV RANK="0"
# ENV WORLD_SIZE="1"
# ENV MASTER_ADDR="0.0.0.0"
# ENV MASTER_PORT="2137"
# ENV NCCL_P2P_DISABLE="1"
# ENV OMP_NUM_THREADS=4 


CMD exec uvicorn laas.main:app --host 0.0.0.0 --port 8080