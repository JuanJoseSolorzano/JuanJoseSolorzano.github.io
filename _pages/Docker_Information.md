---
layout: page
title: Docker Information
permalink: /pages/Docker_Information/
date: 2021-07-16
---

# Create a Debian Dockerfile

log-in into Docker.com and run docker desktop and log-in as well.

create a file:
```bash
touch Dockerfile
vim ./Dockerfile
```
Add the following information:
```bash
# Default Debian Distro
FROM debian:bookworm
# Non-Interactive prompts to disable the pop-up
ENV DEBIAN_FRONTEND=noninteractive
# Update the OS
RUN apt update && apt install -y curl vim git build-essential && apt clean && rm -rf /var/lib/apt/lists/*
# Create a personal workpace directory
WORKDIR /workspace
# Set the default shell
CMD ["bash"]
```

run:

```bash
docker build -t my-full-debian .
docker run -it --rm my-full-debian
```