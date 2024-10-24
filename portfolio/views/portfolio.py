from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Portfolio
from ..serializers import PortfolioSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    @action(detail=False, methods=['POST'])
    def create_portfolio(self, request):
        serializer = PortfolioSerializer(data=request.data)
        if serializer.is_valid():
            # You can handle owner in other ways if needed
            # e.g., manually passing an owner or ignoring it
            serializer.save()  # We skip setting an owner since no user is authenticated
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET'])
    def retrieve_portfolio(self, request, pk=None):
        portfolio = self.get_object()
        serializer = PortfolioSerializer(portfolio)
        return Response(serializer.data)

    @action(detail=True, methods=['PUT', 'PATCH'])
    def update_portfolio(self, request, pk=None):
        portfolio = self.get_object()
        serializer = PortfolioSerializer(portfolio, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['DELETE'])
    def delete_portfolio(self, request, pk=None):
        portfolio = self.get_object()
        portfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def list_portfolios(self, request):
        portfolios = Portfolio.objects.all()  # No filtering by user since there's no authentication
        serializer = PortfolioSerializer(portfolios, many=True)
        return Response(serializer.data)
