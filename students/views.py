from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentForm
from .models import Student


def student_list(request):
    """Home page: show every student in the database."""
    students = Student.objects.all()
    return render(request, "students/student_list.html", {"students": students})


def student_add(request):
    """Show a blank form on GET, save it on a valid POST."""
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect("student_list")
    else:
        form = StudentForm()

    return render(request, "students/student_form.html", {"form": form, "title": "Add Student"})


def student_edit(request, pk):
    """Show the form pre-filled with the existing student on GET, update on POST."""
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)

    return render(request, "students/student_form.html", {"form": form, "title": "Edit Student"})


def student_delete(request, pk):
    """Show a confirmation page on GET, delete the record on POST."""
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect("student_list")

    return render(request, "students/student_confirm_delete.html", {"student": student})
