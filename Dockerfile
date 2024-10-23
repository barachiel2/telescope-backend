FROM python:3.9

# Install system dependencies
RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    libgdal-dev

# Set GDAL and GEOS library paths (if needed)
ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so
ENV GEOS_LIBRARY_PATH=/usr/lib/libgeos_c.so

# Set the working directory in the container
WORKDIR /code

# Copy requirements.txt and install Python dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . /code/

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
