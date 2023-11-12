from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from apps.users.views import UserViewSet

from apps.users.views import UserViewSet

router = DefaultRouter()
router.register('', UserViewSet, "api_users")

urlpatterns=[
    path('api/login/', TokenObtainPairView.as_view(), name="api_login"),
    path('api/refresh/', TokenRefreshView.as_view(), name="api_refresh")
]

urlpatterns += router.urls