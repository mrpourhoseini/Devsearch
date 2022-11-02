from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


# Create your views here.

def projects_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    context = {'project': project_obj}
    return render(request, 'project.html', context)


def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'project_form.html', context)


def update_project(request, pk):
    project_form = Project.objects.get(id=pk)
    form = ProjectForm(instance=project_form)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project_form)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'project_form.html', context)


def delete_project(request, pk):
    project_obj = Project.objects.get(id=pk)
    if request.method == 'POST':
        project_obj.delete()
        return redirect('projects')
    context = {'object': project_obj}
    return render(request, 'delete_project.html', context)
