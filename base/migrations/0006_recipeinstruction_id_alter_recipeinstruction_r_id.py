# Generated by Django 4.0.4 on 2022-07-20 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_recipeinstruction_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeinstruction',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipeinstruction',
            name='r_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.recipe'),
        ),
    ]