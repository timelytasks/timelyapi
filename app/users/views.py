from rest_framework import viewsets
from django.contrib.auth.models import User
from app.users.serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
