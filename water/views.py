from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from .models import CounterW
from .forms import CounterWForm


class WaterListView(ListView):
    model = CounterW
    context_object_name = 'counters_w'
    template_name = 'water/counter_w_list.html'
    paginate_by = 10

    def get_queryset(self):
        return CounterW.objects.filter(created_date__lte=timezone.now()).order_by("created_date")


class CounterWDetailView(DetailView):
    model = CounterW
    template_name = 'water/counter_w_detail.html'


def counter_w_new(request):
    if request.method == "POST":
        form = CounterWForm(request.POST)
        if form.is_valid():
            counter = form.save(commit=False)
            counter.autor = request.user
            counter.created_date = timezone.now()
            counter.save()
            return redirect('counter_w_list', )
    else:
        form = CounterWForm()
        return render(request, 'water/counter_w_edit.html', {'form': form})
