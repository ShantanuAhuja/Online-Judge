# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install basic tools
RUN apt-get update && apt-get install -y \
g++-14 \
clang \
gcc \
python3 \
python3-pip \
default-jdk \
libc++-dev \
libc++abi-dev \
libstdc++-12-dev \
&& apt-get clean

# Dynamically set JAVA_HOME




# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install django and populate the database
RUN pip install --no-cache  django
RUN python manage.py makemigrations
RUN python manage.py migrate

# Make port 5000 available to the world outside this container
EXPOSE 8000

# Setting file for main app ie onlinejudge
ENV DJANGO_SETTINGS_MODULE=onlinejudge.settings
ENV PYTHONUNBUFFERED=1
ENV JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH


# Run the application
CMD ["python", "manage.py","runserver","0.0.0.0:8000"]
