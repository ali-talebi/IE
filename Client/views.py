from django.shortcuts import render
from .models import USER_INFORMATION 
from blog.models import Post , INSTAGRAM_POST 
# Create your views here.




def Show_USER(request , id ) : 
    human = USER_INFORMATION.objects.get(id = id ) 
    content = {
        'person' : human ,
        'posts' : Post.objects.all().filter(author = human ) , 
        'len_post' : len(Post.objects.all().filter(author = human )) , 
        'instagram_posts' : INSTAGRAM_POST.objects.all() , 
    }

    return render(request , 'author-single.html' , content )


