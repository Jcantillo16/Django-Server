from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import PersonaSerializers
from .models import Persona
from django.shortcuts import render, redirect


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
            return redirect('home')
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class PersonaDetail(APIView):
    def get_object(self, pk):
        try:
            return Persona.objects.get(pk=pk)
        except Persona.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        persona = self.get_object(pk)
        serializer = PersonaSerializers(persona).data
        return Response(serializer)

    def put(self, request, pk):
        persona = self.get_object(pk)
        serializer = PersonaSerializers(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        try:
            persona = self.get_object(pk)
            persona.delete()
            return render(request, 'home.html', {'persona': persona})
        except Persona.DoesNotExist:
            raise Http404
