from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Aircraft Production API",
        default_version='v1',
        description="API documentation for the Aircraft Production application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@local.dev"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),

    # Authentication views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # App-specific URLs (includes both frontend and API views)
    path('users/', include('users.urls')),
    path('aircrafts/', include('aircrafts.urls')),
    path('parts/', include('parts.urls')),
    path('teams/', include('teams.urls')),

    # DRF authentication
    path('api-auth/', include('rest_framework.urls')),

    # Swagger documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

