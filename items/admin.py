from django.contrib import admin

from people.models import Person
from items.models import Item
from items.models import Type
from items.models import Category

class ItemModelAdmin(admin.ModelAdmin):
	"""docstring for ItemModelAdmin"""

	model = Item
	radio_fields = {'publishing_status': admin.VERTICAL, 'audience_gender': admin.VERTICAL}

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
	    if db_field.name == "Author":
	        kwargs["queryset"] = Pesron.objects.filter(username='a')
	    return super(ItemModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class TypeModelAdmin(admin.ModelAdmin):
	"""docx"""

	radio_fields = {'name': admin.VERTICAL}

admin.site.register(Item, ItemModelAdmin)
admin.site.register(Type, TypeModelAdmin)
admin.site.register(Category)