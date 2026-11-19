from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    """ModelForm auto-generates form fields from the Student model."""

    class Meta:
        model = Student
        fields = ["name", "email", "age", "course"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. John Doe"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "e.g. john@example.com"}),
            "age": forms.NumberInput(attrs={"class": "form-control", "placeholder": "e.g. 20"}),
            "course": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Computer Science"}),
        }
