"""epic_events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api.views import (
    ClientViewSet, 
    ContractViewSet, 
    EventViewSet,
)
from core.views import EmployeeViewSet

router = SimpleRouter()
router.register(r'clients', ClientViewSet, basename="clients")

clients_router = routers.NestedSimpleRouter(router, r'clients', lookup='client')
clients_router.register(r'contracts', ContractViewSet, basename="contracts")

contracts_router = routers.NestedSimpleRouter(clients_router, r'contracts', lookup='contract')
contracts_router.register(r'events', EventViewSet, basename="events")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/', include(clients_router.urls)),
    path('api/', include(contracts_router.urls)),
    path('signup/', EmployeeViewSet.as_view({'post': 'create'}), name='signup'),
]
