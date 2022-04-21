from .models import User
from .serializers import UserModelSerializer

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet  # drf类视图需导入
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.filters import OrderingFilter
# from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status


# Create your views here.
# django视图有两种：FBV函数视图 和 CBV类视图
# drf中，我们经常使用的是类视图
class UserAPIView(ModelViewSet):
    """
    这里提供了5个api接口，

    create:添加一条数据

    delete:删除项目
    retrieve:获取一条数据
    list:获取所有数据
    update:更新项目
    interfaces:获取指定项目的所有接口信息
    latest: 返回最新的一条数据

    """
    queryset = User.objects.all().order_by("id")  # 要操作的数据
    serializer_class = UserModelSerializer  # 序列化器

    # 限流设置
    throttle_classes = (AnonRateThrottle,)

    # 使用过滤器, 指定哪个可过滤
    filter_fields = ['username', 'mobile']

    # 指定后端排序
    filter_backends = [OrderingFilter, ]
    # 排序设置
    ordering_fields = ['id', 'username']

    # 权限设置
    # IsAuthenticated: 只有登录才能访问
    # IsAuthenticatedOrReadOnly: 认证用户可读可写，未认证用户可读
    permission_classes = [IsAuthenticated, ]

    @action(['get', ], detail=False)
    def lasted(self, request):
        """
        返回最新的一条数据
        :param request:
        :return:
        """
        user = User.objects.latest('id')
        serializer = self.get_serializer(user)

        return Response(serializer.data)


class DemoList(APIView):
    """
    get: 测试接口
    """
    def get(self, request):
        """返回测试数据"""
        data = {"code": 200, "msg": "测试数据"}
        """
        data： 响应的序列化数据。
        status： 响应的状态代码。默认为200。
        template_name： 选择 HTMLRenderer 时使用的模板名称。
        headers： 设置 HTTP header，字典类型。
        content_type： 响应的内容类型，通常渲染器会根据内容协商的结果自动设置，但有些时候需要手动指定。
        Response 可以将内置类型转换成字符串。写到data的位置
        """
        return Response(data, status=status.HTTP_200_OK)