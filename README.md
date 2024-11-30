# Gas Utility Service - Django Application

This is a Django-based web application designed to streamline the customer service process for a gas utility company. The application allows customers to submit and track service requests, while providing support personnel with tools to manage and resolve these requests.

## Live Application

You can access the live version of the project at:

- **Customer Login**: [http://108.61.209.123:9000/](http://108.61.209.123:9000/)
- **Support Login**: [http://108.61.209.123:9000/admin](http://108.61.209.123:9000/admin)

### Login Credentials:

- **Customer**:
  - Username: `darshan`
  - Password: `Pass@123`
- **Support Personnel**:
  - Username: `admin`
  - Password: `Pass@123`

---

## Project Folder Structure

```
GAS_UTILITY_SERVICE
│   .gitignore
│    db.sqlite3
│    manage.py
│    requirements.txt
│
├────customer_service
│ │     admin.py
│ │     apps.py
│ │     forms.py
│ │     models.py
│ │     tests.py
│ │     urls.py
│ │     views.py
│ │     __init__.py
│ │
│ ├─────migrations
│ │         0001_initial.py
│ │         __init__.py
│ │
│ └─────templates
│       └───customer_service
│               base.html
│               dashboard.html
│               login.html
│               request_detail.html
│               submit_request.html
│               user_profile.html
│
├────gas_utility_service
│       asgi.py
│       settings.py
│       urls.py
│       wsgi.py
│       __init__.py
│
└────media
    └───service_requests
            Screenshot_112.png
```

## Features

### Customer Side:

- **Submit Service Requests:** Customers can submit service requests by selecting the type of service, adding a description, and attaching files.
- **Track Request Status:** Customers can view the status of their requests and track when they were submitted and resolved.
- **View Account Information:** Customers can view their account details, including username, account number.

### Support Side:

- **Manage Requests:** Provides support personnel with access to the Django admin panel, where they can view, update, and resolve customer requests.

## Setup Instructions

To set up this project locally, follow these steps:

### 1. Clone the Repository

```sh
git clone https://github.com/darshandevelopes/gas-utility-service
cd gas-utility-service
```

### 2. Create a Virtual Environment

```sh
python -m venv venv
```

Activate the virtual environment:

- For Windows
  ```sh
  venv\Scripts\activate
  ```
- For Mac/Linux:
  ```sh
  source venv/bin/activate
  ```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Run Migrations

```sh
python manage.py migrate
```

### 5. Run the Development Server

```sh
python manage.py runserver 9000
```

Visit http://127.0.0.1:9000 in your browser to access the application.
