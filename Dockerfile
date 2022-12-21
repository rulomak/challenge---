FROM python:3.10-alpine3.17

ENV PYTHONUNBUFFERD=1

WORKDIR /app


COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

