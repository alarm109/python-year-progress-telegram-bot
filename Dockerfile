# Use the official Python 3.10 image as the base image
FROM python:3.10
# Update package lists and install the cron package
RUN apt-get update && apt-get -y install cron
# Set the working directory to /app
WORKDIR /app

# Copy the cron job schedule file to the cron.d directory
COPY run-daily-cron /etc/cron.d/crontab
# Copy the main Python script to the /app directory
COPY main.py /app/main.py
# Copy the .env file containing environment variables to the /app directory
COPY .env /app/.env
# Create an empty log file for cron
RUN touch /var/log/cron.log

# Copy the requirements.txt file to the /app directory
COPY requirements.txt /app/requirements.txt
# Upgrade pip
RUN pip install --root-user-action=ignore --upgrade pip
# Install the Python dependencies listed in requirements.txt
RUN pip install --root-user-action=ignore -r requirements.txt

# Set the correct permissions for the cron job schedule file
RUN chmod 0644 /etc/cron.d/crontab
# Install the cron job schedule file to the cron daemon's configuration
RUN /usr/bin/crontab /etc/cron.d/crontab

# Start the cron daemon and continuously print the cron log
CMD cron && tail -f /var/log/cron.log