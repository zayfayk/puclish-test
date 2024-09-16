from django import forms
from .models import Customer,Category


choices= Category.objects.all().values_list('customer_country_catalog','customer_country_catalog')

choices_list=[]

for item in choices:
    choices_list.append(item)
class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields =  fields = ('author','name', 'last_name', 'number', 'country','category', 'city', 'situation' )
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'faysa','type':'hidden'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices_list,attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'situation': forms.Textarea(attrs={'class': 'form-control'}),
            
        }
class CustomerEdit(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ('name', 'last_name', 'number', 'country', 'city', 'situation')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'situation': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }
