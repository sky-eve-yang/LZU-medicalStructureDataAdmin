# Generated by Django 4.1 on 2024-03-07 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("medicalStructureDataAdmin", "0004_llm"),
    ]

    operations = [
        migrations.AddField(
            model_name="record",
            name="model_id",
            field=models.ForeignKey(
                default="4401011977123232385643",
                on_delete=django.db.models.deletion.CASCADE,
                to="medicalStructureDataAdmin.llm",
                verbose_name="模型ID",
            ),
            preserve_default=False,
        ),
    ]
