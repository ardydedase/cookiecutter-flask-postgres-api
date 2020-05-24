FROM python:3.6

RUN mkdir -p /flask-app
WORKDIR /flask-app

# Copy files
COPY ./requirements.txt ./
COPY ./setup.py ./
# COPY ./run-migrations.sh ./

# Copy folders
COPY ./src ./src

# Install packages
RUN pip install -r requirements.txt

# Run flask app
EXPOSE 5000
ENV FLASK_APP="src/main.py" FLASK_DEBUG=1 FLASK_ENV=docker
CMD ["flask", "run", "-h", "0.0.0.0"]