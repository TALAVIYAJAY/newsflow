# Use the official Python 3.10 image as base
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy all project files
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the application port
EXPOSE 8000

# Default command (only starts the server)
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]
