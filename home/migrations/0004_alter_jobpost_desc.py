# Generated by Django 3.2.3 on 2021-09-11 13:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210905_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='desc',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
