# Deploying to Render

1. Push this repository to GitHub.
2. In Render, choose **New +** → **Blueprint** and select the repository. Render reads `render.yaml` and creates the Flask web service and PostgreSQL database.
3. When prompted, provide `ADMIN_EMAIL` and `ADMIN_PASSWORD` for the first admin account. Render generates `SECRET_KEY` automatically.
4. Deploy. The service installs `requirements.txt` and starts with Gunicorn; the database tables and configured admin are initialized on startup.

The included free PostgreSQL plan is intended for evaluation and expires after 30 days. Upgrade the database to a paid plan before then if you need to keep its data. The free web service may sleep when idle and take a short time to wake up.

To run locally, install the requirements and run `python run.py`. Local startup still creates the development admin account `admin@gmail.com` / `admin@123`; do not use those credentials in a public deployment.
