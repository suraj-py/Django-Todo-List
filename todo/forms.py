from django import forms

class TodoForm(forms.Form):
    task = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'placeholder': '  Add Task . . . .'}
            ))
