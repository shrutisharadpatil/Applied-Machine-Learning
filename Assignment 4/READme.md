# Assignment 4: Containerization & Continuous Integration

**Due: 8 April 2025**

This assignment focuses on Docker-based containerization and setting up basic continuous integration via Git pre-commit hooks.

## Containerization

### Objective
Create a Docker container for the Flask app developed in Assignment 3.

### Dockerfile Instructions
The Dockerfile performs the following:

- Uses Python base image.
- Installs required dependencies listed in `requirements.txt`.
- Copies `app.py` and `score.py` into the container.
- Launches the Flask app using `python app.py`.

### Build Docker Image

To build the image:
```bash
docker build -t train-model .
