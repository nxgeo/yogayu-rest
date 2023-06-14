from rest_framework.generics import ListCreateAPIView

from yogahistories.models import YogaHistory
from yogahistories.serializers import YogaHistorySerializer


class YogaHistoryListCreateView(ListCreateAPIView):
    queryset = YogaHistory.objects.select_related("user", "yoga_pose").all()
    serializer_class = YogaHistorySerializer
