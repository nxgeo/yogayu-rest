from rest_framework import routers

from yogalevels.views import YogaLevelViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"yoga-levels", YogaLevelViewSet)

urlpatterns = router.urls
