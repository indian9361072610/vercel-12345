# Generated by Django 4.0.6 on 2022-09-24 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_age_datas_password_alter_datas_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datas',
            name='Address',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datas',
            name='Contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='datas',
            name='Mail',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datas',
            name='Password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datas',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imges/'),
        ),
    ]
