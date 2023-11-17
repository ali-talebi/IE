from django.db import models
from Client.models import USER_INFORMATION
from ckeditor.fields import  RichTextField
from django.utils import timezone
from django.urls import reverse 

# Create your models here.


class SOCIAL_MEDIA_WEBSITE(models.Model) : 
    facebook = models.CharField(verbose_name="فیسبوک" , max_length=100 , null = True , blank = True )
    twitter = models.CharField(verbose_name="توئیتر" , max_length=100 , null = True , blank = True )
    linkedin = models.CharField(verbose_name="لینکدین" , max_length=100 , null = True , blank = True )
    github = models.CharField(verbose_name="گیتهاب" , max_length=100 , null = True , blank = True )
    youtube = models.CharField(verbose_name="یوتیوب" , max_length=100 , null = True , blank = True )



    def __str__(self) : 
        return "شبکه های اجتماعی وبسایت"
    
    class Meta : 
        db_table = "SOCIAL_MEDIA_WEBSITE"
        verbose_name_plural = "شبکه های اجتماعی وبسایت مهندسی صنایع"


class Post(models.Model) :
    STATUS_LEVEL = (
        ("P"  , "منتشر شدن") ,
        ("D"  ,  "پیش نویس شدن" )
    )

    STATUS_LOCATION_PICK = (
        ('EDITORS Pick' , 'منتخب نویسنده' ) , 
        ('TRENDING POST' , 'پست برتر' ) , 
        ('POPULAR POST' , 'پست محبوب' ) 
    )

    picture = models.FileField(verbose_name="عکس سر تیتر " , upload_to="Post_Image/" , null = True )
    picture2 = models.FileField(verbose_name="عکس 2 " , upload_to="Post_Image/" , null = True , blank= True )
    title = models.CharField(verbose_name="عنوان پست " , max_length=200 )
    text  = RichTextField(verbose_name= "متن " )
    created = models.DateTimeField(verbose_name="زمان انتشار" , auto_now=False , auto_now_add= True )
    status = models.CharField(verbose_name="وضعیت پست " , max_length=1 , choices=STATUS_LEVEL  , default= "D")
    author = models.ForeignKey(USER_INFORMATION , verbose_name= "نویسنده" , on_delete=models.CASCADE , null= True )
    category = models.ForeignKey("Category_of_Post" ,verbose_name="دسته بندی مقالات " , on_delete=models.CASCADE   )
    tags = models.ManyToManyField("TOTAL_TAGS")
    time_to_read = models.IntegerField(verbose_name="مدت زمان لازم برای خواندن پست " , null= True )

    status_location = models.CharField(verbose_name="وضعیت پست از نظر محل" , null=True , max_length=20 , choices=STATUS_LOCATION_PICK )




    def __str__(self):
        return self.title

    class Meta :
        db_table = "Post"
        verbose_name_plural = "پست های نوشته شده "


    def get_absolute_url(self ) : 
        return reverse('BLOG:Read_Post' , args=[str(self.id)])


class Category_of_Post(models.Model) :
    name = models.CharField(verbose_name=  "اسم دسته بندی" , max_length=50 )
    slug = models.SlugField(verbose_name= "آدرس دسته بندی" , unique= True )


    def __str__(self):
        return self.name

    class Meta :
        db_table = "Category_of_Post"
        verbose_name_plural = "دسته بندی های پست ها "






class TOTAL_TAGS(models.Model) :

    name = models.CharField(verbose_name="اسم تگ "  , max_length= 50 )
    slug = models.SlugField(verbose_name= "آدرس اینترنتی تگ ها " , unique= True )


    def __str__(self):
        return  self.name


    class Meta :
        db_table = "TOTAL_TAGS"
        verbose_name_plural = "تگ های دسته بندی ها "



