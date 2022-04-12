
from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
app_name='accounts'

urlpatterns = [
    path('', views.home),
    path('lesson/', views.lesson),
    path('contact/', views.contact),
    path('products/',views.products,name='products'),
    path('dashboard/',views.dashboard,name='dashboard'),

    path('create_order/', views.createorder, name='create_order'),
    path('update_order/<str:pk>', views.update_order, name='update_order'),
    path('delete_order/<str:pk>', views.delete_order, name='delete_order'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.register,name='register'),
    path('booking/',views.booking,name='booking'),
    path('submit',views.submit,name='submit'),
    path('bookingdash/',views.bookingdash, name ='book')

]
