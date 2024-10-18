from django.shortcuts import render, redirect, get_object_or_404
from .models import Post  # Assuming you have a Post model defined
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required  # Ensures that only authenticated users can create a post
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)  # Use your form here
        if form.is_valid():
            post = form.save(commit=False)  # Create a Post instance but don't save to DB yet
            post.author = request.user  # Set the author to the logged-in user
            post.save()  # Now save the post to the database
            return redirect('post_list')  # Redirect after successful creation
    else:
        form = PostForm()  # Create a new form instance for GET requests

    return render(request, 'blog/post_create.html', {'form': form})

@login_required  # Ensures that only authenticated users can delete a post
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()  # Delete the post
        return redirect('post_list')  # Redirect to the post list after deletion
    return render(request, 'blog/post_delete.html', {'post': post})

@login_required  # Ensures that only authenticated users can edit a post
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Get the specific post to edit
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # Bind the form with the post instance
        if form.is_valid():
            form.save()  # Save the edited post
            return redirect('post_list')  # Redirect after successful edit
    else:
        form = PostForm(instance=post)  # Create a form instance for GET requests with existing post data

    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})  # Render the edit form
