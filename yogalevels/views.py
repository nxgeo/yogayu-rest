from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from yogalevels.models import YogaLevel
from yogalevels.serializers import YogaLevelSerializer
from yogaposes.serializers import YogaPoseSerializer


class YogaLevelViewSet(ReadOnlyModelViewSet):
    queryset = YogaLevel.objects.all()
    serializer_class = YogaLevelSerializer

    @action(detail=True, url_path="yoga-poses")
    def list_yoga_poses(self, request, pk):
        yoga_level = self.get_object()
        yoga_level_poses = yoga_level.yogapose_set.all()
        serializer = YogaPoseSerializer(yoga_level_poses, many=True)
        return Response(serializer.data)
