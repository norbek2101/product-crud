FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /product-crud

# Copy the requirements file and install dependencies
COPY ./requirements.txt /product-crud/
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . /product-crud/

# Install additional packages required for PostgreSQL
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*


# CMD to start the web server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
