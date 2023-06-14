from rest_framework import routers

from yogaposes.views import YogaPoseViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"yoga-poses", YogaPoseViewSet)

urlpatterns = router.urls
