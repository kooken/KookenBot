# Habit Tracking Application

A Django-based habit tracker where users can create, manage, and track habits with integrated Telegram reminders (Kooken bot). Key features include:

- **CRUD for Habits**: Manage personalized and public habits.
- **Task Scheduling**: Celery-powered reminders for habit notifications.
- **Custom Validators**: Ensure correct habit setup (e.g., time, linked habits).
- **Pagination**: Habits listed with pagination (5 per page).
- **Integration**: Telegram for sending reminders.
- **Technologies**: Python, Django, DRF, PostgreSQL, Celery.

To run it, you need to:

- Make sure that Docker Desktop is available on your device
- After deploying the project, you need to create a .env file in which to specify the data for the environment variables
- The variables are in the .env.example file
- Dependencies are written in the requirements.txt file
- Build and run the project using the command: docker-compose up --build
- After starting the server in Docker, follow the link
