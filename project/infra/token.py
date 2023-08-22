import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
import datetime

from credentials import MY_SECRET_KEY

def generate_token(payload):
    my_secret = MY_SECRET_KEY
    token = jwt.encode(
      payload= {
        'payload': payload,
        'exp': (datetime.datetime.now() + datetime.timedelta(hours=8))
        },
      key=my_secret,
      
    )
    return token
  
def decode_token(token):
    try:
        jwt.decode(token, key=MY_SECRET_KEY, algorithms=['HS256',])
    except InvalidSignatureError:
        return False
    try:
        header_data = jwt.get_unverified_header(token)
        payload = jwt.decode(
          token,
          key=MY_SECRET_KEY,
          algorithms=[header_data['alg'], ]
          )
    except ExpiredSignatureError:
        return False
    return payload