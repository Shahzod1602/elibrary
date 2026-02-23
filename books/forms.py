from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Kitob haqida fikringizni yozing...',
                'class': 'form-control',
            }),
        }


class SearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Kitob nomi, muallif yoki ISBN qidiring...',
            'class': 'form-control form-control-lg',
        })
    )
    category = forms.IntegerField(required=False, widget=forms.HiddenInput())
    language = forms.CharField(required=False)
    year_from = forms.IntegerField(required=False)
    year_to = forms.IntegerField(required=False)
    sort = forms.CharField(required=False)
