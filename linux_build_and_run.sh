#!/bin/bash

# 设置项目名称和镜像名称
PROJECT_NAME="qfnu-score-reminder"
IMAGE_NAME="qfnu-score-reminder"

# 构建Docker镜像
echo "Building Docker image..."
docker build -t $IMAGE_NAME .

# 检查构建是否成功
if [ $? -ne 0 ]; then
    echo "Docker image build failed!"
    exit 1
fi

# 删除已有的容器
docker rm -f $PROJECT_NAME

# 运行Docker容器，挂载当前目录到容器中，以便于不重建镜像修改代码，挂载当前目录到容器中，以便于不重建镜像修改代码
echo "Running Docker container..."
docker run -d -p 5000:5000 -v "$(pwd)":/app --name $PROJECT_NAME $IMAGE_NAME

# 检查容器是否成功启动
if [ $? -ne 0 ]; then
    echo "Docker container failed to start!"
    exit 1
fi

echo "Docker container is running." 