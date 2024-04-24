# from .models import Project
# from .serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class NoneAPI(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    # 定义 GET 请求的方法，内部实现相同 @api_view
    def get(self, request):
        ############################################
        # 业务逻辑
        ############################################
        return Response(data={"message": ["what are you want?"], "code": "200"}, status=status.HTTP_200_OK)

    # 定义 POST 请求的方法
    def post(self, request):
        ############################################
        # 业务逻辑
        ############################################
        return Response(data=["en?"])
