FROM python:3.8-slim
RUN mkdir /app
WORKDIR /app
COPY ./app/requirements.txt /app
RUN pip3 install -r requirements.txt
COPY ./app /app
EXPOSE 8000
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]