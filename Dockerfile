FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE $PORT

CMD voila Mittelwertsatz.ipynb --port=$PORT --host=0.0.0.0 --no-browser --strip_sources=True
