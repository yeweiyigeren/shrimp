# Generated by Django 2.0 on 2018-10-20 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181020_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumb_img',
            field=models.ImageField(blank=True, default='', null=True, upload_to='thumb/%m', verbose_name='缩略图'),
        ),
    ]
