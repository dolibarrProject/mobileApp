# Generated by Django 4.2.3 on 2023-07-28 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryId', models.AutoField(primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('cityId', models.AutoField(primary_key=True, serialize=False)),
                ('cityName', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('credentialId', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.AutoField(primary_key=True, serialize=False)),
                ('orderDate', models.DateField()),
                ('orderTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PointOfSale',
            fields=[
                ('posId', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=200)),
                ('cashierName', models.CharField(max_length=100)),
                ('cityName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApp1.cities')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=20)),
                ('cityAddress', models.CharField(max_length=100)),
                ('creatDate', models.DateField(auto_now_add=True, null=True)),
                ('updateDate', models.DateField(auto_now=True, null=True)),
                ('terms', models.CharField(choices=[('CDI', 'CDI'), ('CDD', 'CDD'), ('SESONIER', 'SESONIER'), ('EXTERN', 'EXTERN')], max_length=10)),
                ('userName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApp1.credentials')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('vehiculeId', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('licensePlate', models.CharField(max_length=20)),
                ('numChassis', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Moral',
            fields=[
                ('pointofsale_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mobileApp1.pointofsale')),
                ('organizationName', models.CharField(max_length=100)),
            ],
            bases=('mobileApp1.pointofsale',),
        ),
        migrations.CreateModel(
            name='Physical',
            fields=[
                ('pointofsale_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mobileApp1.pointofsale')),
                ('storeName', models.CharField(max_length=100)),
            ],
            bases=('mobileApp1.pointofsale',),
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('warehouseId', models.BigAutoField(primary_key=True, serialize=False)),
                ('addressWarehouse', models.CharField(max_length=200)),
                ('capacity', models.IntegerField()),
                ('maxCapacity', models.IntegerField()),
                ('unity', models.CharField(choices=[('m3', 'm3'), ('m2', 'm2'), ('PALETTE', 'PALETTE')], max_length=10)),
                ('cityName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApp1.cities')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productId', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoryName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApp1.category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderCard',
            fields=[
                ('orderCardId', models.AutoField(primary_key=True, serialize=False)),
                ('orderCardDate', models.DateField()),
                ('totalAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApp1.order')),
                ('posId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApp1.pointofsale')),
                ('vehiculeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApp1.vehicule')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='productName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApp1.product'),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('contractID', models.BigAutoField(primary_key=True, serialize=False)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApp1.users')),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mobileApp1.users')),
                ('groupReference', models.IntegerField()),
                ('teamSize', models.IntegerField()),
                ('cityName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supervisor_city', to='mobileApp1.cities')),
            ],
            bases=('mobileApp1.users',),
        ),
        migrations.CreateModel(
            name='Storekeeper',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='mobileApp1.users')),
                ('storekeeperId', models.AutoField(primary_key=True, serialize=False)),
                ('addressWarehouse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mobileApp1.warehouse')),
            ],
            bases=('mobileApp1.users',),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mobileApp1.users')),
                ('salesRegion', models.CharField(max_length=100)),
                ('supervised', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_supervisor', to='mobileApp1.users')),
            ],
            bases=('mobileApp1.users',),
        ),
        migrations.CreateModel(
            name='PreSeller',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mobileApp1.users')),
                ('salesTarget', models.FloatField()),
                ('commissionRate', models.FloatField()),
                ('supervised', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preseller_supervisor', to='mobileApp1.users')),
            ],
            bases=('mobileApp1.users',),
        ),
        migrations.AddField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApp1.seller'),
        ),
        migrations.CreateModel(
            name='DeliveryGuy',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mobileApp1.users')),
                ('cityName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_guy_city', to='mobileApp1.cities')),
                ('supervised', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_guy_supervisor', to='mobileApp1.users')),
                ('vehiculeId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mobileApp1.vehicule')),
            ],
            bases=('mobileApp1.users',),
        ),
    ]
