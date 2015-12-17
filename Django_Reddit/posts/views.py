from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.views import generic
from django.core.urlresolvers import reverse


from .forms import PostCreationForm

from .models import Post,Comment
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_posts_list'

    latest_posts_list = Post.objects.order_by('post_creation_time')[:5]
    print latest_posts_list
    retur



def detail(request,post_id):
    return HttpResponse("You are looking at the post %s." %post_id)

def addNewPost(request):
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['post_header']
            body = form.cleaned_data['post_body']

            q = Post(post_header=title,post_text=body);
            print q.post_header
            print q.post_text
            print q.id
            q.save()

            return HttpResponseRedirect('/posts/')
    else:
        form = PostCreationForm()

    return render(request,'addPost.html',{'form':form})


