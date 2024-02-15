# Generated by Django 5.0.1 on 2024-02-11 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_providers_rac", "0002_endpoint_maximum_connections"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="connectiontoken",
            options={
                "verbose_name": "RAC Connection token",
                "verbose_name_plural": "RAC Connection tokens",
            },
        ),
        migrations.AddField(
            model_name="racprovider",
            name="delete_token_on_disconnect",
            field=models.BooleanField(
                default=False,
                help_text="When set to true, connection tokens will be deleted upon disconnect.",
            ),
        ),
    ]