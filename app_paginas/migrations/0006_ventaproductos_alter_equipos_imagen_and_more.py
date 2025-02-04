# Generated by Django 5.1.4 on 2024-12-23 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_paginas", "0005_alter_equipos_imagen_alter_kits_imagen_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="VentaProductos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=20)),
                (
                    "imagen",
                    models.ImageField(
                        blank=True, null=True, upload_to="imagenes_productos"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="equipos",
            name="imagen",
            field=models.ImageField(
                blank=True, null=True, upload_to="imagenes_productos"
            ),
        ),
        migrations.AlterField(
            model_name="kits",
            name="imagen",
            field=models.ImageField(
                blank=True, null=True, upload_to="imagenes_productos"
            ),
        ),
        migrations.AlterField(
            model_name="material",
            name="imagen",
            field=models.ImageField(
                blank=True, null=True, upload_to="imagenes_productos"
            ),
        ),
        migrations.AlterField(
            model_name="mediocultivo",
            name="imagen",
            field=models.ImageField(
                blank=True, null=True, upload_to="imagenes_productos"
            ),
        ),
        migrations.AlterField(
            model_name="reactivos",
            name="imagen",
            field=models.ImageField(
                blank=True, null=True, upload_to="imagenes_productos"
            ),
        ),
        migrations.AlterField(
            model_name="sucursales",
            name="imagen",
            field=models.ImageField(
                blank=True, null=True, upload_to="imagenes_productos"
            ),
        ),
    ]
