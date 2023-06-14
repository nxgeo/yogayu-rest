from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from users.models import User
from users.serializers import (
    UserCreateSerializer,
    UserPasswordChangeSerializer,
    UserSerializer,
)


class UserRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserPasswordChangeView(APIView):
    def post(self, request):
        serializer = UserPasswordChangeSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=HTTP_204_NO_CONTENT)


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


class UserLeaderboardListView(ListAPIView):
    serializer_class = UserSerializer

    _DEFAULT_LIMIT = 10

    def get_queryset(self):
        limit = self.request.query_params.get("limit") or self._DEFAULT_LIMIT
        yoga_users = User.objects.exclude(yoga_user=None)
        return yoga_users.order_by("-yoga_user__total_points")[: int(limit)]
