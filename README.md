# Flask Blog Project

This Flask project implements a simple blog created by Emin Amirov and Ruslan Hamidov. It utilizes Flask for the backend, SQLite for the database, Jinja for templating, and HTML/CSS for the frontend.

## Contributors
- Emin Amirov (Python code & Frontend)
- Ruslan Hamidov (Database)

## Features
- User authentication (register, login, logout)
- Create, read, update, and delete blog posts
- View posts by category or author
- Responsive design for various devices

## Technologies Used
- Flask
- SQLite
- Jinja
- HTML
- CSS

## Installation
1. Clone the repository:
- git clone https://github.com/RuslanHamidov/flask_project.git
2. Install dependencies:
- pip install -r requirements.txt
3. Run the application:
- flask run

## Usage
- Visit the homepage to browse existing blog posts or register/login to create your own.
- Once logged in, you can create new posts, edit existing ones, or delete them.
- Posts can be filtered by category or author.

## Folder Structure

```rb
flask_project/
│
├── app.py                    # Main Flask application file
├── database_work/            # Folder for database-related files
│   ├── database.db           # SQLite database file
│   └── schema.sql            # Database schema file
├── scripts/                  # Folder for Python scripts
│   ├── __pycache__/          # Cached Python files (generated automatically)
│   ├── models.py             # Python script containing database models
│   └── site_login.py         # Python script for site login functionality
├── static/                   # Folder for static files
│   ├── css/                  # Folder for CSS styles
│       └── styles.css        # CSS styles file
│   
├── templates/                # Folder for HTML templates
│   ├── login.html            # HTML template for login page
│   └── userpage.html         # HTML template for user page
├── .gitignore                # Git ignore file
├── README.md                 # Readme file for the project
```

## Contributing
1. Fork the repository.
2. Create your feature branch (git checkout -b feature/your-feature).
3. Commit your changes (git commit -am 'Add some feature').
4. Push to the branch (git push origin feature/your-feature).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
