from project.infra.token import decode_token

def is_authenticated(request):
        authorization = request.META.get('HTTP_AUTHORIZATION')
        if authorization == None:
          return False
        token = str(authorization).split(' ')
        if not decode_token(token[1]):
            return False
        return True