from django.urls import path
from django.conf.urls import url

from .views import AuthorListView, AuthorDetailView

urlpatterns = [
    path('', AuthorListView.as_view(), name='author-list'),
    url(r'^detalle_autor/(?P<pk>\d+)$', AuthorDetailView.as_view(), name='author-detail'),
]