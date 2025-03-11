# Use the official Python 3.13 image
FROM python:3.13

# Set the working directory
WORKDIR /app

# Copy only requirements first (leveraging Docker caching)
COPY requirements.txt .

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Create a non-root user and switch to it
RUN useradd -m django_user
USER django_user

# Expose port for Django application
EXPOSE 8000

# Run migrations and start the server
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
