from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Function to connect to the PostgreSQL database
def get_db_connection():
    conn = psycopg2.connect(
        dbname="college",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    return conn

# Home Route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


# CRUD Routes for Instructors
@app.route('/instructors', methods=['GET', 'POST'])


def manage_instructors():
    if request.method == 'POST':
        name = request.form['name']
        department = request.form['department']
        email = request.form['email']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO instructors (name, department, email) VALUES (%s, %s, %s)',
                    (name, department, email))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('manage_instructors'))

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM instructors')
    instructors = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('instructors.html', instructors=instructors)

# CRUD Routes for Students
@app.route('/students', methods=['GET', 'POST'])
def manage_students():
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cur.execute('INSERT INTO students (name, email) VALUES (%s, %s)', (name, email))
        conn.commit()

    # Fetch students and courses to populate the forms
    cur.execute('SELECT * FROM students')
    students = cur.fetchall()

    cur.execute('SELECT * FROM courses')
    courses = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('students.html', students=students, courses=courses)

# CRUD Routes for Courses
@app.route('/courses', methods=['GET', 'POST'])
def manage_courses():
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        course_name = request.form['course_name']
        instructor_id = request.form['instructor_id']
        cur.execute('INSERT INTO courses (course_name, instructor_id) VALUES (%s, %s)',
                    (course_name, instructor_id))
        conn.commit()

    # Fetch courses and instructors
    cur.execute('SELECT * FROM courses')
    courses = cur.fetchall()

    cur.execute('SELECT * FROM instructors')
    instructors = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('courses.html', courses=courses, instructors=instructors)

# Enroll Students in Courses
@app.route('/enroll', methods=['POST'])
def enroll_student():
    student_id = request.form['student_id']
    course_id = request.form['course_id']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO student_courses (student_id, course_id) VALUES (%s, %s)',
                (student_id, course_id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('manage_students'))

# Start the Flask Application
if __name__ == '__main__':
    app.run(debug=True)
