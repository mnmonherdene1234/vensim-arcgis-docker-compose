FROM python:latest

WORKDIR /code
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src ./src

CMD [ "uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "1000", "--reload" ]