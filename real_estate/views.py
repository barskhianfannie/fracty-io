from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView

from real_estate.constants import PropertyType
from real_estate.models import House, Location


class HomePageView(ListView):
    template_name = 'real_estate/house_list.html'
    model = House
    queryset = House.objects.all().order_by('-id')

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx['locations'] = Location.objects.values_list('name', flat=True)
        ctx['property_types'] = dict(PropertyType.CHOICES).keys()
        return ctx


def get_house_detail(request, slug):
    object = get_object_or_404(House, slug=slug)
    return render(request, 'real_estate/house_detail.html', {'object': object})
