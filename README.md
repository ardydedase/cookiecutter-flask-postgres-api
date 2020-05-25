![CI](https://github.com/ardydedase/cookiecutter-flask-postgres-api/workflows/CI/badge.svg)

# Cookiecutter for Flask API with Postgres

Project template for Flask API.

## What's included
* Go live with a Continuous Deployment Pipeline using GitHub and Render's Infrastructure as Code. See sample [IaC file here](https://github.com/ardydedase/flask-postgres-api/blob/master/render.yaml).
* Works with SQLAlchemy / Postgres DB out of the box.
* Uses mypy for static type checks.

## Reference app

There is a sample reference package generated from our cookiecutter which you can refer to in here: https://github.com/ardydedase/flask-postgres-api.

Deploy the Sample Repo built from this cookiecutter to Render.com:

<a href="https://render.com/deploy?repo=https://github.com/ardydedase/flask-postgres-api">
  <img src="https://render.com/images/deploy-to-render-button.svg">
</a>

* Check the deployed API: `<API URL>/healthcheck`
* Ensure that you have deleted your resources from Render when you're done.


## Usage

1. Install cookiecutter

        pip install cookiecutter

1. Cookie cut the template.

        cookiecutter git@github.com:ardydedase/cookiecutter-flask-postgres-api.git

1. Enter the values accordingly. Pick your project name.


1. Change the working directory to the generated folder, same name as the project slug.

        cd <project_slug>


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
export POSTGRES_URL="127.0.0.1:5432"
export POSTGRES_DB="mydb"
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