from django.urls import path
from retete import views

app_name = 'retete'

urlpatterns = [
    path('', views.CreateReteteView.as_view(), name='retete'),
]