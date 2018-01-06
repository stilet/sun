from django.conf.urls import url
from . import views
from .models import CounterW

urlpatterns = [
    url(r'^counter_w$', views.WaterListView.as_view(),
        name='counter_w_list'),  # список счетчиков воды
    url(r'^counter_w/new/$', views.counter_w_new, name='counter_w_new'),
    url(r'counter_w/(?P<pk>\d+)/', views.CounterWDetailView.as_view(model=CounterW), name='counter_w_detail')
]
