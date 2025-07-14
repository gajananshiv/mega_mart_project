🛒 MegaMart – E-Commerce Backend (Django + DRF)
MegaMart is a scalable, production-ready e-commerce backend built with Django REST Framework, JWT authentication, custom user model, and modular app structure. This project is built using GitHub feature-branch workflow and follows real-world development practices.

✅ Features
🔐 JWT Authentication (djangorestframework-simplejwt)

🧑‍💼 Custom User Model with Email Login

📦 Product Catalog: Brands, Categories, Images

🛒 Cart, Orders, Checkout APIs (coming soon)

📤 Product image upload and deletion with Django signals

📄 API Documentation with Swagger (drf-yasg)

📂 Modular App Structure (apps/ folder)

⚙️ Environment Configurations with .env

🧪 Unit Testing using pytest, pdb, logging

🧠 GitHub Workflow (develop → feature → PR → merge)

🧾 Requirements managed via requirements.txt

🗂️ Project Structure
bash
Copy
Edit
mega_mart_backend/
├── apps/
│   ├── users/
│   ├── products/
│   ├── orders/
│   ├── cart/
├── media/                   # Product images
├── static/                  # Static files
├── mega_mart_proj/          # Main Django settings
├── manage.py
├── .env                     # Env variables
├── .gitignore
├── requirements.txt
└── README.md
🛠️ Setup Instructions
Clone the repo

bash
Copy
Edit
git clone https://github.com/<your-username>/mega_mart_project.git
cd mega_mart_project
Create and activate virtual environment

bash
Copy
Edit
python -m venv env
source env/bin/activate  # For Linux/macOS
env\Scripts\activate     # For Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run migrations

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Create superuser

bash
Copy
Edit
python manage.py createsuperuser
Run development server

bash
Copy
Edit
python manage.py runserver
📄 Swagger API Docs
Access full API docs at:
📍 http://127.0.0.1:8000/swagger/

🔐 JWT Authentication
Token Endpoint:

bash
Copy
Edit
POST /api/token/
{
  "email": "user@example.com",
  "password": "yourpassword"
}
Headers for protected APIs:

pgsql
Copy
Edit
Authorization: Bearer <your-access-token>
🧪 Testing
Run test suite with pytest:

bash
Copy
Edit
pytest
Tests include:

Model tests

Serializer validation tests

Signal tests

Debugging via pdb, print(), and logging

🧠 GitHub Flow Used
main = production branch

develop = staging branch

feature/* = development branches

Workflow:

bash
Copy
Edit
git checkout -b feature/<feature-name>
# Work → Commit → Push
# Create PR to develop → Merge
📢 Tech Stack
Backend: Django, Django REST Framework

Auth: JWT (SimpleJWT)

Database: SQLite (for now), MySQL supported

API Docs: drf-yasg (Swagger)

Testing: Pytest

Version Control: Git + GitHub Flow

📸 Screenshots
✅ Swagger API UI
✅ JWT Token Response
✅ Admin Panel
✅ Directory Structure (modular)

✍️ Author
👤 Gajanan Shivasharan
📧 gajashiv1010@gmail.com
🌍 Pune, India

📌 Next Features (Planned)
✅ Razorpay Payment Gateway Integration

✅ Email Notifications (Django + Celery)

✅ Role-based Access for Admin/Customer

✅ Inventory & Order Management Dashboard

✅ Deployment on AWS / Railway