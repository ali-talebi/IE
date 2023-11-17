from django.contrib import admin
from .models import  USER_INFORMATION
from django.utils.html import  format_html
# Register your models here.


@admin.register(USER_INFORMATION)
class USER_INFORMATION_ADMIN(admin.ModelAdmin) :
    list_display = ("name" , "show_image" , "Email" , "about_user"  )


    def show_image(self , obj ) :
        return format_html('<img width=50px , height = 50px src="{}">'.format(obj.picture.url))