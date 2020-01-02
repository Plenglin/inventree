# Generated by Django 2.2.2 on 2020-01-02 01:07

from django.db import migrations, models
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20200101_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtag',
            name='image',
            field=models.ImageField(null=True, upload_to='item/', validators=[inventory.models.validate_image]),
        ),
        migrations.AlterField(
            model_name='container',
            name='image',
            field=models.ImageField(null=True, upload_to='container/', validators=[inventory.models.validate_image]),
        ),
    ]
