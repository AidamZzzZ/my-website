from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from .models import Post
from .forms import PostForm

class ListPostView(ListView):
    model = Post
    template_name = "posts/index.html"

class DetailPostView(DetailView):
    model = Post
    template_name = "posts/detail_post.html"

class CreatePostView(CreateView):
    template_name = "posts/create_post.html"
    success_url = "/"   
    model = Post
    form_class = PostForm

    def send_post(request):
        if request.method == "POST":
            form = PostForm()
            if form.is_valid():
                post = form.save()
                return redirect("/")
        else:
            form = PostForm()
        return render(request, "posts/create_post.html", {'form':form})
    
class DeletePostView(DeleteView):
    model = Post
    template_name = "posts/delete_post.html"
    success_url = "/"

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/update_post.html"
    success_url = "/"
   
        