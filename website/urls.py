from login import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # url
    path('', auth_views.LoginView.as_view(template_name='signIn.html'), name='home'),
    path('signin/', views.signIn, name='signIn'),
    path('signup/', views.signUp, name='signUp'),
    path('postsign/', views.postSignIn, name='postSignIn'),
    path('logout/', auth_views.LoginView.as_view(template_name='signIn.html'), name="logout"),
    path('postsignup/', views.postSignUp, name="postSignUp"),

]
