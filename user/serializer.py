from rest_framework import exceptions
from rest_framework.serializers import ModelSerializer

from user.models import User

class UserModelserializer(ModelSerializer):
    "序列化器"

    class Meta:
        model = User
        # 参与序列化与反序列化
        fields = ("username", "password")

    # 添加DRF校验规则
    extra_kwargs = {
        "username": {
            "required": True,  # 设置必填项
            "min_length": 8, # 最小长度
            "error_messages":{
                "required": "用户名必填",
                "min_length": "你太短了"
            }
        },
        "password": {
            "required": True,  # 设置必填项
            "min_length": 16,  # 最小长度
            "error_messages": {
                "required": "密码必填",
                "min_length": "密码太短了"
            }
        }
    }

    # 是否存在相同
    def validate_username(self, value):
        # request = self.context.get('request')

        username = User.objects.filter(username=value)
        if username:
            raise exceptions.ValidationError("用户名已存在")
        return value