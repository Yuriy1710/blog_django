from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy



class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article-details.html'
    
    
class AddPostView(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'add-post.html'
    
    
class UpdatePostView(UpdateView):
    form_class = UpdateForm
    model = Post
    template_name = 'update-post.html'
  
    
# class DeletePostView(DeleteView):
#     model = Post
#     template_name = 'delete-post.html'
#     success_url = reverse_lazy('home')

def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('home')