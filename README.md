# llm-as-a-service

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
## Automatic setup
Script checks all the requirements, downloads the model, builds the image and starts the server.
```bash
./setup.sh
```
