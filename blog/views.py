from django.shortcuts import render
from .models import Post , TOTAL_TAGS , Category_of_Post  , INSTAGRAM_POST 
from Client.models import USER_INFORMATION 
from .forms import SEND_COMMENT , SEND_CONTACT 
from .models import ABOUT_US_MODEL , Comments_of_Post , ABOUT_WEBSITE , Contact_us , SOCIAL_MEDIA_WEBSITE 
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage 

# Create your views here.







def Home(request) :




    content = {
        'posts' :  Post.objects.all() , 
        'total_tags' : TOTAL_TAGS.objects.all() , 
        'recent_posts' : Post.objects.all().order_by("-created")[:5] , 
        'authors' : USER_INFORMATION.objects.all() , 
        'categories' : Category_of_Post.objects.all() , 
        'instagram_posts' : INSTAGRAM_POST.objects.all() , 
        'about_website' : ABOUT_WEBSITE.objects.first() ,
        'social_media_website' :  SOCIAL_MEDIA_WEBSITE.objects.first() , 
        'trend_post' : Post.objects.filter(status_location = 'TRENDING POST' )[:3] ,
        'populated_post' : Post.objects.filter(status_location = 'POPULAR POST' ).first(), 
        'editor_pick' :  Post.objects.filter(status_location = 'EDITORS Pick').first(), 


    }
    return render(request , 'index.html' , content )



def SELECT_TAGS(request , tag  ) : 
    content = {
        'posts' : Post.objects.filter(tags__slug = tag ) , 
        'about_website' : ABOUT_WEBSITE.objects.first() ,
        'total_tags' : TOTAL_TAGS.objects.all() , 
        'social_media_website' :  SOCIAL_MEDIA_WEBSITE.objects.first() , 
        'authors' : USER_INFORMATION.objects.all() , 
        'categories' : Category_of_Post.objects.all() , 
        'recent_posts' : Post.objects.all().order_by("-created")[:5] ,
        'tag' : TOTAL_TAGS.objects.all().filter(slug = tag ).first() , 
        'instagram_posts' : INSTAGRAM_POST.objects.all() , 

    }

    return render(request , 'SELECT_TAGS.html' , content )




def SELECT_CATEGORY( request , category   ) : 

    content = {
        'posts'  : Post.objects.filter(category__slug = category ) , 
        'total_tags' : TOTAL_TAGS.objects.all() , 
        'social_media_website' :  SOCIAL_MEDIA_WEBSITE.objects.first() , 
        'authors' : USER_INFORMATION.objects.all() , 
        'categories' : Category_of_Post.objects.all() , 
        'recent_posts' : Post.objects.all().order_by("-created")[:5] ,
        'category_name' :  Category_of_Post.objects.all().filter(slug = category).first() , 
        'about_website' : ABOUT_WEBSITE.objects.first() ,
        'instagram_posts' : INSTAGRAM_POST.objects.all() , 

        

    }
    return render(request , 'SELECT_CATEGORY.html' , content )


def Read_Post(request , id ) : 
    post_now = Post.objects.get(id = id ) 

    if request.method == "POST" : 
        form1 = SEND_COMMENT(request.POST)
        if form1.is_valid() : 
            new_name = form1.cleaned_data["name"]
            new_email = form1.cleaned_data["email"]
            new_website = form1.cleaned_data["website"]
            new_Comments = form1.cleaned_data["Comments"]

            new_comment = Comments_of_Post(post = post_now , Comments = new_Comments , name = new_name , email = new_email , website = new_website  )
            new_comment.save() 

    content = {
        'read_post' : post_now , 
        'comments'  :  Comments_of_Post.objects.all().filter(post = post_now ).order_by("-time"), 
    }

    return render(request , 'post-details.html' , content  )



def CONTACT_US(request) : 

    if request.method == "POST" : 
        form2 = SEND_CONTACT(request.POST) 

        if form2.is_valid() : 
            new_name = form2.cleaned_data["name"] 
            new_email = form2.cleaned_data["email"]
            new_subject = form2.cleaned_data["subject"]
            new_message = form2.cleaned_data["message"]

            model = Contact_us(name = new_name , email = new_email , subject = new_subject , message = new_message )
            model.save() 





        
    content = {
        'instagram_posts' : INSTAGRAM_POST.objects.all() ,
        
    }
    return render(request , 'contact.html' , content )




def ABOUT_WEBSITE_DESCRIPTION(request) : 
    content = {
        'instagram_posts' : INSTAGRAM_POST.objects.all() ,  
        'social_media_website' :  SOCIAL_MEDIA_WEBSITE.objects.first() ,
        'ABOUT_US_MODEL' : ABOUT_US_MODEL.objects.first() , 
        'instagram_posts' : INSTAGRAM_POST.objects.all() ,

    }

    return render(request , 'about-us.html' , content )



def TOTAL_USER(request) : 
    users = USER_INFORMATION.objects.all()
    print(users)
    content = {
        'TOTAL_USER':USER_INFORMATION.objects.all() ,
        'instagram_posts' :  INSTAGRAM_POST.objects.all() , 
        'instagram_posts' : INSTAGRAM_POST.objects.all() ,
    }
    return render(request , 'author.html' , content )



def SEARCH_WEBSITE(request) : 

    if request.method == "GET" : 
        q = request.GET.get("text") 

    posts = Post.objects.all().filter(title__icontains = q )


    if len(posts) : 
        name_template = 'search-result.html'
    else : 
        name_template = "search-not-found.html"

    return render(request , name_template  , {'posts' : posts , 'q' :q , 'instagram_posts' : INSTAGRAM_POST.objects.all() })


def custom_404(request, exception):

    return render(request, '404.html', {'instagram_posts' : INSTAGRAM_POST.objects.all() } , status=404 ) 