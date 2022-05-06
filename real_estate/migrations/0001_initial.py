# Generated by Django 4.0.4 on 2022-04-28 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=250)),
                ('address_line_1', models.CharField(max_length=200)),
                ('address_line_2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=30)),
                ('year_built', models.DateField()),
                ('no_of_bathrooms', models.IntegerField()),
                ('no_of_bedrooms', models.IntegerField()),
                ('description', models.TextField(verbose_name='About the Property')),
                ('sqft', models.PositiveIntegerField()),
                ('token_price', models.DecimalField(decimal_places=2, max_digits=2)),
                ('total_tokens', models.PositiveIntegerField()),
                ('token_sold', models.PositiveIntegerField()),
                ('is_occupied', models.BooleanField(default=False)),
                ('property_type', models.CharField(choices=[('Single Family', 'Single Family'), ('Multi Family', 'Multi Family'), ('Mixed Use', 'Mixed Use')], max_length=20)),
                ('starting_date', models.DateTimeField()),
                ('is_active', models.BooleanField()),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Underlying asset price')),
                ('closing_costs', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Closing costs')),
                ('llc_admin_fee_upfront', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Upfront LLC fees')),
                ('maintenance_reserve', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Initial maintenance reserve')),
                ('vacancy_reserve', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Vacancy Reserve')),
                ('listing_fee', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Listing fee')),
                ('irr', models.FloatField(help_text='10.99 %', verbose_name='Internal Rate of Return')),
                ('appreciation', models.FloatField(help_text='9.99 %', verbose_name='Projected Appreciation')),
                ('coc', models.FloatField(help_text='8.99 %', verbose_name='Cash on Cash return')),
                ('cap_rate', models.FloatField(help_text='7.63 %', verbose_name='Cap Rate')),
                ('taxes', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Property Taxes')),
                ('insurance', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Homeowners insurance')),
                ('management_fees', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Property Management')),
                ('llc_admin_fee_yearly', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Annual LLC administration and filing fees')),
                ('annual_cash_flow', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Annual cash flow')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HouseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/images/real_estate/house/house_image/')),
                ('is_primary', models.BooleanField(default=False)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='real_estate.house')),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='market',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='real_estate.location'),
        ),
    ]