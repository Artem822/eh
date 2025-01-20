# Generated by Django 4.2 on 2024-12-17 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_alter_employee_more_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdivision',
            name='description',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='employees',
            field=models.ManyToManyField(null=True, related_name='subdivision_employees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='sub_sub_division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='models.subsubdivision'),
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervisor', to=settings.AUTH_USER_MODEL),
        ),
    ]
