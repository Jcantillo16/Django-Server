from django.urls import path
from .views import PersonaList, PersonaDetail

urlpatterns = [
    path('persona/', PersonaList.as_view(), name='persona_list'),
    path('persona/<int:pk>/', PersonaDetail.as_view(), name='persona_detail'),
]
