# Generated by Django 4.1.4 on 2023-06-05 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_items_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='item',
            name='item_about',
            field=models.TextField(null=True),
        ),
    ]