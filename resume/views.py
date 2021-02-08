from django.shortcuts import render, get_object_or_404
from .models import Post
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm
from django.core.mail import send_mail


def home(request):
    return render(request, 'home2.html',{} )

def hobbies(request):
    return render(request, 'hobbies.html',{} )

def about_me(request):
    return render(request, 'about_me.html',{} )

def website(request):
    return render(request, 'website.html',{} )
    
def contact(request):
    return render(request, 'contact.html',{} )


def back(request):
    return render(request, 'back-end.html',{} )


def blog(request):
    return render(request, 'blog.html',{} )



def post_detail(request, year, month, day, post):
    print(request)
    post = get_object_or_404(Post, slug = post, status = 'published', publish__year = year, publish__month = month, publish__day = day)
    print(post)
    template = 'blog_detail.html'
    context = {'post': post}
    return render(request, template, context)


def mail(request):
    sent = False
    if request.method == 'POST':
        # Formularz został wysłany.
        form = EmailPostForm(request.POST)
        if form.is_valid():
        # Weryfikacja pól formularza zakończyła się powodzeniem...
            cd = form.cleaned_data
            dane = 'Została wysłana wiadomość z servera DJANGO od urzytkownika {} o adresie email  {}   OK.  '.format(cd['name'],cd['email']) 
        # ... więc można wysłać wiadomość e-mail.
            send_mail(dane, cd['notice'], '2021resumecv@gmail.com', ['2021resumecv@gmail.com'])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'contact.html', {'form': form, 'sent':sent})

def skills(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 3) # Trzy posty na każdej stronie.
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'page': page, 'posts': posts, 'tag':tag}
    return render(request, 'skills.html', context )