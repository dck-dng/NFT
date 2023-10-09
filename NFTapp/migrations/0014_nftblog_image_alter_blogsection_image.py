# Generated by Django 4.2.5 on 2023-10-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFTapp', '0013_alter_blogsection_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='nftblog',
            name='image',
            field=models.ImageField(null=True, upload_to='blog/title/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='blogsection',
            name='image',
            field=models.ImageField(null=True, upload_to='blog/section/%Y/%m/%d/'),
        ),
    ]