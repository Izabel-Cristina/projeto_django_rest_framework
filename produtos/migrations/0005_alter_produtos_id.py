# Generated by Django 4.1.7 on 2023-02-26 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produtos", "0004_rename_quantidade_produtos_quantidade_estoque"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produtos",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
