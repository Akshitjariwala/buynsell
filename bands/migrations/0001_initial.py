# Generated by Django 2.0 on 2017-12-15 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('attribute_name', models.CharField(max_length=20)),
                ('Att_id', models.AutoField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(max_length=15, primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Ad',
            fields=[
                ('ad_title', models.TextField(max_length=50)),
                ('product_category', models.CharField(max_length=20)),
                ('product_subcategory', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('product_description', models.TextField(max_length=300, null=True)),
                ('price', models.IntegerField(max_length=15)),
                ('phone_no', models.IntegerField(max_length=12)),
                ('ad_id', models.AutoField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product_attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.CharField(max_length=30)),
                ('attributes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bands.Attributes')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bands.Product_Ad')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('subcat_id', models.AutoField(max_length=15, primary_key=True, serialize=False)),
                ('subcat_name', models.CharField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bands.Category')),
            ],
        ),
        migrations.CreateModel(
            name='User_Data',
            fields=[
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('user_email', models.EmailField(max_length=20)),
                ('user_password', models.TextField(max_length=15)),
                ('user_id', models.AutoField(max_length=15, primary_key=True, serialize=False)),
                ('user_phone_no', models.CharField(max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='product_ad',
            name='user_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bands.User_Data'),
        ),
        migrations.AddField(
            model_name='attributes',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bands.SubCategory'),
        ),
    ]