import re

def validate_password(password):
        password_re = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        password_validation = re.match(password_re, password)
        if password_validation == None:
            return False
        return True