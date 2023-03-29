# syntax=docker/dockerfile:1
FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY BookShy /code/
COPY .env /code/BookShy
EXPOSE 8000
# Setup GDAL
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin  python3-gdal

CMD ["gunicorn","--bind", ":8000", "BookShy.wsgi:application"]