from django.contrib import admin
from .models import ABOUT_US_MODEL ,  SOCIAL_MEDIA_WEBSITE , Contact_us ,  Post , Category_of_Post , TOTAL_TAGS , Comments_of_Post , INSTAGRAM_POST , ABOUT_WEBSITE 
from django.utils.html import format_html
# Register your models here.


@admin.register(ABOUT_US_MODEL)
class ABOUT_US_MODEL_ADMIN(admin.ModelAdmin) : 
    list_display = ("main_mission_mine_title" , "show_image1")



    def show_image1(self , obj ) : 
        return format_html('<img width=50px , height=50px src="{}">'.format(obj.picture1.url))

@admin.register(SOCIAL_MEDIA_WEBSITE)
class SOCIAL_MEDIA_WEBSITE_ADMIN(admin.ModelAdmin) : 
    list_display = ("facebook" , "twitter" , "linkedin" , "github" , "youtube" )



@admin.register(Contact_us)
class Contact_us_ADMIN(admin.ModelAdmin) : 
    list_display = ("name" , "email" , "subject" , "message") 
    search_fields = ("email" , "name" , "subject" , "message") 
    fields = [("name" , "email" ) , "subject" , "message"]



@admin.register(ABOUT_WEBSITE)
class ABOUT_WEBSITE_ADMIN(admin.ModelAdmin) : 
    list_display = ("title" , "show_image" , "description")
    def show_image(self , obj ) : 
        return format_html('<img width=50px , height=50px src="{}">'.format(obj.picture.url))
    



@admin.register(INSTAGRAM_POST)
class INSTAGRAM_POST_ADMIN(admin.ModelAdmin) : 
    list_display = ("name" , "slug" , "show_image")

    def show_image(self , obj ):
        return format_html('<img width=50px , height = 50px src="{}">'.format(obj.picture.url))

    show_image.short_description = "عکس های پست های اینستاگرامی"



@admin.register(Comments_of_Post)
class Comments_of_Post_ADMIN(admin.ModelAdmin) : 
    list_display = ("name"  , "email" ,"website" , "post" , "Comments")
    search_fields = ("name" , "email" , "post" , "website" , "Comments" ) 
    list_editable = ["post" , ]



@admin.register(Post)
class Post_ADMIN(admin.ModelAdmin) :
    list_display = ("title"  , "show_image" , "author" , "category" , "status" , "show_tags" )

    def show_tags(self , obj ):
        return ' , '.join([i.name for i in obj.tags.all() ] )

    show_tags.short_description ="تگ ها "


    def show_image(self , obj ):
        return format_html('<img width=50px , height = 50px src="{}">'.format(obj.picture.url))

    show_image.short_description = "عکس سر تیتر مقاله"




@admin.register(Category_of_Post)
class Category_of_Post_ADMIN(admin.ModelAdmin) :
    list_display = ("name" , "slug" )
    prepopulated_fields = {'slug' : ('name' , )}


@admin.register(TOTAL_TAGS)
class TOTAL_TAGS_ADMIN(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {'slug': ('name',)}

