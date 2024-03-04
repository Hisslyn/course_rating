from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import RateCourseForm

def rate_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        form = RateCourseForm(request.POST)
        if form.is_valid():
            new_rating = form.cleaned_data['rating']
            course.update_rating(new_rating)
            return redirect('course_detail', course_id=course.id)
    else:
        form = RateCourseForm()
    return render(request, 'courses/rate_course.html', {'course': course, 'form': form})

def course_list(request):
    courses = Course.objects.all().order_by('-rate')
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

def rate_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        try:
            new_rating = float(request.POST.get('rating', 0))
            course.update_rating(new_rating)
        except ValueError:
            # Handle the error if the input is not a valid float
            pass
        return HttpResponseRedirect(reverse('courses:course_detail', args=[course_id]))
    return render(request, 'courses/rate_course.html', {'course': course})
