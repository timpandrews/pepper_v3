from django import forms

from journal.models import Journal, Plants


class DateInput(forms.DateInput):
    input_type = 'date'


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        widgets = {'journal_date': DateInput()}
        fields = (
            'journal_date',
            'title',
            'text',
        )


class PlantsForm(forms.ModelForm):
    class Meta:
        model = Plants
        fields = (
            'title',
            'description',
        )

