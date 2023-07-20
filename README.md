# Human Resources Management System (HRMS)

HRMS is a web-based application provides a basic, beautiful, and modern solution for managing various aspects of human resources within an organization. With a user-friendly interface and robust functionalities, HRMS simplifies HR-related tasks and enhances efficiency.

## Technologies Used

- Python: A powerful programming language used for the backend development of HRMS.
- Flask Framework: A lightweight and flexible web framework for building web applications in Python.
- Flask SQLAlchemy: An extension for Flask that provides an easy-to-use interface for interacting with SQL databases.
- Bootstrap: A popular CSS framework for creating responsive and appealing frontend designs.
- SQLite3: A lightweight, serverless database engine used for storing HRMS data.

## Project Structure

The repository has the following structure:

```
.
├── CHANGELOG.md
├── configure-python3.10.txt
├── images
├── instance
│   ├── db.sqlite3
│   └── insert.sql
├── LICENSE
├── main.py
├── __pycache__
│   └── main.cpython-310.pyc
├── README.md
├── requirements.txt
├── src
│   ├── admin
│   │   ├── __init__.py
│   │   ├── modules.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── modules.cpython-310.pyc
│   │   │   └── routes.cpython-310.pyc
│   │   └── routes.py
│   ├── app.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── modules.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── modules.cpython-310.pyc
│   │   │   └── routes.cpython-310.pyc
│   │   └── routes.py
│   ├── config.py
│   ├── home
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   └── routes.cpython-310.pyc
│   │   └── routes.py
│   ├── models.py
│   ├── __pycache__
│   │   ├── app.cpython-310.pyc
│   │   ├── app.cpython-311.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── modules.cpython-310.pyc
│   │   └── routes.cpython-310.pyc
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       ├── datatables-simple-demo.js
│   │       └── scripts.js
│   ├── templates
│   │   ├── admin
│   │   │   ├── gere_avance.html
│   │   │   ├── gere_conge.html
│   │   │   ├── liste_dep.html
│   │   │   ├── liste_employees.html
│   │   │   └── profile.html
│   │   ├── auth
│   │   │   ├── login.html
│   │   │   ├── password.html
│   │   │   └── register.html
│   │   ├── base.html
│   │   ├── home
│   │   │   ├── 401.html
│   │   │   ├── 404.html
│   │   │   ├── 500.html
│   │   │   └── home.html
│   │   └── user
│   │       ├── demande_avance.html
│   │       ├── demande_conge.html
│   │       └── suivie.html
│   └── user
│       ├── __init__.py
│       ├── modules.py
│       ├── __pycache__
│       │   ├── __init__.cpython-310.pyc
│       │   ├── modules.cpython-310.pyc
│       │   └── routes.cpython-310.pyc
│       └── routes.py
└── TODO.md

21 directories, 59 files

```

## Getting Started

To get started with HRMS on your local machine, follow these steps:

1. Clone the repository: `git clone https://github.com/Oussama1403/HRMS`
2. Navigate to the project directory: `cd hrms`
3. Install the project dependencies: `pip install -r requirements.txt`
4. Run the application: `python main.py`
5. Access HRMS in your browser at `ttp://127.0.0.1:5000/`

## How to Contribute

We welcome contributions to HRMS from the community. If you would like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name: `git checkout -b feature/my-new-feature`
3. Make changes and add your enhancements.
4. Commit your changes: `git commit -am 'Add new feature'`
5. Push the branch to your forked repository: `git push origin feature/my-new-feature`
6. Submit a pull request to the main repository.
7. Provide a detailed description of your changes and why they should be merged.

## Developer

HRMS is developed and maintained by [Osama Ben Sassi](https://www.linkedin.com/in/osama-ben-sassi/).

Feel free to contact me with any questions or feedback regarding HRMS.

## License

HRMS is released under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the license terms.

Thank you for your interest in HRMS! I appreciate your contribution and hope you find the project useful.
