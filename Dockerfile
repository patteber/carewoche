FROM python:3.11-alpine
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
VOLUME [ "/mnt/data/" ]
RUN rm /code/app/resource.json
RUN ln -s /mnt/data/resource.json /code/app/resource.json
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
