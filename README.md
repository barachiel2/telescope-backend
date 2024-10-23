Telescope Fullstack Case Study
This project is a Django application with PostgreSQL as the database, built using Docker. It provides a simple API and web interface for managing portfolio-related data.

Getting Started
Prerequisites
Ensure you have the following software installed on your machine:

Docker: You can download and install Docker Desktop from here.
Installation
Clone the repository:

git clone https://github.com/yourusername/telescope-fullstack-case.git
cd telescope-fullstack-case
Set up environment variables:

Create a .env file at the root of the project with the following content (adjust as necessary for your local setup):

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db

Build and Run the Project
Build the Docker containers:
Run the following command to build the Docker containers for the application:

docker compose build
Start the containers:

After the containers are built, start them with:

docker compose up
This will start both the Django application and PostgreSQL database.

Apply database migrations:
In a separate terminal, run the following command to apply the migrations to the database:

docker compose exec web python manage.py migrate
Create a superuser (optional):
If you want access to the Django admin panel, create a superuser with:

docker compose exec web python manage.py createsuperuser

Access the Application
The Django application will be running at: http://localhost:8000.
The Django admin panel can be accessed at: http://localhost:8000/admin.
Running Tests
To run the unit tests for the project, use the following command:

docker compose exec web python manage.py test
Stopping the Containers
To stop the running containers, press CTRL + C in the terminal where docker compose up was run, or execute the following command:

docker compose down
Useful Docker Commands
Rebuild the containers:

docker compose build
View running containers:

docker ps
Access the running Django container:

docker compose exec web /bin/bash
Technologies Used
Django: Python web framework
PostgreSQL: Relational database
Docker: For containerization
Docker Compose: For managing multi-container Docker applications
Notes
Ensure Docker Desktop is running when you execute Docker commands.
Adjust environment variables in the .env file as necessary for your setup.
