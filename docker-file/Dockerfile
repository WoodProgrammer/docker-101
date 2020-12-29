FROM python:latest
COPY requirements.txt .
COPY app.py .
RUN  pip3 install -r requirements.txt
ENTRYPOINT python3 app.py