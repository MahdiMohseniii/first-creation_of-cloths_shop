# Generated by Django 4.2.14 on 2024-07-18 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(choices=[('classic', 'Classic'), ('modern', 'Modern')], max_length=15)),
                ('product_type', models.CharField(choices=[('tshirt', 'T-Shirt'), ('shirt', 'Shirt'), ('pants', 'Pants'), ('skirt', 'Skirt'), ('dress', 'Dress')], max_length=20)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Men',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('size', models.CharField(choices=[('small', 'S'), ('medium', 'M'), ('large', 'L'), ('xlarge', 'XL'), ('xxlarge', 'XXL')], max_length=20)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('pt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='men_by_product_p_t', to='products.product')),
                ('st', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='men_by_product_s_t', to='products.product')),
            ],
        ),
    ]
