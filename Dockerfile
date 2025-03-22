FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# Install system dependencies in a single RUN command to reduce layers
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libegl1-mesa \
    libxrandr2 \
    libxss1 \
    libxcursor1 \
    libxcomposite1 \
    libasound2 \
    libxi6 \
    libxtst6 \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY system-hardware-info.py .

# Set display environment variable for GUI applications
ENV DISPLAY=:0

CMD ["python", "system-hardware-info.py"]
