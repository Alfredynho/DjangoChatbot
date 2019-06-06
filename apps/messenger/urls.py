from django.urls import path, include

from .views import BotView

urlpatterns = [
    path('webhook',BotView.as_view(), name='fb-webhook'),
]