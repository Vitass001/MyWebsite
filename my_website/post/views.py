from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from post.models import Post
from post.forms import PostForms
from django.contrib import messages


def home_page(request):
    return render(request, 'post/home_page.html')


# def post_create(request):
#     return render(request, 'post/post_create.html')


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForms(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Successful created!!!')
        return HttpResponseRedirect(instance.get_absolute_url())
    content = {
        'title': 'post create',
        'form': form
    }
    return render(request, 'post/post_create.html', content)


# def posts_list(request):
#     # queryset = Post.objects.all()
#     # context = {
#     #     'object_list': queryset,
#     #     'title': 'Posts list'
#     # }
#     # return render(request, 'post/posts_list.html', context)
#     pass
#     return render(request, 'post/posts_list.html')

def posts_list(request):
    queryset = Post.objects.all()
    paginator = Paginator(queryset, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'object_list': queryset,
        'title': 'Posts list',
        'page_request_var': page_request_var
    }
    return render(request, 'post/posts_list.html', context)



def post_delete(request):
    return render(request, 'post/post_delete.html')


def post_update(request):
    return render(request, 'post/post_update.html')

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': 'Posts detail',
        'object': instance,
    }
    return render(request, 'post/post_detail.html', context)


def about(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset,
        'title': 'about',

    }
    return render(request, 'post/about.html', context)


def contact(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset,
        'title': 'Content',

    }
    return render(request, 'post/contact.html', context)


