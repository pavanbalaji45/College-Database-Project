# College-Database-Project

This is a web application designed for managing a college database. The application allows users to perform CRUD operations on students, instructors, and courses. Built with Flask for the backend and PostgreSQL (via pgAdmin) for database management, this project aims to provide a simple, yet comprehensive system for managing college data.

Features
Student Management: Add and view students.
Instructor Management: Add and view instructors.
Course Management: Add and view courses, along with instructors assigned to each course.
Student Enrollment: Enroll students in courses.

Technologies Used
Frontend:

HTML for structuring the web pages.
CSS for styling and layout.
Flask as the web framework to manage requests and serve templates.
Backend:

Flask: Python web framework for handling routing and application logic.
PostgreSQL (via pgAdmin): Relational database to store data for students, instructors, and courses.
psycopg2: Python library to interact with the PostgreSQL database.

/college-database
│
├── /templates              # HTML templates
│   ├── home.html           # Home page
│   ├── about.html          # About page
│   ├── instructors.html    # Instructors management page
│   ├── students.html       # Students management page
│   └── courses.html        # Courses management page
│
├── app.py                  # Flask application
└── requirements.txt        # Python dependencies


Routes
Home: / - Displays the home page.
About: /about - Displays the about page.
Instructors: /instructors - Displays and allows CRUD operations for instructors.
Students: /students - Displays and allows CRUD operations for students.
Courses: /courses - Displays and allows CRUD operations for courses.
Enroll: /enroll - Allows enrolling students in courses.
Screenshots

Future Enhancements
Implement user authentication for different roles (e.g., Admin, Instructor, Student).
Improve the UI with frameworks like Bootstrap or Tailwind CSS.
Add more features like grade management, attendance tracking, etc.
