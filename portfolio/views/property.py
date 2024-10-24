from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Property
from ..serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    # Action to return the count of properties for a specific portfolio
    @action(detail=True, methods=['GET'])
    def property_count(self, request, pk=None):
        portfolio_id = pk
        property_count = Property.objects.filter(portfolio_id=portfolio_id).count()
        return Response({'property_count': property_count})

    @action(detail=False, methods=['POST'])
    def create_property(self, request):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET'])
    def retrieve_property(self, request, pk=None):
        property_instance = self.get_object()
        serializer = PropertySerializer(property_instance)
        return Response(serializer.data)

    @action(detail=True, methods=['PUT', 'PATCH'])
    def update_property(self, request, pk=None):
        property_instance = self.get_object()
        serializer = PropertySerializer(property_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['DELETE'])
    def delete_property(self, request, pk=None):
        property_instance = self.get_object()
        property_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def list_properties(self, request):
        portfolio_id = request.query_params.get('portfolio')
        if portfolio_id:
            properties = Property.objects.filter(portfolio_id=portfolio_id)
        else:
            properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)
