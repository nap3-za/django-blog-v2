from django import forms
from .models import Article


status_choices = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)


class UpdateForm(forms.Form):

    title = forms.CharField(label='')
    page_title = forms.CharField(max_length=249, label='')
    content = forms.CharField(label='', widget=forms.Textarea())
    sum = forms.CharField(label='')
    status = forms.ChoiceField(label='', choices=status_choices)


    def clean_title(self):
        data = self.cleaned_data.get("title")
        
        return data
    
        
    def clean_page_title(self):
        data = self.cleaned_data.get("page_title")
        
        return data
    
    def clean_content(self):
        data = self.cleaned_data.get("content")
        
        return data
    
    def clean_status(self):
        data = self.cleaned_data.get("status")
        
        return data

    def clean_sum(self):
        data = self.cleaned_data["sum"]
        
        return data
    


class AddArticleForm(forms.Form):

    title = forms.CharField(label='')
    page_title = forms.CharField(max_length=249, label='')
    content = forms.CharField(label='', widget=forms.Textarea())
    sum = forms.CharField(label='')  
    status = forms.ChoiceField(label='', choices=status_choices)



    def clean_title(self):
        data = self.cleaned_data.get("title")
        
        return data
    
        
    def clean_page_title(self):
        data = self.cleaned_data.get("page_title")
        
        return data
    
    def clean_content(self):
        data = self.cleaned_data.get("content")
        
        return data
    
    def clean_status(self):
        data = self.cleaned_data.get("status")

        return data

    def clean_sum(self):
        data = self.cleaned_data["sum"]
        
        return data
    
    
        
