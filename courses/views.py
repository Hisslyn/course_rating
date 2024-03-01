from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from django.http import HttpResponseRedirect

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
        return redirect('course_detail', course_id=course_id)
    return render(request, 'courses/rate_course.html', {'course': course})