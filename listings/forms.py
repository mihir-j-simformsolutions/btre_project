from django import forms 
  

from .models import Listing 
  
# create a ModelForm 
class ListingForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Listing 
        fields = "__all__"