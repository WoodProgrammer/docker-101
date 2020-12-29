FROM python
COPY requirements.txt /code/ 
COPY app.py /code/
RUN pip3 install -r /code/requirements.txt
ENTRYPOINT python3 /code/app.py