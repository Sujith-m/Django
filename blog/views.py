from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def index(request):
    return render(request, 'blog/index.html', {})

def about_us(request):
    return render(request, 'blog/about-us.html', {})

def team(request):
    return render(request, 'blog/team.html', {})

def packages(request):
    return render(request, 'blog/packages.html', {})

def gallery(request):
    return render(request, 'blog/gallery.html', {})

def blog(request):
    return render(request, 'blog/blog.html', {})

def contact_us(request):
    return render(request, 'blog/contact-us.html', {})
