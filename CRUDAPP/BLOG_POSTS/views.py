from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import BlogPost
from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = "__all__"

def listview(request):
    blogs = BlogPost.objects.all()
    return render(request, 'BLOG_POSTS/POST_LIST.html', {'blog_list':blogs})

def blogread(request,pk):
    blog = get_object_or_404(BlogPost,pk=pk)
    return render(request, 'BLOG_POSTS/POST_READ.html', {'blog':blog})

def blogupdate(request,pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('listview')
    return render(request, 'BLOG_POSTS/POST_FORM.html', {'form':form})

def blogdelete(request,pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    if request.method=="POST":
        blog.delete()
        return redirect('listview')
    return render(request,'BLOG_POSTS/POST_DELETE.html',{'blog':blog})

def blogcreate(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listview')
    return render(request,'BLOG_POSTS/POST_FORM.html', {'form':form})