# WADP-L4 Demonstration-2 [Task-Management]
# Task Management System

A simple and user-friendly **Task Management Web Application** built with **Python and Django**. This project allows users to create, manage, track, and update their tasks with deadlines and different task statuses.

## 🚀 Features

* 👤 User Registration & Login
* 🔐 User Authentication
* 📝 Create Tasks
* 📋 View Tasks
* ✏️ Update Tasks
* 🗑️ Delete Tasks
* 📌 Task Status Management
* 📅 Task Deadline
* 👤 Tasks linked to the respective user
* 📄 Task title and description
* 📊 Track task progress

## 📌 Task Status

The application provides three different task statuses:

* **Not Started** – Task has not been started yet.
* **In Progress** – Task is currently being worked on.
* **Completed** – Task has been successfully completed.

## 🛠️ Technologies Used

* **Python**
* **Django**
* **HTML**
* **CSS**
* **SQLite**
* **Django ORM**
* **Git & GitHub**

## 📂 Project Structure

```text
Task-Management/
│
├── manage.py
├── requirements.txt
│
├── TaskHub/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── task/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── task/
│
└── static/
    ├── css/
    └── images/
```

## 🗃️ Main Models

### UserModel

The custom user model is based on Django's `AbstractUser`.

```python
class UserModel(AbstractUser):
    full_name = models.CharField(max_length=200, null=True)
```

It stores:

* Username
* Email
* Password
* Full Name
* Other Django user information

### TaskModel

The `TaskModel` stores information about each task.

```text
Title
Description
Status
Deadline
Created By
```

Each task is associated with the user who created it.

## 📊 Task Workflow

```text
Create Task
     ↓
Not Started
     ↓
In Progress
     ↓
Completed
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### 2. Go to the project directory

```bash
cd your-repository
```

### 3. Create a virtual environment

```bash
python -m venv env
```

### 4. Activate the virtual environment

**Windows:**

```bash
env\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 🔑 Authentication

Users can:

1. Create an account
2. Login to the application
3. Create their own tasks
4. Manage existing tasks
5. Track task progress
6. Logout securely

## 🎯 Future Improvements

* 🔍 Task search
* 🔎 Task filtering by status
* 📊 Dashboard statistics
* 🔔 Deadline notifications
* 📱 Responsive design
* 🌙 Dark mode
* 📧 Email notifications
* 📅 Calendar-based task management

## 👨‍💻 Author

**Oren Michael Dessai**

Python & Django Backend Developer

> Building web applications with Django and continuously learning new technologies.

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
