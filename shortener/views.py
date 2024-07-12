from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import URLForm
import string, random

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url_instance = form.save(commit=False)
            url_instance.short_url = generate_short_url()
            url_instance.save()
            return render(request, 'shortener/success.html', {'short_url': url_instance.short_url, 'original_url': url_instance.original_url})
    else:
        form = URLForm()
    return render(request, 'shortener/home.html', {'form': form})

def redirect_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.original_url)
