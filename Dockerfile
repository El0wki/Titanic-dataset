FROM python:3.11-slim

WORKDIR /app

COPY sla.py .

RUN pip install kagglehub
RUN pip install kagglehub[pandas-datasets]
RUN pip install matplotlib


CMD ["python", "sla.py"]