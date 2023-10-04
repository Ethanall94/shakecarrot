# Generated by Django 4.2.5 on 2023-09-29 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrot_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionshopimages',
            name='shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='carrot_app.regionshop'),
        ),
        migrations.AlterField(
            model_name='regionshopproductprice',
            name='region_shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price', to='carrot_app.regionshop'),
        ),
    ]