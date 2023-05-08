from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import Post
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.
def home(request):
    form = BlogPostForm(request.POST)
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('home-page')
        else:
            form = BlogPostForm()
    else:
        form = BlogPostForm()
    context = {
        'form':form
    }
    return render(request, 'app/home.html', context)

def about(request):
    if 'q' in request.GET:
        q = request.GET['q']
        posts = Post.objects.filter(title__icontains=q).order_by('-id')
    else:
        posts = Post.objects.all().order_by('-id')
        paginator = Paginator(posts, 2)
        page = request.GET.get('page')
        paged_post = paginator.get_page(page)

    context = {
        'posts':paged_post
    }
    return render(request, 'app/about.html', context)
def read(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post':post
    }
    return render(request, 'app/read.html', context)
def update(request, id):
    post = Post.objects.get(id=id)
    form = BlogPostForm(request.POST, instance=post)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('read-page',id=post.id)
        else:
            form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post)
    context = {
        'form':form,
        'post':post
    }
    return render(request, 'app/update.html', context)
def delete_view(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('about-page')

