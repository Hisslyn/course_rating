from django import forms

class RateCourseForm(forms.Form):
    rating = forms.FloatField(min_value=0.0, max_value=5.0, help_text="Enter a rating between 0 and 5")
