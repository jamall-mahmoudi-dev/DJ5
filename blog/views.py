from django.shortcuts import render
from website.forms import PostModelForm
from django.shortcuts import render, redirect
from django.contrib import messages
from website.models import Posts
# Create your views here.

def blog_home(request):
    return render(request, 'blog/blog-home.html')


def blog_single(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            # چاپ کن ببینم داده میاد یا نه
            print("Form is valid")
            print(form.cleaned_data)
            
            post = form.save()
            print("Post saved:", post.id)  # چاپ کن ببینم ذخیره شد یا نه
            
            messages.success(request, 'کامنت شما با موفقیت ثبت شد!')
            return redirect('blog:blog_single')
        else:
            # چاپ کن ببینم خطا چی هست
            print("Form errors:", form.errors)
            messages.error(request, f'خطا: {form.errors}')
    else:
        form = PostModelForm()
    
    comments = Posts.objects.all().order_by('-created_at')
    return render(request, 'blog/blog-single.html', {
        'form': form,
        'comments': comments
    })
    
    
'''def blog_single(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
    form = PostModelForm()
        
    return render(request, 'blog/blog-single.html', {'form': form})'''