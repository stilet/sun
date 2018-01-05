from django.conf.urls import url
from . import views
from .models import CounterE

urlpatterns = [
    url(r'^counter_e$', views.CounterListView.as_view(),
        name='counter_e_list'),  # список счетчиков электричества
    url(r'^counter_e/new/$', views.counter_e_new, name='counter_e_new'),
    #url(r'^(?P<pk>[0-9]+)/$', views.CounterDetailView.as_view(), name='detail'),
    url(r'counter_e/(?P<pk>\d+)/', views.CounterDetailView.as_view(model=CounterE), name='counter_detail')
]
