# Generated by Django 2.2.4 on 2020-01-18 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sih', '0025_auto_20200118_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='personinneed',
            name='audio',
            field=models.FileField(default='Sound', upload_to='sih/static/Audio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='audio',
            name='aud',
            field=models.FileField(upload_to='sih/static/Audio'),
        ),
        migrations.AlterField(
            model_name='personinneed',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
