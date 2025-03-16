FROM python:3.12

EXPOSE 8080

#I got tmp files couldn't be removed warning when I tried it normally.
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

COPY . /tmp/
WORKDIR /app

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
