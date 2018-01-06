from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Pko
from .forms import PkoForm


class PkoListView(ListView):
    model = Pko
    context_object_name = 'pkos'
    template_name = 'pko/pko_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Pko.objects.filter(created_date__lte=timezone.now()).order_by("created_date")


class PkoDetailView(DetailView):
    model = Pko
    template_name = 'pko/pko_detail.html'

def rko_new(request):
    if request.method == "POST":
        form = PkoForm(request.POST)
        if form.is_valid():
            counter = form.save(commit=False)
            counter.autor = request.user
            counter.created_date = timezone.now()
            counter.save()
            return redirect('pko_list', )
    else:
        form = PkoForm()
        return render(request, 'pko/pko_edit.html', {'form': form})
