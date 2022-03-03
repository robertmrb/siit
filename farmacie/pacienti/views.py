from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pacienti.models import Pacient
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_control


@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url='login')
def pacienti(request):
    # return render(request, "pacienti.html")

    if 'q' in request.GET:
        q = request.GET['q']
        all_pacienti_list = Pacient.objects.filter(
            Q(nume__icontains=q) | Q(telefon__icontains=q) | Q(email__icontains=q) | Q(varsta__icontains=q) | Q(
                gen__icontains=q) | Q(observatii__icontains=q)
        ).order_by('-data_adaugarii')

    else:
        all_pacienti_list = Pacient.objects.all().order_by('-data_adaugarii')
    paginator = Paginator(all_pacienti_list, 10)
    page = request.GET.get('page')
    all_pacienti = paginator.get_page(page)

    return render(request, 'pacienti.html', {'pacienti': all_pacienti})

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url='login')
def add_pacient(request):
    if request.method == 'POST':
        if request.POST.get('nume') and request.POST.get('telefon') and request.POST.get('email') and request.POST.get(
                'varsta') and request.POST.get('gen') or request.POST.get('observatii'):
            pacient = Pacient()
            pacient.nume = request.POST.get('nume')
            pacient.telefon = request.POST.get('telefon')
            pacient.email = request.POST.get('email')
            pacient.varsta = request.POST.get('varsta')
            pacient.gen = request.POST.get('gen')
            pacient.observatii = request.POST.get('observatii')
            pacient.save()
            messages.success(request, "Pacient adaugat cu succes")
            return HttpResponseRedirect(reverse('pacienti:pacienti'))
    else:
        return render(request, 'adauga_pacient.html')


# functie accesare pacient individual
@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url='login')
def pacient(request, nrgestiune):
    pacientul = Pacient.objects.get(nrgestiune=nrgestiune)
    if pacientul != None:
        return render(request, 'editare.html', {'pacient': pacientul})


# functie editare pacient
@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url='login')
def editare_pacient(request):
    if request.method == 'POST':
        pacient = Pacient.objects.get(nrgestiune=request.POST.get('nrgestiune'))
        if pacient != None:
            pacient.nume = request.POST.get('nume')
            pacient.telefon = request.POST.get('telefon')
            pacient.email = request.POST.get('email')
            pacient.varsta = request.POST.get('varsta')
            pacient.gen = request.POST.get('gen')
            pacient.observatii = request.POST.get('observatii')
            pacient.save()

            messages.success(request, "Pacient editat cu succes")
            return HttpResponseRedirect(reverse('pacienti:pacienti'))


# functie sterge pacient
@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url='login')
def sterge_pacient(request, nrgestiune):
    pacient = Pacient.objects.get(nrgestiune = nrgestiune)
    pacient.delete()

    messages.success(request, "Pacient sters!")
    return HttpResponseRedirect(reverse('pacienti:pacienti'))