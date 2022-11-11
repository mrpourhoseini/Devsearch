from django.shortcuts import render
from users.models import Profile


# Create your views here.
def profiles(request):
    profiles_obj = Profile.objects.all()
    context = {'profiles': profiles_obj}
    return render(request, 'users/profiles.html', context)


def profile(request, username):
    profile_obj = Profile.objects.get(username=username)
    top_skills = profile_obj.skill_set.exclude(description__exact="")
    other_skills = profile_obj.skill_set.filter(description="")

    context = {
        "profile": profile_obj,
        "topSkills": top_skills,
        "otherSkills": other_skills
    }
    return render(request, 'users/profile.html', context)
