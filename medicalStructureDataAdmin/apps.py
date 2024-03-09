# medicalStructureDataAdmin/apps.py

from django.apps import AppConfig

class MedicalStructureDataAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'medicalStructureDataAdmin'
    verbose_name = '结构化数据'
