from django import forms
from . models import ScriptInfo,UserInfo,BuyInfo,SellInfo, PlaceInfo
class Scriptform(forms.ModelForm):
    class Meta:
        model = ScriptInfo
        fields ='__all__'

class Userform(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserInfo
        fields ='__all__'
class Buyform(forms.ModelForm):
    class Meta:
        model = BuyInfo
        fields ='__all__'
    def __init__(self,*args,**kwargs):
        super(Buyform,self).__init__(*args,**kwargs)
        self.fields['ScriptName'].empty_label='--Select--'
    def __init__(self,*args,**kwargs):
        super(Buyform,self).__init__(*args,**kwargs)
        self.fields['UserName'].empty_label='--Select--'
class Sellform(forms.ModelForm):
    class Meta:
        model = SellInfo
        fields ='__all__'
    def __init__(self,*args,**kwargs):
        super(Sellform,self).__init__(*args,**kwargs)
        self.fields['ScriptName'].empty_label='--Select--'
    def __init__(self,*args,**kwargs):
        super(Sellform,self).__init__(*args,**kwargs)
        self.fields['UserName'].empty_label='--Select--'


class Placeform(forms.ModelForm):
    class Meta:
        model = PlaceInfo
        fields ='__all__'