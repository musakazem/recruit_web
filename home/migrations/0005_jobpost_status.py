# Generated by Django 3.2.3 on 2021-09-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_jobpost_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
