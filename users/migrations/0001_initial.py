# Generated by Django 3.1.7 on 2021-02-21 12:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='static/img/def_user.jpg', null=True, upload_to=users.models.u_d_p, verbose_name='Avatar')),
                ('bio', models.TextField(default='No Biography Yet', max_length=1500, verbose_name='Bio')),
                ('slogan', models.CharField(default='You can if you think you can !', max_length=300, verbose_name='Slogan')),
                ('birthday', models.DateField(default=datetime.datetime(2002, 1, 1, 1, 1, 1, 1))),
                ('slug', models.SlugField(default=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL), unique=True, verbose_name='Slug')),
                ('created', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'ordering': ('created',),
            },
        ),
    ]
