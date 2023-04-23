FROM python:latest
RUN apt-get update && apt-get install -y && rm -rf /var/lib/apt/lists/*
RUN mkdir -p 
WORKDIR /usr/src/app
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3", "manage.py", "migrate"]
ENTRYPOINT [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]