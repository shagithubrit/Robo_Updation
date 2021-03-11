# Generated by Django 3.0.3 on 2021-03-11 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_overview'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareKey',
            fields=[
                ('location', models.TextField()),
                ('token', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_seconds', models.BigIntegerField()),
            ],
        ),
    ]
