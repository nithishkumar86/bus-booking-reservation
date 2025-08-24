FROM python:3.10-slim

# setting environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# working directory inside the container
WORKDIR /app

# install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*


# copying the current directory contents into the container
COPY . .

# install python dependencies
RUN pip install --no-cache-dir -e .

# EXPOSE the port the app runs on
#streamlit bydefault runs on this port 8051
#fastapi by default runs on this port 8000
EXPOSE 8501 
EXPOSE 8000

# command to run the application
CMD ["python", "app/main.py"]
