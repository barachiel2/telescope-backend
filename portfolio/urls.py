from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.portfolio import PortfolioViewSet
from .views.property import PropertyViewSet

router = DefaultRouter()
router.register(r'portfolios', PortfolioViewSet)
router.register(r'properties', PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
