# Getting started

## Environment variables

Create `.env` file and add the required environment variables.

```
cp .env.example .env
```

# Using Makefile to run commands

You can also use the provided Makefile to build, run, stop, and remove the Docker container for the application. Here are the available commands:

## Build the Docker image

```
make build
```

## Run the Docker container

```
make run
```

## Stop the running Docker container

```
make stop
```

## Remove the Docker container

```
make remove
```

Replace `${APPLICATION_NAME}` with the desired name for your application. By default, it is set to `year-progress-telegram-bot`.

# Running with Docker

## Build

```
docker build -t year-progress-telegram-bot .
```

## Run

```
docker run -d --name year-progress-telegram-bot year-progress-telegram-bot
```

To run just run `python3 main.py` file with python3.

# Running locally

Create a virtual environment with command in the terminal:

```
python3 -m venv .venv
```

To activate virtual environment run:

```
source .venv/bin/activate
```

Install the required dependencies in virtual environment

```
pip install -r requirements.txt
```
