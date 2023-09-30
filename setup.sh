
echo "Checking if nvidia drivers are installed"

nvidia-smi &> /dev/null
if [ $? -eq 0 ]; then
    echo "Drivers installed"
else
    echo "Nvidia drivers not installed"
    exit 1
fi


echo -e "\nChecking GPU count"

GPU_COUNT=$(nvidia-smi --list-gpus | wc -l)
if [ $GPU_COUNT -eq 0 ]; then
    echo "No GPU found"
    exit 1
else
    echo "Found $GPU_COUNT GPUs"
fi


echo -e "\nChecking GPU memory > 20 GB"

GPU_MEMORY=$(nvidia-smi --query-gpu memory.total --format=csv,nounits,noheader)
if [ $GPU_MEMORY -lt 20000 ]; then
    echo "At least 20GB of VRAM needed"
    exit 1
else
    echo "Found $GPU_MEMORY MiB of VRAM in first GPU"
fi


echo -e "\nChecking if docker is installed"

docker run hello-world &> /dev/null
if [ $? -eq 0 ]; then
    echo "Docker installed"
else
    echo "Docker not installed"
    exit 1
fi

echo -e "\nChecking if runtime nvidia is installed in Docker"

docker run --runtime=nvidia nvidia/cuda:12.2.0-base-ubuntu22.04 nvidia-smi &> /dev/null
if [ $? -eq 0 ]; then
    echo "Nvidia runtime installed"
else
    echo "Command failed. Install drivers from https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html"
    exit 1
fi

echo -e "\nDownloading CODE LLAMA 34B Instruct"
mkdir -p models/34B/
cd models/34B/
wget -nc https://huggingface.co/TheBloke/CodeLlama-34B-Instruct-GGUF/resolve/main/codellama-34b-instruct.Q3_K_M.gguf
cd ../..

echo -e "\nBuilding docker image"
docker build -t laas .


echo -e "\nStarting server (it will take a while - up to 10 minutes)"
docker run --runtime=nvidia -v $(pwd)/models/:/app/models  --gpus all -p 8080:8080 laas
