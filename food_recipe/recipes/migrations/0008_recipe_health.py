# Generated by Django 4.2.3 on 2023-08-13 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipe_calories'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='health',
            field=models.JSONField(default=list),
        ),
    ]
