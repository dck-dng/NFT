# Generated by Django 4.2.5 on 2023-10-07 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NFTapp', '0007_alter_nftproduct_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to='NFTapp.nftblog'),
        ),
        migrations.AlterField(
            model_name='blogimage',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_image', to='NFTapp.nftblog'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_comments', to='NFTapp.nftproduct'),
        ),
    ]
