

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post
#we can use class based views instead of function based views to list all post, TO DO THIS WE USE THE GENERIC listView
from django.views.generic import ListView

#generic class based views are used as inheritances
class PostListView(ListView):

    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blogs/post/list.html'
    '''
def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(post_list, 3)#Psginator here is an inbuilt function that takes the post_list, and a number as values(params)
    page_number = request.GET.get('page', 1) #retrieve page GET HTTP parameter and store in the pagenumber variable
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        #if the page_number request request does not include an integer
        posts = paginator.page(1)
    except EmptyPage:
        #if page_number is out of range get the last page of results given by paginator.page(page_number)
        posts = paginator.page(paginator.num_pages)
    '''
return render(
        request,
        'blogs/post/list.html',
        {'posts': posts}
    )










def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                            status=Post.Status.PUBLISHED,
                            slug=post,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    return render(request,
                 'blogs/post/detail.html',  # Changed to match your structure
                 {'post': post})