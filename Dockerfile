FROM python:3.9.16-slim

ENV API_TRIAL_KEY=''

# need curl and gcc
RUN apt update -y \
    && apt install -y curl git ffmpeg \
    && apt-get clean \
    && pip install -U Flask cohere openai-whisper waitress flask-cors

WORKDIR /app/

COPY app.py /app

CMD ["python3", "app.py"]

EXPOSE 8000
