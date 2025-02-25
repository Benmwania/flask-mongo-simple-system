from flask_bcrypt import Bcrypt
from database import mongo  # ✅ Ensure it's imported correctly

bcrypt = Bcrypt()

class User:
    @staticmethod
    def create_user(username, email, password):
        """Creates a new user with a hashed password and ensures uniqueness."""
        if User.find_by_email(email) or User.find_by_username(username):
            return None  # Avoid duplicate users
        
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        user = {'username': username, 'email': email, 'password': hashed_pw}
        mongo.db.users.insert_one(user)  # ✅ Corrected `mongo.db.users`
        return user  # Return user for reference if needed

    @staticmethod
    def find_by_username(username):
        """Finds a user by username."""
        return mongo.db.users.find_one({'username': username})  # ✅ Use `mongo.db`

    @staticmethod
    def find_by_email(email):
        """Finds a user by email."""
        return mongo.db.users.find_one({'email': email})  # ✅ Use `mongo.db`

    @staticmethod
    def verify_password(hashed_password, password):
        """Verifies a given password against the stored hash."""
        return bcrypt.check_password_hash(hashed_password, password)

    @staticmethod
    def update_password(email, new_password):
        """Updates the password for a user with the given email."""
        user = User.find_by_email(email)
        if user:
            hashed_pw = bcrypt.generate_password_hash(new_password).decode('utf-8')
            mongo.db.users.update_one({'email': email}, {'$set': {'password': hashed_pw}})
            return True  # Indicate success
        return False  # Indicate failure if email not found
