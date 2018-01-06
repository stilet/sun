from django.conf.urls import url
from . import views
from .models import Pko

urlpatterns = [
    url(r'^pko$', views.PkoListView.as_view(), name='pko_list'),  # список кассовых ордеров
    url(r'^pko/new/$', views.rko_new, name='pko_new'),
    # url(r'pko/(?P<pk>[0-9]+)/$', views.PkoDetailView.as_view(), name='detail'),
    url(r'pko/(?P<pk>\d+)/', views.PkoDetailView.as_view(model=Pko), name='pko_detail'),
]
