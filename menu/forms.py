from django import forms 

# LIST_QD = [(i, str(i)) for i in range(1,10)]

# class cardAddForm(forms.Form):
#     quantity = forms.TypedChoiceField(choices=LIST_QD)


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    comment = forms.CharField(widget=forms.Textarea, required=True)
