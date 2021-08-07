# Course Registration Application

This is a Python project built on the following tech stacks:

- Flask
- Flask-Restful
- SQLAlchemy
- MySQL
- Gunicorn WSGI server

## Project initialization

```bash
source init.sh
```

_The above command is also used to re-initialize the development environment._

## Starting the application in development mode

```bash
source init.sh
python app/main.py
```

## Run the application in production mode with a WSGI server

```bash
source init.sh
gunicorn --chdir=app --workers=4 main:app
```
