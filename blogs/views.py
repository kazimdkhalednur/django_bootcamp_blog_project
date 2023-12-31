from django.shortcuts import render, get_object_or_404
from .models import Blog
from .forms import ContactForm


def home(request):
    blogs = Blog.objects.all()

    context = {
        "title": "Blog",
        "blogs": blogs
    }

    return render(request, "blogs/index.html", context)


def about(request):
    context = {
        "title": "About"
    }
    return render(request, "blogs/about.html", context)


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            context = {
                "title": "Contact",
                "form": ContactForm(),
                "success": True
            }
            return render(request, "blogs/contact.html", context)
    context = {
        "title": "Contact",
        "form": form
    }
    return render(request, "blogs/contact.html", context)


def post(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {
        "title": "Post",
        "blog": blog
    }
    return render(request, "blogs/post.html", context)
