# Profiles REST API

A REST API built with **Django** and **Django REST Framework**, featuring a custom
user model with email-based authentication and token authentication for API access.

This project was built while following the Udemy course **"How to Build a Backend
REST API with Python & Django - Advanced"** by Mark Winterbottom (LondonAppDev). The
original course project structure comes from
[LondonAppDev/profiles-rest-api](https://github.com/LondonAppDev/profiles-rest-api);
this repository contains my own implementation and additional changes made while
working through the course, including switching the local development setup from
Vagrant to Docker.

## About

The project is fully containerized with **Docker** and **Docker Compose**, so it can
be run locally without installing Python or any dependencies on the host machine.
The original course material uses Vagrant + VirtualBox for the development
environment; this version replaces that with Docker for a lighter and more portable
setup.

### Features

- Custom user model using email instead of username
- Token-based authentication (`Authorization: Token <key>`)
- ViewSets and Routers for clean, RESTful endpoint structure
- Django admin panel for managing users
- Dockerized development environment (SQLite, no external services required)
- Dev Container support for VS Code

### Tech Stack

- Python 3.13
- Django 6.1
- Django REST Framework
- Docker & Docker Compose
- SQLite (development)

## Getting Started

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and
  running

### Running locally

```bash
git clone https://github.com/mmdparimoon/Profiles-rest-api.git
cd Profiles-rest-api
docker compose up --build
```

The API will be available at `http://localhost:8000`.

### Environment variables

Copy the example environment file and fill in your own values:

```bash
cp env.example .env
```

At minimum, set a `SECRET_KEY` for Django.

### Common commands

Run these from the project root while the containers are up:

```bash
# Apply database migrations
docker compose exec web python manage.py migrate

# Create a new migration after changing models.py
docker compose exec web python manage.py makemigrations

# Create an admin user
docker compose exec web python manage.py createsuperuser

# Run the test suite
docker compose exec web python manage.py test

# Open a shell inside the running container
docker compose exec web bash
```

## Project Structure

```
Profiles-rest-api/
├── Profiles_project/     # Django project settings and root URL config
├── profiles_api/         # Main app: models, views, serializers, admin
├── .devcontainer/         # VS Code Dev Container configuration
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── manage.py
```

## Course Reference

This repository was created as a learning project. Credit for the original course
curriculum and starter code goes to Mark Winterbottom / LondonAppDev. This version
diverges from the original in its use of Docker instead of Vagrant for local
development, along with some additional configuration and fixes made along the way.

## License

This project is for educational purposes, built while following the course
referenced above.