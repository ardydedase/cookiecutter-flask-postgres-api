# {{cookiecutter.project_name}}

![CI](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/workflows/CI/badge.svg?branch=master)

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

## Continuous Deployment Pipeline

Go live with a Continuous Deployment Pipeline using GitHub and Render's Infrastructure as code.

### Create your repository on GitHub

Ensure that you are using the GitHub username and project slug that you have entered earlier when cookie cutting.
This will match the settings in the [render.yaml](render.yaml) file.

Your repo should be accessible in: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

* Check the deployed API: `<API URL>/healthcheck`
* Ensure that you have deleted your resources from Render when you're done.
