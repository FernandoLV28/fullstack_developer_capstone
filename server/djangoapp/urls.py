# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
    path(route='register', view=views.registration, name='register'),
    
    # path for login
    path(route='login', view=views.login_user, name='login'),
    
    #path for logout
    path(route='logout', view=views.logout_request, name='logout'),

    # path for dealer reviews view

    # path for add a review view
    
    #path for get cars
    path(route='cars', view=views.get_cars, name ='getcars'),
    
    #path for get car makes
    path(route='cars_makes', view=views.get_car_make, name ='getmake')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
