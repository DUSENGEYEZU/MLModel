# Generated by Django 3.1.2 on 2021-10-02 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FARGApp', '0011_auto_20211002_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='PharomacyTransfer',
            fields=[
                ('certID', models.IntegerField(primary_key=True, serialize=False)),
                ('certTitle', models.CharField(default='Certificate of merits For FARG  Beneficial ', editable=False, max_length=100)),
                ('certDate', models.DateTimeField()),
                ('Agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FARGApp.agentmodel')),
                ('Beneficial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FARGApp.beneficialmodel')),
                ('Pharomacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FARGApp.pharomacymodel')),
                ('TransiderName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FARGApp.transfermodels')),
            ],
        ),
        migrations.CreateModel(
            name='CertificateTransfer',
            fields=[
                ('certID', models.IntegerField(primary_key=True, serialize=False)),
                ('certTitle', models.CharField(default='Certificate of merits For FARG  Beneficial ', editable=False, max_length=100)),
                ('certDate', models.DateTimeField()),
                ('Agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FARGApp.agentmodel')),
                ('Beneficial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FARGApp.beneficialmodel')),
                ('TransiderName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FARGApp.transfermodels')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FARGApp.hospitalmodel')),
            ],
        ),
    ]
