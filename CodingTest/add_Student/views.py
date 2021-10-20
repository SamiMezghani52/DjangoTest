from django.shortcuts import render, redirect

from . import models
from .filters import LineFilter

def displayClasses(request):
    if request.method == "GET":
       lines = models.Lines.objects.all()
       context = {
           'filter': LineFilter(request.GET, queryset=lines),
           'lines': lines
       }
    return render(request, 'display_page.html', context)

def addLine(request):
    school_list = models.School.objects.all()

    if request.method == 'POST':
        school = request.POST.get('school')
        level = request.POST.get('level')
        classroom = request.POST.get('classroom')
        print(classroom)
        description = request.POST.get('description')

        line = models.Lines(
            school= models.School.objects.get(Name=school),
            level = models.Level.objects.get(level=level),
            classroom = models.Classroom.objects.get(classroom=classroom),
            description= description
        )
        if line:
            line.save()
            return redirect('classes-list')
    return render(request, "add_page.html", {'schools': school_list})

def load_levels(request):
    school = request.GET.get('school_id')
    id_school = models.School.objects.get(Name=school).id
    levels = models.Level.objects.filter(school_id=id_school)
    context ={
        'levels': levels,
    }
    return render(request, 'levels_dropdown_list.html', context)

def load_classes(request):
    level = request.GET.get('level')
    print(level)
    id_level = models.Level.objects.get(level=level).id
    classes = models.Classroom.objects.filter(level=id_level)
    
    context ={
        'classes': classes
    }
    return render(request, 'clases_dropdown_list.html', context)
