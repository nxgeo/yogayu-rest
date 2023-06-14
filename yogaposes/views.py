from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet

from yogaposes.models import YogaPose
from yogaposes.serializers import YogaPoseSerializer


class YogaPoseViewSet(ReadOnlyModelViewSet):
    queryset = YogaPose.objects.select_related("yoga_level").all()
    serializer_class = YogaPoseSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name"]
