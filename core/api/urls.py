from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *
urlpatterns = [
    path('SignIn', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("Document", include("document.urls")),
    
    path('employee/', EmployeeView.as_view()),
    path('events/', EventView.as_view()),
    path('news/', NewsView.as_view()),
    
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]