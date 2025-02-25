from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.contact import Contact

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        return redirect(url_for('contact.add_contact'))  # ✅ Redirects to add_contact

    return render_template('dashboard.html')

@contact_bp.route('/add_contact', methods=['POST'])
def add_contact():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    mobile = request.form['mobile']
    email = request.form['email']
    address = request.form['address']
    reg_number = request.form['reg_number']

    Contact.add_contact(mobile, email, address, reg_number)
    flash('Contact added successfully!', 'success')
    
    return redirect(url_for('contact.dashboard'))  # ✅ Redirect to dashboard

@contact_bp.route('/search', methods=['GET'])
def search():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    reg_number = request.args.get('reg_number')
    contact = Contact.find_by_reg_number(reg_number)
    
    return render_template('search.html', contact=contact)
