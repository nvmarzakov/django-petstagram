from django.urls import path, include

from petstagram.pets.views import add_pet, details_pet,edit_pet, delete_pet

urlpatterns = (
    path('add/', add_pet, name='add-pet'),
    path('<str:username>/pet/<slug:pet_name>/', include([
        path('', details_pet, name='details-pet-page'),
        path('edit/', edit_pet, name='edit-pet-page'),
        path('delete/', delete_pet, name='delete-pet-page')
    ]))
)