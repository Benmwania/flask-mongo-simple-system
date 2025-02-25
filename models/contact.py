from database import mongo

class Contact:
    @staticmethod
    def add_contact(mobile, email, address, reg_number):
        contact = {
            'mobile': mobile,
            'email': email,
            'address': address,
            'reg_number': reg_number
        }
        mongo.db.contacts.insert_one(contact)
    
    @staticmethod
    def find_by_reg_number(reg_number):
        return mongo.db.contacts.find_one({'reg_number': reg_number})

