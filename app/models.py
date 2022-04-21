from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # 表字段声明
    # 字段名 = models.数据类型(字段约束)
    mobile = models.CharField(max_length=11, unique=True, verbose_name="手机号", help_text='手机号码')

    # 表信息声明
    class Meta:
        # 设置数据库中表名
        db_table = "tb_users"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    # 模型的操作方法
    def __str__(self):
        return self.username
