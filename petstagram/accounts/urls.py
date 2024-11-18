from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/<int:pk>/', include([
        path('', views.details, name='details'),
        path('edit/', views.edit, name='edit'),
        path('delete/', views.delete, name='delete'),
    ]))
]
