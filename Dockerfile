FROM python:3.8

COPY . /app
WORKDIR /app
 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8051

CMD ["opyrator", "launch-ui", "app:babyshark_brooklyn_ainft_chat"] 
