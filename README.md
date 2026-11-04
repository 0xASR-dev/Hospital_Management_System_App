# Hospital Management System

A Flask application for managing doctors, patients, availability, appointments, and treatment records. The application has three roles: administrator, doctor, and patient.

## Features

- Administrators manage doctor and patient accounts and appointments.
- Doctors manage their availability, appointments, and treatment records.
- Patients can register, find doctors, book appointments, and view treatment history.

## Requirements

- Python 3.11
- pip

## Run locally

Create and activate a virtual environment, then install the dependencies:

```shell
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

macOS or Linux:

```shell
source venv/bin/activate
```

Install dependencies and start the application:

```shell
pip install -r requirements.txt
python run.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000).

Local startup creates the SQLite database and tables if they do not exist. If `ADMIN_EMAIL` and `ADMIN_PASSWORD` are not set, running `python run.py` creates the local development administrator account `admin@gmail.com` with password `admin@123`. Do not use these credentials in a public deployment.

## Configuration

| Variable | Purpose |
| --- | --- |
| `SECRET_KEY` | Flask session signing key. Set a private value outside local development. |
| `DATABASE_URL` | SQLAlchemy database URL. Defaults to the local `hospital.db` SQLite file. |
| `ADMIN_EMAIL` | Email for creating the initial administrator account. Set together with `ADMIN_PASSWORD`. |
| `ADMIN_PASSWORD` | Password for the initial administrator account. |

The application creates its tables at startup. The initial administrator is created only if the configured email does not already exist.

## Deploy to Render

The repository includes a Render Blueprint in [`render.yaml`](./render.yaml) that defines the web service and PostgreSQL database. Follow the [Render deployment guide](./RENDER.md) to deploy it.

## Project layout

```text
app/
  models.py       Database models
  routes.py       Application routes
  templates/      Jinja templates
  utils.py        Shared utilities
static/           CSS, JavaScript, and images
config.py         Application configuration
run.py            Application entry point
requirements.txt  Python dependencies
```
