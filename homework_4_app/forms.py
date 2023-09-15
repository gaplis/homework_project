from django import forms


class ChangeProductForm(forms.Form):
    pk = forms.IntegerField(min_value=1)
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    price = forms.FloatField()
    count = forms.IntegerField(min_value=1)


class ImageForm(forms.Form):
    pk = forms.IntegerField(min_value=1)
    image = forms.ImageField()