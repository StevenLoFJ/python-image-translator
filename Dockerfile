FROM python:3.9-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y tesseract-ocr \
    && apt-get clean

ENV IMG_DIR=test.py \

COPY . /app

RUN pip install --no-cache-dir pytesseract pillow deep_translator

# Run script
CMD [ "python", "img-translator.py" ]
