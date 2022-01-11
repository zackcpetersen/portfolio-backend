# Base Image
FROM python:3.9-buster

# Set working directory (same as cd /usr/src/app
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1  # prevents python from copying .pyc files into container
ENV PYTHONUNBUFFERED 1  # ensures that Python output is logged to the terminal, making it possible to monitor Django logs in realtime

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Can try with pipenv too
#RUN pip install --upgrade pip \
#    && pip install pipenv
#COPY Pipfile .
#RUN pipenv lock -r > requirements.txt \
#    && pipenv install requirements.txt


# Copy entrypoint.sh
COPY entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh \
    && chmod +x /usr/src/app/entrypoint.sh

# Copy source code into container, expose port 8000
COPY . .
#EXPOSE 8000
#
## Set command to run when container starts
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
