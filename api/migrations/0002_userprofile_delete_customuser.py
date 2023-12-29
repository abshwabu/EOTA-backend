# Generated by Django 4.2.7 on 2023-12-29 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('occupation', models.CharField(blank=True, max_length=50)),
                ('religion', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]