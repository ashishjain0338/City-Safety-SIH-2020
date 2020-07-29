# Generated by Django 2.2.4 on 2020-01-18 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sih', '0019_auto_20200115_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='Address',
            field=models.CharField(default='Unknown', max_length=500),
        ),
        migrations.AlterField(
            model_name='personinneed',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]