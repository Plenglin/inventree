# Generated by Django 3.0.6 on 2020-05-24 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_containeruuid_itemuuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemuuid',
            name='parent',
        ),
        migrations.DeleteModel(
            name='ContainerUUID',
        ),
        migrations.DeleteModel(
            name='ItemUUID',
        ),
    ]
