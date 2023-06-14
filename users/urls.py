from django.urls import path

from users.views import (
    UserCreateView,
    UserLeaderboardListView,
    UserPasswordChangeView,
    UserRetrieveUpdateView,
)

urlpatterns = [
    path("user", UserRetrieveUpdateView.as_view()),
    path("user/password", UserPasswordChangeView.as_view()),
    path("users", UserCreateView.as_view()),
    path("users/leaderboard", UserLeaderboardListView.as_view()),
]
