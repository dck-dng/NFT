# Generated by Django 4.2.5 on 2023-10-23 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFTapp', '0002_queryresult_alter_user_cover_photo_searchresult_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchresult',
            name='result',
        ),
        migrations.AlterField(
            model_name='user',
            name='cover_photo',
            field=models.ImageField(default='/static/images/generic/Acer_Wallpaper_02_3840x2400.jpg', upload_to='avatar/%Y/%m/%d/'),
        ),
    ]