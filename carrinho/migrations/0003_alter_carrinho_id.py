# Generated by Django 4.1.7 on 2023-02-26 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carrinho", "0002_carrinho_preco"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carrinho",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]