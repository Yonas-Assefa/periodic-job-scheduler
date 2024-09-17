from django import forms
from .models import Job, Script

class JobForm(forms.ModelForm):
    schedule_days = forms.MultipleChoiceField(
        choices=Job.WEEKDAYS,
        widget=forms.CheckboxSelectMultiple,  
    )

    class Meta:
        model = Job
        fields = ['name', 'description', 'schedule_days', 'schedule_time']
        widgets = {
            'schedule_time': forms.TimeInput(attrs={'type': 'time'}),
        }


class ScriptForm(forms.ModelForm):
    class Meta:
        model = Script
        fields = ['script_name', 'content', 'table_name', 'order_exec', 'import_enabled']
        widgets = {
            'content': forms.HiddenInput(),  # Use HiddenInput to hide the text area and include the Ace Editor content
            'order_exec': forms.NumberInput(attrs={'class': 'form-control', 'style': 'max-width: 80px;'}),
        }

ScriptFormSet = forms.inlineformset_factory(Job, Script, form=ScriptForm, extra=1, can_delete=True)
