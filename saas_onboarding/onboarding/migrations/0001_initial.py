# Generated by Django 4.2.7 on 2023-11-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('org_id', models.AutoField(primary_key=True, serialize=False)),
                ('org_id_name', models.CharField(max_length=255, unique=True)),
                ('org_phone', models.CharField(max_length=20)),
                ('org_email', models.EmailField(max_length=254, unique=True)),
                ('service', models.ManyToManyField(to='onboarding.service')),
            ],
        ),
    ]
