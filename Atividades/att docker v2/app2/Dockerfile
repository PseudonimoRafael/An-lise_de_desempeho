FROM python:3.12-slim

WORKDIR /app

COPY app2.py . 

RUN pip install flask

EXPOSE 8000

CMD ["python", "app2.py"]