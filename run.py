import os

from app import create_app, db
from app.models import User, DoctorProfile, PatientProfile
from werkzeug.security import generate_password_hash

app = create_app()

def create_admin_if_missing(admin_email, admin_password):
    admin = User.query.filter_by(email=admin_email).first()
    if not admin:
        admin = User(
            name="Admin",
            email=admin_email,
            role="admin",
            password_hash=generate_password_hash(admin_password)
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin user created:", admin_email)

with app.app_context():
    db.create_all()
    admin_email = os.getenv("ADMIN_EMAIL")
    admin_password = os.getenv("ADMIN_PASSWORD")
    if bool(admin_email) != bool(admin_password):
        raise RuntimeError("Set both ADMIN_EMAIL and ADMIN_PASSWORD to create the initial admin.")
    if admin_email and admin_password:
        create_admin_if_missing(admin_email, admin_password)

if __name__ == "__main__":
    if not os.getenv("ADMIN_EMAIL") and not os.getenv("ADMIN_PASSWORD"):
        with app.app_context():
            create_admin_if_missing("admin@gmail.com", "admin@123")
    app.run(debug=os.getenv("FLASK_DEBUG", "").lower() in ("1", "true"))
