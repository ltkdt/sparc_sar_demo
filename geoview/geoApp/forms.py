from django import forms

# Create custom widget in your forms.py file.
class DateInput(forms.DateInput):
    input_type = 'date'

class LastActiveForm(forms.Form):
    """
    Last Active Date Form
    """
    start_active = forms.DateField(widget=DateInput, label="Start Date")
    end_active = forms.DateField(widget=DateInput, label="End Date")