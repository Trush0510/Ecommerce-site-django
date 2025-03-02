## Features

- **User Authentication:** Secure login and registration.
- **Product Listing:** Display all available products with images and pricing.
- **Shopping Cart:** Add, remove, and adjust quantities of products in the cart.
- **Checkout Process:** Seamless checkout experience.
- **Session-Based Cart Management:** Products remain in the cart until the session ends.
- **Admin Panel:** Manage products and orders.
- **Responsive Design:** Mobile-friendly UI using Bootstrap.

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (can be switched to PostgreSQL or MySQL)
- **Authentication:** Django’s built-in authentication system
- **Session Storage:** Django Sessions for cart management

## Installation Guide

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package manager)
- Virtualenv (recommended for dependency management)

### Step 1: Clone the Repository
```bash
$ git clone https://github.com/your-username/ecommerce-store.git
$ cd ecommerce-store
```

### Step 2: Set Up Virtual Environment
```bash
$ python -m venv venv
$ source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
$ pip install -r requirements.txt
```

### Step 4: Apply Migrations & Setup Database
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### Step 5: Create Superuser (For Admin Access)
```bash
$ python manage.py createsuperuser
```
Follow the instructions to create an admin user.

### Step 6: Run the Development Server
```bash
$ python manage.py runserver
```
Access the website at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Project Structure
```
/ ecommerce-store
│── ecommerce/            # Main Django project folder
│   ├── settings.py       # Django settings
│   ├── urls.py           # URL configurations
│   ├── wsgi.py           # WSGI application
│
│── store/                # E-commerce app
│   ├── models.py         # Database models
│   ├── views.py          # Business logic
│   ├── urls.py           # Store-specific URLs
│   ├── templates/        # HTML templates
│   ├── static/           # Static files (CSS, JS, images)
│
│── media/                # Product images (if uploaded)
│── db.sqlite3            # SQLite database (default)
│── manage.py             # Django CLI management tool
│── requirements.txt      # Project dependencies
│── README.md             # This file
```

## How to Change Product Prices
1. **Using Django Admin Panel:**
   - Navigate to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
   - Log in using the superuser credentials.
   - Edit the product prices.

2. **Updating Directly in the Database:**
   - Open `models.py` in the `store` app.
   - Modify the `price` field in the `Product` model.
   - Run migrations using `python manage.py makemigrations && python manage.py migrate`.

## Future Enhancements
- Implement payment gateway integration (Stripe, PayPal, etc.).
- Add product categories and search functionality.
- User order history and tracking.
- REST API for mobile integration.
