from django.urls import path
from pacienti import views

app_name = 'pacienti'

urlpatterns = [
    path('', views.pacienti, name='pacienti'),
    #path adauga pacient
    path('add_pacient', views.add_pacient, name='add_pacient'),
    # path accesare pacient
    path('pacient/<str:nrgestiune>', views.pacient, name='pacient'),
    # path editare pacient
    path('editare_pacient', views.editare_pacient, name='editare_pacient'),
    # path stergere pacient
    path('sterge_pacient/<str:nrgestiune>', views.sterge_pacient, name='sterge_pacient'),
]