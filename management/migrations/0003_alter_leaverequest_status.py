# Generated by Django 4.2.4 on 2023-08-27 03:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "management",
            "0002_remove_employee_email_remove_employee_first_name_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="leaverequest",
            name="status",
            field=models.CharField(
                choices=[("Accepted", "Accepted"), ("Pending", "Pending")],
                default="Pending",
                max_length=20,
            ),
        ),
    ]