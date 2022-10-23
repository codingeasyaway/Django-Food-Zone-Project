# Generated by Django 3.1.7 on 2022-09-15 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_category_dish_profile_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='contact_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]