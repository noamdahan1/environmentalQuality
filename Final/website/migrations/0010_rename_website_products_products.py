# Generated by Django 5.0.2 on 2024-03-08 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_user_comp_num_delete_corpuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='website_products',
            new_name='products',
        ),
    ]