from .models import Rubbish, Category
from rest_framework import permissions, status
from rest_framework.response import Response
from .serializers import RubbishSerializer, RubbishCategorySerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
# Create your views here.

# 所有分类获取处理 继承listAPIView
class RubbishCategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = RubbishCategorySerializer

# 单个分类获取处理 继承RetrieveAPIView 表示只可以get
class RubbishCategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = RubbishCategorySerializer

    def get(self, request, pk):
        try:
            category = Category.objects.get(name=pk)
            serializer = RubbishCategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# 所有垃圾获取处理 继承listAPIView
class RubbishView(ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    # 进行jwt验证
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Rubbish.objects.all()
    serializer_class = RubbishSerializer


# 单个垃圾获取处理 继承RetrieveAPIView 表示只可以get
class RubbishDetailView(RetrieveAPIView):
    queryset = Rubbish.objects.all()
    serializer_class = RubbishSerializer

    def get(self, request, pk):
        try:
            rubbish = Rubbish.objects.get(name=pk)
            serializer = RubbishSerializer(rubbish)
            return Response(serializer.data)
        except Rubbish.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
