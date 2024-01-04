FROM python:3.7-slim
WORKDIR /app
COPY . .
RUN apt-get update
RUN apt-get -y install python3-pip python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0
RUN pip install -r requirements.txt
CMD ["python", "sample.py"]