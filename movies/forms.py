from django import forms
from .models import MovieReview

class MovieReviewForm(forms.ModelForm):
    # Cambiar el campo de ChoiceField a IntegerField
    rating = forms.IntegerField(label='Rating', min_value=0, max_value=100)

    class Meta:
        model = MovieReview
        fields = ['rating', 'review']
