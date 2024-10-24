from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import Property
from ..serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    @action(detail=False, methods=['POST'])
    def create_property(self, request):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET'])
    def retrieve_property(self, request, pk=None):
        property = self.get_object()
        serializer = PropertySerializer(property)
        return Response(serializer.data)

    @action(detail=True, methods=['PUT', 'PATCH'])
    def update_property(self, request, pk=None):
        property = self.get_object()
        serializer = PropertySerializer(property, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['DELETE'])
    def delete_property(self, request, pk=None):
        property = self.get_object()
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def list_properties(self, request):
        portfolio_id = request.query_params.get('portfolio')
        if portfolio_id:
            properties = Property.objects.filter(portfolio_id=portfolio_id)
        else:
            properties = Property.objects.all()  # Fallback to all properties
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)
