from django.urls import path, include
from .views import UserAPIView, DemoList
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

# 路由列表
urlpatterns = [
    path(r'docs/', include_docs_urls(title="api接口文档")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'user/latest', UserAPIView.as_view({'get': 'latest'}), name="user"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('demo/', DemoList.as_view(), name="demo"),
]

# 使用drf提供的路由类来自动生成路由
from rest_framework.routers import DefaultRouter

# router 的作用就是自动生成 Api Root 页面
router = DefaultRouter()  # 可以处理视图的路由器
router.register('user', UserAPIView, basename="user")  # 向路由器中注册视图集,"user":浏览器访问的路径，basename:路由别名
# router.register('DemoAPIView', DemoAPIView, basename="demo")
urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中

