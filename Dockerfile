FROM python:3.10-slim-bullseye

WORKDIR /app/

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD cd server && python manage.py migrate && python manage.py runserver 0.0.0.0:8000;