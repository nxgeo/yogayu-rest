from rest_framework.viewsets import ReadOnlyModelViewSet

from yogalevels.models import YogaLevel
from yogalevels.serializers import YogaLevelSerializer


class YogaLevelViewSet(ReadOnlyModelViewSet):
    queryset = YogaLevel.objects.all()
    serializer_class = YogaLevelSerializer
