from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

auth_bp = Blueprint('auth', __name__)

# ✅ Register Route
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if User.find_by_email(email) or User.find_by_username(username):
            flash('Username or Email already exists!', 'danger')
            return redirect(url_for('auth.register'))

        User.create_user(username, email, password)
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

# ✅ Login Route (Redirects to Dashboard after login)
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.find_by_username(username)

        if user and bcrypt.check_password_hash(user['password'], password):  # ✅ Fixed Password Checking
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  # ✅ Redirects to Dashboard

        flash('Invalid credentials', 'danger')

    return render_template('login.html')

# ✅ Forgot Password Route
@auth_bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.find_by_email(email)

        if user:
            flash('A password reset link has been sent to your email.', 'info')
        else:
            flash('No account found with that email.', 'danger')

        return redirect(url_for('auth.login'))

    return render_template('forgot_password.html')


# 🚪 Logout Route
@auth_bp.route('/logout')
def logout():
    """Logs out the user by removing session data."""
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
