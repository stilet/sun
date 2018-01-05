from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import CounterE
from .forms import CounterEForm


class CounterListView(ListView):
    model = CounterE
    context_object_name = 'counters_e'
    template_name = 'counter/counter_e_list.html'
    paginate_by = 10

    def get_queryset(self):
        return CounterE.objects.filter(created_date__lte=timezone.now()).order_by("created_date")


class CounterDetailView(DetailView):
    model = CounterE
    template_name = 'counter/counter_detail.html'


def counter_e_new(request):
    if request.method == "POST":
        form = CounterEForm(request.POST)
        if form.is_valid():
            counter = form.save(commit=False)
            counter.autor = request.user
            counter.created_date = timezone.now()
            counter.save()
            return redirect('counter_e_list', )
    else:
        form = CounterEForm()
        return render(request, 'counter/counter_e_edit.html', {'form': form})
