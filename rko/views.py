from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .models import Rko
from .forms import RkoForm


class RkoListView(ListView):
    model = Rko
    context_object_name = 'rkos'
    template_name = 'rko/rko_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Rko.objects.filter(created_date__lte=timezone.now()).order_by("created_date")


class RkoDetailView(DetailView):
    model = Rko
    template_name = 'rko/rko_detail.html'


def rko_new(request):
    if request.method == "POST":
        form = RkoForm(request.POST)
        if form.is_valid():
            counter = form.save(commit=False)
            counter.autor = request.user
            counter.created_date = timezone.now()
            counter.save()
            return redirect('rko_list', )
    else:
        form = RkoForm()
        return render(request, 'rko/rko_edit.html', {'form': form})
