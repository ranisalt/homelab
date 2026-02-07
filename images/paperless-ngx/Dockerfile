# syntax=docker/dockerfile:1
FROM ghcr.io/paperless-ngx/paperless-ngx
RUN apt-get update && apt-get install -y --no-install-recommends tesseract-ocr-eng tesseract-ocr-por tesseract-ocr-swe && rm -rf /var/lib/apt/lists/*
