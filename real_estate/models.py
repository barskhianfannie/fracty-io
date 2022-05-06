from django.db import models

# Create your models here.
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.utils.timezone import now

from real_estate.constants import PropertyType
from django.utils.translation import gettext_lazy as _

from real_estate.utils import get_next_number


class Location(models.Model):
    name = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.name


class House(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(null=True, blank=True)

    name = models.CharField(max_length=200, blank=True, default="", editable=False)
    address = models.CharField(max_length=250, blank=True, default="", editable=False)
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200, editable=False, blank=True, default="")
    city = models.CharField(max_length=200)
    # choice field for location
    market = models.ForeignKey(Location, on_delete=models.PROTECT)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=30)
    year_built = models.DateField()
    no_of_bathrooms = models.IntegerField()
    no_of_bedrooms = models.IntegerField()
    description = models.TextField(verbose_name=_("About the Property"))
    sqft = models.PositiveIntegerField()
    token_price = models.DecimalField(max_digits=20, decimal_places=2, )
    total_tokens = models.PositiveIntegerField()
    token_sold = models.PositiveIntegerField()
    is_occupied = models.BooleanField(default=False)
    property_type = models.CharField(choices=PropertyType.CHOICES, max_length=20)

    slug = models.SlugField(blank=True, unique=True, default="", editable=False)

    starting_date = models.DateTimeField()
    is_active = models.BooleanField()

    # ------First Block ------
    # Money
    sale_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=_("Underlying asset price"))
    closing_costs = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=_("Closing costs"))
    llc_admin_fee_upfront = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=_('Upfront LLC fees'))
    maintenance_reserve = models.DecimalField(max_digits=20, decimal_places=2,
                                              verbose_name=_('Initial maintenance reserve'))
    vacancy_reserve = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=_('Vacancy Reserve'))
    listing_fee = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=_('Listing fee'))

    # -------- Second Block
    # percentage
    irr = models.FloatField(verbose_name=_('Internal Rate of Return'), help_text=_("10.99 %"))
    appreciation = models.FloatField(verbose_name=_('Projected Appreciation'), help_text=_("9.99 %"))
    coc = models.FloatField(verbose_name=_('Cash on Cash return'), help_text=_("8.99 %"))
    cap_rate = models.FloatField(verbose_name=_('Cap Rate'), help_text=_("7.63 %"))

    # -- Third Block
    # Money
    taxes = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=_("Property Taxes"))
    insurance = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=_("Homeowners insurance"))
    management_fees = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=_("Property Management"))
    llc_admin_fee_yearly = models.DecimalField(max_digits=20, decimal_places=2,
                                               verbose_name=_("Annual LLC administration and filing fees"))
    annual_cash_flow = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=_("Annual cash flow"))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        address_line_2 = f"{self.city}, {self.state} {self.zip_code}"
        address = f"{self.address_line_1}, {address_line_2}"
        self.address = address
        self.name = address
        self.address_line_2 = address_line_2
        if not self.pk:
            slug = slugify(self.address)
            if House.objects.filter(slug=slug).exists():
                next_number = get_next_number(House, 'id')
                slug = f"{slug}-{next_number}"
            self.slug = slug
        super().save(*args, **kwargs)

    def primary_image(self):
        primary_image = self.images.filter(is_primary=True)
        if primary_image:
            return primary_image.first()
        return self.images.first()

    @property
    def monthly_cash_flow(self):
        return round(self.annual_cash_flow / 12, 2)

    @property
    def annual_gross_rents(self):
        return self.taxes + self.insurance + self.management_fees + self.llc_admin_fee_yearly + self.annual_cash_flow

    @property
    def total_investment_value(self):
        return self.sale_price + self.closing_costs + self.llc_admin_fee_upfront + self.maintenance_reserve

    @property
    def is_sold_out(self):
        if self.total_tokens == self.token_sold:
            return True

    @property
    def is_upcoming(self):
        if self.starting_date > now():
            return True

    def get_status(self):
        if self.is_sold_out:
            return "Sold"
        elif self.is_upcoming:
            return "Upcoming"
        elif self.is_active:
            return "Active"
        return "N/A"

    @property
    def tokens_left(self):
        return self.total_tokens - self.token_sold

    @property
    def tokens_sold_percentage(self):
        return (self.token_sold / self.total_tokens) * 100

    @property
    def tokens_sold_percentage_rounded(self):
        return round(self.tokens_sold_percentage)

    def financial_blocks(self):
        block_1 = [
            {"label": 'Total Investment Value', "value": self.total_investment_value},
            {"label": 'Underlying asset price', "value": self.sale_price},
            {"label": "Closing costs", "value": self.closing_costs},
            {"label": 'City Transfer Tax', "value": self.taxes},
            {"label": 'Upfront LLC fees:', "value": self.llc_admin_fee_upfront},
            {"label": f'Initial maintenance reserve', "value": self.maintenance_reserve},
            {"label": f'Vacancy reserve', "value": self.vacancy_reserve},
            {"label": f'Listing Fees', "value": self.listing_fee},
        ]

        block_2 = [
            {'label': "Total returns (IRR)", 'value': self.irr},
            {'label': 'Projected Appreciation', 'value': self.appreciation},
            {'label': 'Cash on Cash return', 'value': self.coc},
            {'label': 'Cap Rate', 'value': self.cap_rate},
        ]
        block_3 = [
            {'label': "Annual Gross Rents", 'value': self.annual_gross_rents},
            {'label': 'Property Taxes', 'value': self.taxes},
            {'label': 'Homeowners insurance', 'value': self.insurance},
            {'label': 'Property management', 'value': self.management_fees},
            {'label': 'Annual LLC administration and filing fees', 'value': self.llc_admin_fee_yearly},
            {'label': 'Annual cash flow', 'value': self.annual_cash_flow},
            {'label': 'Monthly cash flow', 'value': self.monthly_cash_flow},
        ]
        return {
            'block_1': block_1,
            'block_2': block_2,
            'block_3': block_3,
        }


class HouseImage(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='uploads/images/real_estate/house/house_image/')
    is_primary = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self._ensure_defaults_integrity()
        super().save(*args, **kwargs)

    def _ensure_defaults_integrity(self):
        if self.is_primary:
            self.__class__._default_manager.filter(house=self.house, is_primary=True).update(is_primary=False)
