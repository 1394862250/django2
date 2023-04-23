from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Post, Category


# Create your views here.


def post_detail(request, id):
    """
    新闻详情
    :param request:
    :param id: 新闻id
    :return:
    """
    post = get_object_or_404(Post, id=id)
    if post.approved or request.user.has_perm('posts.view_all_post'):
        return render(request, 'front/post.html', context={'post': post,
                                                           'categories': Category.objects.filter(parent=None)})
    else:
        raise Http404  # 隐藏未通过审核的新闻id
