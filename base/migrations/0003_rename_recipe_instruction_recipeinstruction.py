# Generated by Django 4.0.4 on 2022-07-20 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_recipe_recipe_instruction'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipe_instruction',
            new_name='RecipeInstruction',
        ),
    ]