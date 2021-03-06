# Generated by Django 3.0.5 on 2021-02-18 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virus', '0012_auto_20210205_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'ordering': ['c_time'],
            },
        ),
        migrations.AlterModelOptions(
            name='asset',
            options={'verbose_name': '资产请购表', 'verbose_name_plural': '资产请购表'},
        ),
    ]
