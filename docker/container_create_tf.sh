xhost +
sudo docker run --gpus all -it  -v /home/cfs/docker/Realtime-Stocker:/workspace/ -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -e XAUTHORITY -e NVIDIA_DRIVER_CAPABILITIES=all --env QT_X11_NO_MITSHM=1 -p 2200:8888 nvcr.io/nvidia/tensorflow:19.07-py3

