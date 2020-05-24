# {{cookiecutter.project_name}}

## Run locally with docker

Use docker-compose
```
docker-compose up
```

## Run the flask app outside docker

Bring up the Postgres DB container
```
docker-compose up -d db
```

Install requirements.
`mypy` takes some time to install
```
pip install -r requirements.txt
```

Initialise environment variables. The `.env` is used in `docker-compose.yml`.
```
export FLASK_APP="src/main.py"
export POSTGRES_URL="127.0.0.1:54320"
export POSTGRES_DB="{{cookiecutter.project_name}}"
export POSTGRES_USER="postgres"
export POSTGRES_PASSWORD="example"
```

Run migrations
```
chmod+x run-migrations.sh
./run-migrations.sh
```

Run flask
```
# initialise environment variables
flask run
```

## Run tests

```
py.test -vv
```


## Run with gunicorn
For production.
```
cd src && gunicorn main:app
```

## Build and run commands in render.com

Build command
```
pip install -r requirements.txt && ./run-migrations.sh
```

Run the app
```
cd src && gunicorn app:app
```