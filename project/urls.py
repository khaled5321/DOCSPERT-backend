from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
    TokenVerifyView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    # Redirect to docs page
    path("", lambda req: redirect("/api/v1/docs/")),
    # Admin page
    path("admin/", admin.site.urls),
    # Docs
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/v1/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    # JWT
    path("api/v1/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(
        "api/v1/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("api/v1/auth/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(
        "api/v1/auth/token/blacklist/",
        TokenBlacklistView.as_view(),
        name="token_blacklist",
    ),
    # My apps
    path("api/v1/", include("accounts.urls")),
    path("api/v1/", include("books.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
