# Generated by Django 4.2.3 on 2023-08-02 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_title'),
        ('saved_recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedrecipe',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.recipe'),
        ),
    ]
