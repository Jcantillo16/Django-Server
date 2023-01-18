from django.shortcuts import render
from django.views.generic import View
from apps.persona.models import Persona
from apps.persona.views import PersonaDetail


class HomeView(View):
    def get(self, request):
        personas = Persona.objects.all()
        return render(request, 'home.html', {'personas': personas})


class formView(View):
    def get(self, request):
        return render(request, 'form.html')
