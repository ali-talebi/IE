from django.db import models
from django.urls import reverse 

# Create your models here.


class USER_INFORMATION(models.Model) :
    picture = models.FileField(verbose_name=  "عکس " , upload_to="USER_INFORMATION_Image/" )
    name = models.CharField(verbose_name= "نام و نام خانوادگی" , max_length=100 )
    Email = models.EmailField(verbose_name=  "ایمیل" , unique=True )
    password = models.CharField(verbose_name=  "رمز کاربر" , max_length=12 )

    about_user = models.TextField(verbose_name="معرفی فیلد های کاری و از اینجور حرف ها " , null= True )

    face_book = models.CharField(verbose_name="فیسبوک" , null = True , blank = True , max_length=50 )
    twitter = models.CharField(verbose_name="توئیتر" , null = True , blank = True , max_length=50)
    github = models.CharField(verbose_name="گیت هاب" , null = True , blank = True , max_length=50)
    instagram = models.CharField(verbose_name="اینستاگرام" , null = True , blank = True , max_length=50 )


    def get_absolute_url(self) : 
        return reverse('CLIENT:Show_USER' , args=[str(self.id)])

    def __str__(self):
        return self.name

    class Meta :
        db_table = "USER_INFORMATION"
        verbose_name_plural = "اطلاعات کاربران سایت"




