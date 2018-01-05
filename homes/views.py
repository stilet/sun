from django.utils import timezone
from django.views.generic import ListView
from .models import Homes


class HomeListView(ListView):
    model = Homes
    context_object_name = 'homes'
    template_name = 'homes/home_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Homes.objects.filter().order_by("section")
