from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from . import serializers
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class HelloAuthView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message":"hello Auth"}, 
                        status=status.HTTP_200_OK)
        
HELLO_AUTH_VIEW = HelloAuthView.as_view()

class UserCreateView(generics.GenericAPIView):
    serializer_class=serializers.UserCreationSerializer
    @swagger_auto_schema(operation_summary="通过注册创建用户帐户 (Create a user account by signing Up)")
    def post(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,
                status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
USER_CREATE_VIEW = UserCreateView.as_view()