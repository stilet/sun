from django.conf.urls import url
from . import views
from .models import Rko

urlpatterns = [
    url(r'^rko$', views.RkoListView.as_view(), name='rko_list'),  # список кассовых ордеров
    url(r'^rko/new/$', views.rko_new, name='rko_new'),
    url(r'rko/(?P<pk>\d+)/', views.RkoDetailView.as_view(model=Rko), name='rko_detail'),
]

