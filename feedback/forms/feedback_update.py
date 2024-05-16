from django import forms
from feedback.models import Feedback

class FeedbackUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    

    class Meta:
        model = Feedback
        fields = ['status']

