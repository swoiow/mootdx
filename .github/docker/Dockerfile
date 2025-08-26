# .github/docker/Dockerfile
ARG PYTHON_VERSION=3.13
FROM python:${PYTHON_VERSION}-alpine as builder

RUN pip install --upgrade pip && pip install build wheel setuptools

WORKDIR /app
COPY . .

# 构建 wheel 包（默认输出到 /app/dist）
RUN pip install -r requirements.txt && python setup.py bdist_wheel
