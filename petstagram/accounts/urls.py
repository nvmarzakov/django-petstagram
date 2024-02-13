import profile

from django.urls import path, include

from petstagram.accounts.views import login_account, register_account, details_account, edit_account, delete_account

urlpatterns = (
    path('login/', login_account, name='login-page'),
    path('register/', register_account, name='register-page'),
    path('profile/<int:pk>/', include([
        path('', details_account, name='details-page'),
        path('edit/', edit_account, name='edit-page'),
        path('delete/', delete_account, name='delete-page'),
    ]))
)