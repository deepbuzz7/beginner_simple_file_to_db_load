FROM python:3.9.1
WORKDIR /app
COPY goodreads_data.csv goodreads_data.csv
COPY main.py main.py
COPY ddl.py ddl.py
RUN pip install pandas psycopg2-binary
ENTRYPOINT ["python","main.py"]
