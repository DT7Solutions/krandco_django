# resources.py
# from import_export import resources, fields
# from .models import Productitem

# class ProductItemResource(resources.ModelResource):
#     class Meta:
#         model = Productitem
#         fields = ('Title', 'Image1', 'CropYear', 'Type', 'Grade', 'From', 'Nic', 'Sug', 'Packing', 'Quantity')
#         import_id_fields = ['Title']
#         skip_unchanged = True
#         report_skipped = False
#         clean_model_instances = True

from import_export import resources
from .models import ProductItem

class ProductItemResource(resources.ModelResource):
    class Meta:
        model = ProductItem
        import_id_fields = ('Title',)
        fields = ('id', 'Title', 'Type', 'Grade', 'Nicotine', 'Sugar', 'Packing', 'Quantity', 'Price', 'Image', 'CreatedName', 'Create_at')

    def get_instance(self, instance_loader, row):
        """
        Override this method to return an existing instance based on the import_id_fields.
        """
        title = row.get('Title')
        if not title:
            return None

        try:
            return self._meta.model.objects.get(Title=title)
        except self._meta.model.DoesNotExist:
            return None

    def get_or_init_instance(self, instance_loader, row):
        """
        Check if the item with the same title exists and update it if it does.
        """
        instance = self.get_instance(instance_loader, row)
        if instance:
            return instance, False
        else:
            return self.init_instance(row), True
