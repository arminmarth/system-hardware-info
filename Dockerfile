FROM python:3-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update
RUN apt-get install -y libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

RUN pip install -r requirements.txt

COPY system-hardware-info.py .

CMD ["python", "system-hardware-info.py"]
