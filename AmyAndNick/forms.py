from django import forms
from AmyAndNick.models import Guest


YES_OR_NO = (
    (True, 'Yes'),
    (False, 'No')
)

BOOL_CHOICES = ('Yes', 'NO')

class GuestForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Your name")
    email_address = forms.EmailField(max_length=75, help_text="Your email address")
    #date = forms.DateField(widget=forms.HiddenInput(), auto_now=True)
    significant_other = forms.CharField(max_length=128, required=False, help_text="Name of significant other")
    #children = forms.IntegerField(initial=0, help_text="Number of children between the ages of 3 and 12 accompanying you")    
    #babies = forms.IntegerField(initial=0, help_text="Number of children under the age of 3")                 
    
    '''rehersal_dinner = forms.TypedChoiceField(widget=forms.Select(choices=YES_OR_NO), 
                                                                required=True, empty_value=None, coerce=bool,
                                                                help_text="Will you be attending the rehersal dinner Friday April 24th?")
    '''
    rehersal_dinner = forms.BooleanField(widget=forms.Select(choices=YES_OR_NO), required=False, initial=False,
                                help_text="Will you be attending the rehersal dinner Friday April 24th?")                           
    wedding = forms.BooleanField(widget=forms.Select(choices=YES_OR_NO), required=False, initial=False,
                                 help_text="Will you be attending the wedding ceremony Saturday April 25th?")
    brunch = forms.BooleanField(widget=forms.Select(choices=YES_OR_NO), required=False, initial=False,
                                                              help_text="Will you be attending brunch on Sunday April 26th?")
    stay_in_cabin = forms.BooleanField(widget=forms.Select(choices=YES_OR_NO), required=False, initial=False,
                                help_text="Will you be staying with us in the cabins at the YMCA?")
    #vegetarian = forms.BooleanField(widget=forms.Select(choices=YES_OR_NO), required=False, initial=False,help_text="Would you like a vegetarian meal?")
    notes = forms.CharField(max_length=256, required=False, help_text="notes:")
    #paid = forms.BooleanField(widget=forms.HiddenInput(), initial=False)
    
    # An inline class to provide additional information on the form.
    class Meta:
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        model = Guest
        #exclude= ('date', 'paid',)