from flask import Flask, render_template, session, flash, redirect, url_for
from database import init_db, mongo  # ✅ Import from `database.py`
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.secret_key = "your_secret_key"  # ✅ Required for session management
    app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"  # ✅ Update with correct DB name

    # ✅ Initialize database
    init_db(app)
    bcrypt.init_app(app)

    # ✅ Import and register blueprints
    from routes.auth import auth_bp  
    from routes.contact import contact_bp  # ✅ Import contact blueprint

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(contact_bp, url_prefix='/contact')  # ✅ Register contact blueprint

    # ✅ Home Route
    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html')

    # ✅ Dashboard Route
    @app.route('/dashboard')
    def dashboard():
        if 'user' not in session:
            flash('You need to log in first', 'warning')
            return redirect(url_for('auth.login'))
        return render_template('dashboard.html', username=session['user'])

    return app

# ✅ Run Flask App
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
