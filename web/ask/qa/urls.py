from django.urls import path
from . import views




urlpatterns = [
    path('/', views.test),
    path('login/', views.test),
    path('signup/', views.test),
    path('question/<int:id>/', views.test),
    path('ask/', views.test),
    path('popular/', views.test),
    path('new/', views.test),
]
