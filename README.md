# 🛒 MegaMart Pro – E-commerce Backend (Django + DRF)

MegaMart Pro is a real-world e-commerce backend project built using Django and Django REST Framework, following industry-level practices.

---

## 🚀 Features

- Custom User Model with JWT Auth
- Product and Category Models
- Cart & Order System
- Role-Based Access
- Admin Dashboard (upcoming)
- Celery + Redis Support (upcoming)

---

## 📁 Project Structure

mega_mart_finalproj/
│
├── apps/
│ ├── users/
│ ├── products/
│ ├── orders/
│ ├── cart/
│
├── media/
├── static/
├── requirements.txt
├── .env
├── manage.py
├── README.md
└── .gitignore



---

## ⚙️ Setup Instructions

### 1. Clone the Project

```bash
git clone https://github.com/<your-username>/mega_mart_project.git
cd mega_mart_project
2. Create Virtual Environment
bash
Copy
Edit
python -m venv env
source env/bin/activate  # Windows: .\env\Scripts\activate
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Setup Environment File
Create .env file in root:

ini
Copy
Edit
SECRET_KEY=your_secret
DEBUG=True
DATABASE_NAME=yourdbname
DATABASE_USER=root
DATABASE_PASSWORD=yourpass
5. Run Migrations & Server
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
📦 Tech Stack
Django + DRF

MySQL

JWT Authentication

Git & GitHub

Swagger API Docs

Celery + Redis (Planned)

✨ Author
Developed by Gajananshiv
GitHub: @gajananshiv