from django.shortcuts import render


# Create your views here.
def profiles(request):
    context = {}
    return render(request, 'users/profile.html', context)