class Comments_of_Post(models.Model) : 
    post = models.ForeignKey(Post , verbose_name="پست " , on_delete=models.CASCADE , null = True )
    Comments = models.TextField(verbose_name="کامنت"  )
    name = models.CharField(verbose_name="نام و نام خانوادگی" , max_length=100 ) 
    email = models.EmailField(verbose_name="ایمیل" )
    website = models.CharField(verbose_name="آدرس وبسایت " , max_length=50 , null = True )
    time = models.DateTimeField(verbose_name="زمان ساخت" , auto_now= True , auto_now_add= False , null = True ) 

    def __str__(self) :
        return self.name 
    
    class Meta : 
        db_table = "Comments"
        verbose_name_plural = "کامنت های پست ها " 

    


class INSTAGRAM_POST(models.Model) : 
    name = models.CharField(verbose_name="نام پست اینستاگرامی"  , max_length= 50 ) 
    picture = models.FileField(verbose_name="عکس پست های اینستاگرامی" , upload_to="Instagram_Posts_Image/"  )
    slug = models.SlugField(verbose_name="آدرس پست اینستاگرامی" )
    def __str__(self) -> str:
        return self.name 
    

    class Meta : 
        db_table = "INSTAGRAM_POST"
        verbose_name_plural = "پست های اینستاگرامی"





class ABOUT_WEBSITE(models.Model) : 
    title = models.CharField(verbose_name="عنوان" , max_length= 30 )
    picture = models.FileField(verbose_name="عکس" , upload_to="ABOUT_WEBSITE_IMAGE/") 
    description = models.TextField(verbose_name="توضیحات" )


    def __str__(self) -> str:
        return self.title 
    

    class Meta : 
        db_table = "ABOUT_WEBSITE"
        verbose_name_plural = "توضیحات وبسایت"
        


class Contact_us(models.Model) : 
    name = models.CharField(verbose_name="نام و نام خانوادگی" , max_length=100 ) 
    email = models.EmailField(verbose_name="ایمیل" ) 
    subject = models.CharField(verbose_name="موضوع پیام" , max_length=200)
    message = models.TextField(verbose_name="متن پیام"  )


    def __str__(self) : 
        return self.name 
    

    class Meta : 
        db_table = "Contact_us"
        verbose_name_plural = "ارتباط با ما "




class ABOUT_US_MODEL(models.Model) : 
    main_mission_mine_title = models.CharField(verbose_name="عنوان متن " , max_length=100 )
    text1 = models.TextField(verbose_name="متن " )
    picture1 = models.FileField(verbose_name="عکس 1 " , upload_to="ABOUT_US_PICTURE_IMAGE/" ) 
    title2 = models.CharField(verbose_name="عنوان 2 " , max_length= 100 , null = True )
    main_mission_of_company1 = models.CharField(verbose_name="1عنوان" , max_length= 50 ) 
    text_main_mission_of_company1 = models.TextField(verbose_name="1متن ماموریت کمپانی" ) 


    main_mission_of_company2 = models.CharField(verbose_name="2عنوان" , max_length= 50 ) 
    text_main_mission_of_company2 = models.TextField(verbose_name="2متن ماموریت کمپانی" , null = True  ) 


    main_mission_of_company3 = models.CharField(verbose_name="3عنوان" , max_length= 50 ) 
    text_main_mission_of_company3 = models.TextField(verbose_name="3متن ماموریت کمپانی" ) 



    great_tem_title = models.CharField(verbose_name="عنوان" , max_length=100 ) 
    text_great_team = models.TextField(verbose_name="متن تیم" )
    picture_great_team = models.FileField(verbose_name="عکس تیم" , upload_to="PICTURE_GREAT_TEAM_IMAGE/") 

    text4 = models.CharField(verbose_name="متن سابسکرایب " , max_length= 100 , null = True ) 

    title5 =  models.CharField(verbose_name="عنوان 5" , max_length= 100 , null = True   ) 
    text_5 = models.TextField(verbose_name='متن 5 '  , null= True )

    def __str__(self) : 
        return "درباره تیم ما"
    

    class Meta : 
        db_table = "ABOUT_US_MODEL"
        verbose_name_plural = "درباره تیم ما "


    