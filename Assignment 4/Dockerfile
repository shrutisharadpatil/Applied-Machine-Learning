# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy required files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY score.py .
COPY model.pkl .
COPY vectorizer.pkl .

# Expose port Flask will run on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
