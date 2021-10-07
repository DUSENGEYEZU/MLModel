from django.contrib import admin

# Register your models here.
from django.contrib import admin
# registor different models
from .models import BeneficialModel,hospitalModel,AgentModel,PharomacyModel,pharmacistModel,TransferModels,hospitalCertificate,PharomacyCertificate


admin.site.register(BeneficialModel)
admin.site.register(hospitalModel)
admin.site.register(AgentModel)
admin.site.register(PharomacyModel)
admin.site.register(pharmacistModel)
admin.site.register(TransferModels)
admin.site.register(hospitalCertificate)
admin.site.register(PharomacyCertificate)



# changing intrface of admin page
# changing intrface of admin page
admin.site.site_header = "FARG HEALTH CARE MANAGEMENT SYSTEM"
admin.site.site_url = "http://127.0.0.1:8000/FARGApp/"
