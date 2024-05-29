from django import forms

from . models import item

CLASS_FORMAT = 'w-full py-4 px-6 rounded-xl bg-gray-100'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['category','name', 'description', 'price', 'image']
        
        widgets = {
            'category': forms.Select(attrs={
                'class' : CLASS_FORMAT
            }), 
            'name' : forms.TextInput(attrs={
                'class' : CLASS_FORMAT
            }),
            'description' : forms.Textarea(attrs={
                'class' : CLASS_FORMAT
            }),
            'price' : forms.TextInput(attrs={
                'class' : CLASS_FORMAT
            }),
            'image' : forms.FileInput(attrs={
                'class' : CLASS_FORMAT
            })
        }