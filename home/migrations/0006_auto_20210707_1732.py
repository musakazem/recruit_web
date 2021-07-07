# Generated by Django 3.2.3 on 2021-07-07 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('home', '0005_auto_20210707_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePic',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('profile_pic', models.ImageField(default='', upload_to='pics/')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
    ]
