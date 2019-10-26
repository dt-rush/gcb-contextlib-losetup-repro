#!/bin/sh -e
set -x

cd /workspace

# we are inside the dind container, starting up a local dockerd
nohup dockerd 2>&1 &
sleep 5  # wait for dockerd to spin up fully

export DOCKER_HOST=unix:///var/run/docker.sock

# create /workspace/disk.img
dd if=/dev/zero of=disk.img bs=1M count=16
# build container which runs repro.py
docker build -t inner-container -f Dockerfile.inner .
# attempt to run repro
docker run --privileged -v /workspace:/workspace inner-container
