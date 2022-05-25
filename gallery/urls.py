from . import views
from django.urls import path

urlpatterns = [
    path('bralettes',views.bralettes, name='bralettes'),
    path('bandanas',views.bandanas, name='bandanas'),
    path('bags',views.bags, name='bags'),
    path('ties',views.ties, name='ties')
]