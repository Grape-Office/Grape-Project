FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY data.json .
COPY nofity.py .
COPY banner.py .
COPY domain_checker.py .
COPY toCSV.py .
COPY exel2json.py .
COPY temp_keyword.py .
COPY toCSV.py .

ENTRYPOINT ["python", "main.py"]
CMD []
