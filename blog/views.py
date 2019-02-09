from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import EmptyPage, InvalidPage, PageNotAnInteger, Paginator

def post_list_view(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/post_list.html', {'posts': posts})


def post_detail_view(request, year, day, month, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/post_detail.html', {'post': post})