from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Portfolio
from ..serializers import PortfolioSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]
