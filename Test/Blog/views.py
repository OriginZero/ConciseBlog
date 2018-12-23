from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog, BlogType
from django.conf import settings
# Create your views here.


def getPaging(request, QuerSet):
    context = {}
    # start 分页操作 start
    # 使用分页器    每6片分一页
    paginator = Paginator(QuerSet, settings.PAGINATOR_PAGE_SETTING)
    # 获取页码参数 get请求 默认参数第一页
    page_num = request.GET.get('page', 1)
    # get_page可以处理非数字的字符，如果出错返回1
    page_of_blogs = paginator.get_page(page_num)
    return page_of_blogs


def index(request):
    context = {}
    page_of_blogs = getPaging(request, QuerSet=Blog.objects.all())
    context['blog_list'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['blog_type_list'] = BlogType.objects.all()
    return render_to_response('Blog/main.html', context)


def TypeBlog(request, type_name):
    context = {}
    type_blog_list = Blog.objects.filter(
        type_blog=BlogType.objects.get(type_name=type_name))
    page_of_blogs = getPaging(request, QuerSet=type_blog_list)
    context['blog_list'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['blog_type_list'] = BlogType.objects.all()
    return render_to_response('Blog/main.html', context)


def infoBlog(request, blog_pk):
    # 获取单个博客
    blog = get_object_or_404(Blog, pk=blog_pk)
    context = {}
    context['blog'] = blog
    context['blog_type_list'] = BlogType.objects.all()
    return render_to_response('Blog/ReadBlogPage.html', context)


def search(request):
    wd = request.GET.get('wd')
    if not wd:
        return render_to_response('Blog/404.html', {'msg': '无法搜索到与之相匹配的信息，您可以尝试重新搜索'})
    search_list = Blog.objects.filter(content__icontains=wd)
    page_of_blogs = getPaging(request, QuerSet=search_list)
    context = {}
    context['blog_list'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['blog_type_list'] = BlogType.objects.all()
    return render_to_response('Blog/main.html', context)
