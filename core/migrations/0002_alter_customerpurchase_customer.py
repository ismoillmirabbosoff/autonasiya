# Generated by Django 4.2.4 on 2023-08-10 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_remove_customer_groups_remove_customer_last_login_and_more'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerpurchase',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.customer'),
        ),
    ]