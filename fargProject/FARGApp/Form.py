from . import views
from . import models
from django import forms



class beneficiaryForm(forms.ModelForm):
    class Meta:
        model = BeneficialModel
        fields = ('id','name','gender','address','province','district','sector','cell')


class hospitalForm(forms.ModelForm):
    class Meta:
        model = hospitalModel
        fields = ('hospital_id','hospital_name','address')

class AgentForm(forms.ModelForm):
    class Meta:
        model = AgentModel
        fields = ('Agent_id','Agent_Username','dataJoined','hospital')


class PharomacyForm(forms.ModelForm):
    class Meta:
        model = PharomacyModel
        fields = ('Pharmacy_id','PharmacyName','address')


class pharmacistForm(forms.ModelForm):
    class Meta:
        model = pharmacistModel
        fields = ('pharmacist_id','pharmacist_Username','dataJoined','Pharomacy')

class TransferForm(forms.ModelForm):
    class Meta:
        model = TransferModels
        fields = ('Transfer_id','transferName','deases','address','hospital','Beneficial','Agent')


class hospitalCertificateForm(forms.ModelForm):
    class Meta:
        model = hospitalCertificate
        fields = ('certID','certTitle','certDate','TransiderName','Beneficial','hospital','Agent')




class PharomacyCertificateForm(forms.ModelForm):
    class Meta:

        model = PharomacyCertificate
        fields = ('certID','certTitle','certDate','Beneficial','Pharomacy','pharmacist','Price','drungDetails')



#class LonginForm(forms.Form):
    #class="un " type="text" align="center" placeholder="Username"
    #<input class="pass" type="password" align="center" placeholder="Password">
    # userName22=forms.TextInput(attrs={'class':'un','type':'text','align':'center','placeholder':'Username'})
     #Password=forms.PasswordInput(attrs={'class':'pass','type':'password','align':'center','placeholder':'Password'})
