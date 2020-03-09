# Generated by Django 3.0.4 on 2020-03-09 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.TextField(unique=True)),
                ('is_team_member', models.BooleanField(default=False, verbose_name='팀 멤버 유무')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
