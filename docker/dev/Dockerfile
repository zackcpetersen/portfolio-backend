# Base Image
FROM python:3.9-slim-buster

# Set working directory (same as cd /usr/src/app
ENV APP_HOME=/usr/src/app
WORKDIR $APP_HOME

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1  # prevents python from copying .pyc files into container
ENV PYTHONUNBUFFERED 1  # ensures that Python output is logged to the terminal, making it possible to monitor Django logs in realtime

# Install dependencies
RUN pip install --upgrade pip
# copy & install requirements
COPY ./requirements.txt $APP_HOME
# install requirements.txt to container
RUN pip install -r requirements.txt

# Copy entrypoint.sh
#COPY ./docker/dev/entrypoint.sh $APP_HOME
#RUN chmod +x $APP_HOME/entrypoint.sh

COPY . .
# run entrypoint script and runserver
ENTRYPOINT ["/usr/src/app/docker/dev/entrypoint.sh"]
