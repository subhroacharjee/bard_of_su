FROM python:3.9-slim
ARG SA_PATH

WORKDIR /root/app

COPY ${SA_PATH} /root/.config/
COPY ./requirements.txt /root/app/requirements.txt
ENV GOOGLE_APPLICATION_CREDENTIALS /root/.config/service.json
RUN pip install --no-cache-dir --upgrade -r /root/app/requirements.txt

COPY ./src /root/app/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]