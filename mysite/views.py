from django.shortcuts import render
from django.views.generic import View
from apps.persona.models import Persona


class HomeView(View):
    def get(self, request):
        personas = Persona.objects.all()
        return render(request, 'home.html', {'personas': personas})

    def post(self, request):
        pass
