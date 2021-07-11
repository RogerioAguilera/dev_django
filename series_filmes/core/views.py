from django.shortcuts import render

# Create your views here.

# def index(request):
#     return redirect('/series/')

def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'series.html', dados)