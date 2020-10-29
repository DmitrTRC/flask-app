FROM python:3.8-alpine
COPY ./ /app
RUN pip install -r /app/requirements.txt
RUN echo "Dockerfile test message"
EXPOSE 5000
CMD python /app/hello.py
