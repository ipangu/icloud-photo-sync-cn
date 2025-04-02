FROM python:3.9-slim
# 使用阿里云镜像源
RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y libheif-dev && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . .
# 使用国内PyPI镜像
RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ \
    pyicloud==0.10.2 \
    python-dotenv==0.19.0
CMD ["python", "main.py"]
