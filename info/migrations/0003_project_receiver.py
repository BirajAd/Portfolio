# Generated by Django 3.1.7 on 2021-02-28 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info', '0002_award_receiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='receiver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='list_project', to='auth.user'),
            preserve_default=False,
        ),
    ]
