from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Portfolio
from .serializers import PortfolioSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]

    # Custom action for additional functionality, if needed
    # @action(detail=True, methods=['POST'])
    # def custom_action(self, request, pk=None):
    #     # custom logic here
    #     return Response({'status': 'custom action'})
