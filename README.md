[![MongoDB CI](https://github.com/software-students-spring2025/5-final-final-push/actions/workflows/mongo-db-tests.yml/badge.svg)](https://github.com/software-students-spring2025/5-final-final-push/actions/workflows/mongo-db-tests.yml)

[![Web App CI](https://github.com/software-students-spring2025/5-final-final-push/actions/workflows/web-app.yml/badge.svg)](https://github.com/software-students-spring2025/5-final-final-push/actions/workflows/web-app.yml)

# Final Project

An exercise to put to practice software development teamwork, subsystem communication, containers, deployment, and CI/CD pipelines. See [instructions](./instructions.md) for details.

# Team Members

- Lana Davydov [Github Link](https://github.com/lanadavydov)
- Samantha Lin [Github Link](https://github.com/sal2948)
- Joylyn Gong [Github Link](https://github.com/joylyngong)
- Jason Mai [Github Link](https://github.com/JasonMai233)

# Project Description
Originating from Japan, our web app Haiku Blossom will allow for users to write, browse, and share Haiku poetry. Users can choose a theme for their poem they would like to work with, in addition to three words that will be relevant to the content of the poem.

# Running Full Application

To Build and Run Full Application:
1. `docker-compose up --build`
2. Visit `http://localhost:5001/`

To shut down: `docker-compose down -v`

# Running on MongoDB

To build and run MongoDB:
```
docker run --name mongodb -d -p 27017:27017 \
  -v $(pwd)/mongo-init:/docker-entrypoint-initdb.d \
  mongo --auth
```

# Running Unit Tests
Running unit tests locally on the web app:

Make sure you've install pytest first:
```
pip install pytest
```

```
cd web-app
```

```
pipenv install --dev
```

```
PYTHONPATH=. pipenv run pytest tests/
```

# Accessing Docker image on DockerHub

Docker image on DockerHub: https://hub.docker.com/repository/docker/sal9791/final-push/general