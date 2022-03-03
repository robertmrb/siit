from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from medicamente.models import Medicament
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.cache import cache_control

# Create your views here.

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url='login')
def medicamente(request):
    # return render(request, 'medicamente.html')

    if 'q' in request.GET:
        q = request.GET['q']
        all_medicamente_list = Medicament.objects.filter(
            Q(numemedicament__icontains=q)
        ).order_by('-data_expirarii')

    else:
        all_medicamente_list = Medicament.objects.all().order_by('-data_expirarii')
    paginator = Paginator(all_medicamente_list, 10)
    page = request.GET.get('page')
    all_medicamente = paginator.get_page(page)

    return render(request, 'medicamente.html', {'medicamente': all_medicamente})

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url='login')
def add_medicament(request):
    if request.method == 'POST':
        if request.POST.get('numemedicament') and request.POST.get('stoc') and request.POST.get('unitate') and request.POST.get(
                'data_expirarii'):
            medicament = Medicament()
            medicament.numemedicament = request.POST.get('numemedicament')
            medicament.stoc = request.POST.get('stoc')
            medicament.unitate = request.POST.get('unitate')
            medicament.data_expirarii = request.POST.get('data_expirarii')
            medicament.save()
            messages.success(request, "Medicament adaugat cu succes")
            return HttpResponseRedirect(reverse('medicamente:medicamente'))
    else:
        return render(request, 'adauga_medicament.html')

# functie accesare medicament
@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url='login')
def medicament(request, id):
    medicamentul = Medicament.objects.get(id=id)
    if medicamentul != None:
        return render(request, 'editare_medicament.html', {'medicament': medicamentul})

# functie editare pacient
@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url='login')
def editare_medicament(request):
    if request.method == 'POST':
        medicament = Medicament.objects.get(id=request.POST.get('id'))
        if medicament != None:
            medicament.numemedicament = request.POST.get('numemedicament')
            medicament.stoc = request.POST.get('stoc')
            medicament.unitate = request.POST.get('unitate')
            medicament.data_expirarii = request.POST.get('data_expirarii')
            medicament.save()

            messages.success(request, "Medicament editat cu succes")
            return HttpResponseRedirect(reverse('medicamente:medicamente'))

# functie sterge medicament
@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url='login')
def sterge_medicament(request, id):
    medicament = Medicament.objects.get(id = id)
    medicament.delete()

    messages.success(request, "Medicament sters!")
    return HttpResponseRedirect(reverse('medicamente:medicamente'))