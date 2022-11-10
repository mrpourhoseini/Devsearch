from django.shortcuts import render
from users.models import Profile


# Create your views here.
def profiles(request):
    profiles_obj = Profile.objects.all()
    context = {'profiles': profiles_obj}
    return render(request, 'users/profiles.html', context)


def profile(request, username):
    profile_obj = Profile.objects.get(username=username)
    context = {"profile": profile_obj}
    return render(request, 'users/profile.html', context)
