from django.urls import path
from .views import  SEARCH_WEBSITE , TOTAL_USER,  ABOUT_WEBSITE_DESCRIPTION ,  Home , SELECT_TAGS , Read_Post , CONTACT_US  , SELECT_CATEGORY 


app_name = "BLOG"
urlpatterns = [
    path("" , Home , name="Home") , 
    path("SELECT_TAGS/<slug:tag>/" , SELECT_TAGS , name="SELECT_TAGS"  ) ,
    path("READ_POST/<int:id>/" , Read_Post , name="Read_Post" ) ,  
    path("CONTACT_US/" , CONTACT_US , name="CONTACT_US" ) , 
    path("TOTAL_USER/" , TOTAL_USER , name="TOTAL_USER" ) , 
    path("SELECT_CATEGORY/<slug:category>/" , SELECT_CATEGORY , name="SELECT_CATEGORY" ) , 
    path("ABOUT_WEBSITE_DESCRIPTION/" , ABOUT_WEBSITE_DESCRIPTION , name="ABOUT_WEBSITE_DESCRIPTION" )  , 
    path("SEARCH_WEBSITE/" , SEARCH_WEBSITE , name="SEARCH_WEBSITE" )
]

