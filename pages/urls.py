from django.urls import path
from posts import views
from .views import (
            AboutView,
            HomeView
            )

urlpatterns = [
    path('about/', AboutView.as_view(), name= 'about'),
    path('', HomeView.as_view(), name= 'home'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name= 'update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name= 'delete')
]