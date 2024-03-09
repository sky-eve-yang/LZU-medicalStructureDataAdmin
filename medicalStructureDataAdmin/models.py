from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager




class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.CharField(max_length=255, primary_key=True, verbose_name="ID")
    username = models.CharField(max_length=255, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=255, verbose_name="密码")
    
    objects = UserManager()
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.id

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name_plural = verbose_name = "用户信息"

class SchemaConfig(models.Model):
    id = models.CharField(max_length=255, primary_key=True, verbose_name="ID")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户ID")
    schema = models.TextField(verbose_name="Schema")
    name = models.CharField(max_length=255, verbose_name="名称")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name_plural = verbose_name = "Schema 配置表"


LARGE_MODEL_CHOICES = (
    (1, 'ChatGPT4'),
    (2, '文心一言4'),
    (3, 'MindSpore'),
    (3, '华驼'),
)

class LLM(models.Model):
    id = models.CharField(max_length=255, primary_key=True, verbose_name="ID")
    model_name = models.IntegerField(choices=LARGE_MODEL_CHOICES, default=1, verbose_name="模型名称")

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name_plural = verbose_name = "模型表"


class Record(models.Model):
    id = models.CharField(max_length=255, primary_key=True, verbose_name="ID")
    medical_text = models.TextField(verbose_name="医疗文本")
    schema_id = models.ForeignKey(SchemaConfig, on_delete=models.CASCADE, verbose_name="Schema ID")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户ID")
    model_id = models.ForeignKey(LLM, on_delete=models.CASCADE, verbose_name="模型ID")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name_plural = verbose_name = "转换记录信息"
        



