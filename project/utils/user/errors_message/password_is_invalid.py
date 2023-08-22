

def invalid_password_message():
  return {
    'password': [
      'The password must have at least 8 characters',
      'The password must have at least one uppercase letter',
      'The password must have at least one lowercase letter',
      'The password must have at least one digit',
      'The password must have at least one special character'
    ]
  }
