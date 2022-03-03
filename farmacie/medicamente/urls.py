from django.urls import path
from medicamente import views

app_name = 'medicamente'

urlpatterns = [
    path('', views.medicamente, name='medicamente'),
    path('add_medicament', views.add_medicament, name='add_medicament'),
    # path accesare medicament
    path('medicament/<str:id>', views.medicament, name='medicament'),
    # path editare medicment
    path('editare_medicament', views.editare_medicament, name='editare_medicament'),
    # path stergere medicament
    path('sterge_medicament/<str:id>', views.sterge_medicament, name='sterge_medicament'),

]