from django.shortcuts import render
from rest_framework.viewsets import ViewSet, GenericViewSet
from utils.response import APIResponse
from user.models import User
from user.serializer import UserModelserializer
from rest_framework.response import Response

# Create your views here.

class UserAPIView(ViewSet):

    # 用户登陆请求
    def user_login(self, request, *args, **kwargs):
        request_data = request.data
        serializer = UserModelserializer(data=request_data)
        # serializer.is_valid(raise_exception=True)
        user_obj = User.objects.filter(username=request_data['username'], password=request_data['password'])
        if user_obj:
            return APIResponse(200, "登陆成功", results=request_data)
        else:
            return APIResponse(201, "登陆失败")

    def user_register(self, request, *args, **kwargs):
        request_data = request.data
        # 将前端传递的参数交给反序列化器进行校验
        serializer = UserModelserializer(data=request_data)

        # 校验数据是否合法 raise_exception: 一旦校验失败，立即抛出异常
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()
        if user_obj:
            return APIResponse(400, "注册成功", results=request_data)
        else:
            return APIResponse(401, "注册失败", results=request_data)

        # class BookGenericAPIView(ListModelMixin,
        #                          RetrieveModelMixin,
        #                          CreateModelMixin,
        #                          DestroyModelMixin,
        #                          UpdateModelMixin,
        #                          GenericAPIView):
        #     # 获取当前视图类要操作的模型
        #     queryset = Book.objects.all()
        #     # 指定当前视图要使用的序列化器类
        #     serializer_class = BookModelSerializer
        #     # 指定获取单个对象的主键的名称
        #     lookup_field = "id"
        #
        #     # 混合视图 查询所有
        #     def get(self, request, *args, **kwargs):
        #         if "id" in kwargs:
        #             # 查询单个
        #             return self.retrieve(request, *args, **kwargs)
        #         return self.list(request, *args, **kwargs)
        #
        #     def post(self, request, *args, **kwargs):
        #         return self.create(request, *args, **kwargs)
        #
        #     def delete(self, request, *args, **kwargs):
        #         return self.destroy(request, *args, **kwargs)
        #
        #     # 整体修改
        #     def put(self, request, *args, **kwargs):
        #         return self.update(request, *args, **kwargs)
        #
        #     # 局部修改
        #     def patch(self, request, *args, **kwargs):
        #         response = self.partial_update(request, *args, **kwargs)
        #         return APIResponse(results=response.data)
