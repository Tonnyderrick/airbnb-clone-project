from flask import Flask, render_template, redirect, url_for, request, session, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DATABASE = 'myscholar.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()

        if user and user['password'] == password:
            session['user_id'] = user['id']
            session['user_name'] = user['full_name']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']

        try:
            conn = get_db_connection()
            conn.execute('INSERT INTO users (full_name, email, password) VALUES (?, ?, ?)',
                         (full_name, email, password))
            conn.commit()
            conn.close()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Email already exists. Try logging in.', 'warning')
            return redirect(url_for('signup'))

    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('login'))

    user_name = session.get('user_name')
    conn = get_db_connection()
    application = conn.execute('SELECT * FROM bursary_applications WHERE user_id = ?', 
                               (session['user_id'],)).fetchone()
    conn.close()

    return render_template('dashboard.html', user_name=user_name, application=application)

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        institution = request.form['institution']
        course = request.form['course']
        year_of_study = request.form['year']
        reason = request.form['reason']

        conn = get_db_connection()
        conn.execute('''
            INSERT INTO bursary_applications 
            (user_id, institution, course, year, reason, status)
            VALUES (?, ?, ?, ?, ?, ?)''',
            (session['user_id'], institution, course, year_of_study, reason, 'Pending'))
        conn.commit()
        conn.close()
        flash('Bursary application submitted!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('apply.html')

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],)).fetchone()
    conn.close()
    return render_template('profile.html', user=user)

@app.route('/notifications')
def notifications():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('notifications.html')

@app.route('/support')
def support():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('support.html')

# ----------------- ADMIN ROUTES ----------------- #

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        admin = conn.execute('SELECT * FROM admins WHERE username = ? AND password = ?', 
                             (username, password)).fetchone()
        conn.close()
        if admin:
            session['admin_id'] = admin['id']
            session['admin_username'] = admin['username']
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid admin credentials', 'danger')
    return render_template('admin_login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))
    return render_template('admin_dashboard.html', admin_username=session.get('admin_username'))

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_id', None)
    session.pop('admin_username', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('admin_login'))

# ----------------- INITIALIZE DATABASE ----------------- #

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        with sqlite3.connect(DATABASE) as conn:
            # Users table
            conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            ''')

            # Bursary applications table
            conn.execute('''
                CREATE TABLE IF NOT EXISTS bursary_applications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    institution TEXT,
                    course TEXT,
                    year TEXT,
                    reason TEXT,
                    status TEXT,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            ''')

            # Admins table
            conn.execute('''
                CREATE TABLE IF NOT EXISTS admins (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            ''')

            # Insert default admin if not exists
            conn.execute('INSERT OR IGNORE INTO admins (id, username, password) VALUES (1, "admin", "admin123")')
            conn.commit()

    app.run(debug=True)
