# Generated by Django 5.0.2 on 2024-03-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_rename_city_user_location_remove_user_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='comp_num',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='CorpUser',
        ),
    ]