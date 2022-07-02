# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN chmod +x *.sh

RUN "./entrypoint.sh" 

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:80"]