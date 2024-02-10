from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from models import MyModel
from serializers import MyModelSerializer


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer


class MyModelCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
