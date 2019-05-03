from django.shortcuts import render
from .models import Feeds
# Create your views here.
def home(request):
    if request.method == 'POST':
        if request.POST.get('feed_entered'):
            post = Feeds()
            post.feed = request.POST.get('feed_entered')
            post.save()
    return render(request, 'home.html')
