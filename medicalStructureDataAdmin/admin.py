from django.contrib import admin
from .models import User, Record, SchemaConfig, LLM

# 注册User模型
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password')
    search_fields = ('username',)

# 注册SchemaConfig模型
@admin.register(SchemaConfig)
class SchemaConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'name', 'schema', 'create_time')
    list_filter = ('create_time', 'user_id')
    search_fields = ('name',)


# 注册Record模型
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'schema_id','model_id', 'medical_text',  'create_time')
    list_filter = ('create_time', 'user_id')
    search_fields = ('medical_text',)


# 注册LLM模型
@admin.register(LLM)
class LLMAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_name')
    list_filter = ('model_name',)
    search_fields = ('model_name',)

