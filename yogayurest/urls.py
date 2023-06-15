from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

v1 = "v1alpha/"

token_patterns = [
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("schema", SpectacularAPIView.as_view(), name="schema"),
    path(v1, include(token_patterns)),
    path(v1, include("yogalevels.urls")),
    path(v1, include("yogaposes.urls")),
    path(v1, include("users.urls")),
    path(v1, include("yogahistories.urls")),
]
