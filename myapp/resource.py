from import_export import resources
from .models import attendance,Production
 
class attendanceResource(resources.ModelResource):
    class Meta:
        model = attendance

class ProductionResource(models.ModelResource):
    class Meta:
        model = Production
