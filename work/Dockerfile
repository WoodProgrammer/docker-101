FROM python
COPY app.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT python3 app.py