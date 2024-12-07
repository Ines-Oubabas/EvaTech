from django.contrib import admin
from django.urls import path
from evaluation import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Page d'accueil

    # Authentification (Connexion / Déconnexion / Inscription)
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),

    # Pages utilisateur
    path('dashboard/', views.dashboard, name='dashboard'),
    path('questions/', views.question_page, name='question_page'),
    path('results/', views.result_page, name='result_page'),
    
    # URL pour les enseignants
path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
path('create_test/', views.create_test, name='create_test'),

# URL pour les étudiants
path('available_tests/', views.available_tests, name='available_tests'),

]
