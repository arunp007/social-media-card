from django.urls import path
from.import views

urlpatterns = [
    path('media',views.media),
    path('card',views.card)
]