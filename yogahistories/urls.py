from django.urls import path

from yogahistories.views import YogaHistoryListCreateView

urlpatterns = [
    path("user/yoga-histories", YogaHistoryListCreateView.as_view()),
]
