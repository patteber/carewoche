FROM python:3.11-alpine
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
RUN mkdir /mnt/data
COPY ./app/data/resource.json /mnt/data/resource.json
RUN rm -rf /code/app/data/
VOLUME [ "/mnt/data/" ]
RUN ln -s /mnt/data/ /code/app/
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
