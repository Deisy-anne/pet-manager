from apps.user.api.serializers.user import UserSerializer
from apps.user.models import User

class UserAuthenticationSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')