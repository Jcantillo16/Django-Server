from django.urls import path
from .views import PersonaList, PersonaDetail, PersonaDelete

urlpatterns = [
    path('persona/', PersonaList.as_view(), name='persona_list'),
    path('persona/<int:pk>/', PersonaDetail.as_view(), name='persona_detail', ),
    path('persona/delete/<int:pk>/', PersonaDelete.as_view(), name='persona_delete', ),
]
