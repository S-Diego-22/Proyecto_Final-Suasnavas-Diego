# Generated by Django 5.1.4 on 2024-12-24 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_paginas", "0009_ventaproductos"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipos",
            name="descripcion",
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="equipos",
            name="nombre",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="kits",
            name="descripcion",
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="kits",
            name="nombre",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="material",
            name="descripcion",
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="material",
            name="nombre",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="mediocultivo",
            name="descripcion",
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="mediocultivo",
            name="nombre",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="reactivos",
            name="descripcion",
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="reactivos",
            name="nombre",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="ventaproductos",
            name="descripcion",
            field=models.TextField(max_length=500),
        ),
    ]
