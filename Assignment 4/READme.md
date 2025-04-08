# Assignment 4: Containerization & Continuous Integration  
**Due: 8 Apr 2025**

---

## Containerization

- Create a Docker container for the Flask app created in Assignment 3.
- Create a `Dockerfile` which contains the instructions to build the container, which include:
  - Installing the dependencies
  - Copying `app.py` and `score.py`
  - Launching the app by running `python app.py` upon entry
- Build the Docker image using the Dockerfile.
- Run the Docker container with appropriate port bindings.

### In `test.py`, write `test_docker(..)` function which does the following:
- Launches the Docker container using command line (e.g. `os.system(..)`, `docker build` and `docker run`)
- Sends a request to the localhost endpoint `/score` (e.g. using `requests` library)
- For a sample text:
  - Checks if the response is as expected
- Closes the Docker container.

- In `coverage.txt`, produce the coverage report using `pytest` for the tests in `test.py`.

---

## Continuous Integration

- Write a pre-commit git hook that will run the `test.py` automatically every time you try to commit the code to your local `main` branch.
- Copy and push this pre-commit git hook file to your GitHub repository.
