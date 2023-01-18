from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import PersonaSerializers
from .models import Persona
from django.shortcuts import render, redirect
#HttpResponseRedirect.
from django.http import HttpResponseRedirect




class PersonaList(APIView):
    def get(self, request):
        personas = Persona.objects.all()
        serializer = PersonaSerializers(personas, many=True).data
        count = personas.count()
        return render(request, 'home.html', {'personas': personas})

    def post(self, request):
        serializer = PersonaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponseRedirect('/')

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class PersonaDetail(APIView):
    def get_object(self, pk):
        try:
            persona = Persona.objects.get(pk=pk)
            return persona
        except Persona.DoesNotExist:
            raise Http404

    # @csrf_protect
    def get(self, request, pk):
        persona = self.get_object(pk)
        serializer = PersonaSerializers(persona).data
        context = {
            'persona': persona
        }
        return render(request, 'form.html', context)

    def post(self, request, pk):
        persona = self.get_object(pk)
        serializer = PersonaSerializers(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponseRedirect('/api/persona/')
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class PersonaDelete(APIView):
    def get_object(self, pk):
        try:
            persona = Persona.objects.get(pk=pk)
            return persona
        except Persona.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        persona = self.get_object(pk)
        persona.delete()
        return redirect('home')