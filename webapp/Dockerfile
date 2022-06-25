FROM python:3.9-buster

RUN apt-get update -y

COPY ./webapp/app /app
RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 9001
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "9001"]