# Generated by Django 3.1.2 on 2021-10-04 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FARGApp', '0013_auto_20211003_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='testmodel',
            fields=[
                ('Aut0ID', models.AutoField(primary_key=True, serialize=False)),
                ('ooner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
