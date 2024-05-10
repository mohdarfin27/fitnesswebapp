from django.urls import path
from . import views
from .views import my_function
from .views import bmi
from .views import videoplay
from .views import videohome
#from .views import linkedin
urlpatterns = [
    path('',views.say_hello),
     path('urld/',views.my_function),
     path('BMI/',views.bmi),
      #path('arfin/bot', views.home, name='home')
      path('chatbot_response/', views.chatbot_response, name='chatbot_response'),
      path('fitchat/',views.linkedin,name='fitchat'),
      path('video/',views.videoplay),
       path('videohome/',views.videohome),
         path('fitshop/',views.ecommerce),
         path('videohome/ecto/',views.ecto),
         path('videohome/endo/',views.endo),
         path('videohome/meso/',views.meso),
        path('workhome/', views.vid)
    
   
]