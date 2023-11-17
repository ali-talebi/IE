from django.urls import path
from .views import Show_USER 


app_name = "CLIENT"
urlpatterns = [
    path("INFORMATION_AUTHOR/<int:id>/" , Show_USER , name="Show_USER" ) ,     

]