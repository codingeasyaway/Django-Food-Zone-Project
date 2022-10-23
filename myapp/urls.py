from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('profile/', views.user_profile, name="profile"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('menu/', views.menu, name="menu"),
    path('single_dish/<int:id>/', views.single_dish, name="single_dish"),
    path('contact/', views.contact, name="contact"),
    path('paypal_done/', views.paypal_done, name="paypal_done"),
    path('paypal_cancel/', views.paypal_cancel, name="paypal_cancel"),
]
