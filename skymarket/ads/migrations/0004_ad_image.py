# Generated by Django 4.1.7 on 2023-05-04 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_comment_options_alter_ad_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
