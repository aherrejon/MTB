#from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from .forms import SuscriptionForm

#from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

# Register your models here.

class EventAdmin(admin.ModelAdmin):

  list_display = ('name', 'date', 'cost', 'suscriptions', 'left_suscriptions', 'jerseys', 'left_jerseys', 'medals', 'left_medals', 'total_rides', 'S', 'M', 'L', 'XL', 'XXL')
  
  def get_form(self, request, obj=None, **kwargs):
    self.exclude = ('left_medals', 'left_jerseys', 'left_suscriptions')
    form = super(EventAdmin, self).get_form(request, obj, **kwargs)
    return form

  def total_rides(self, obj):
    return Suscription.objects.filter(event=obj, ride=True, status='A').count()

  total_rides.short_description = "Transporte"

  def S(self, obj):
    return Suscription.objects.filter(event=obj, status='A', size='S').count()

  def M(self, obj):
    return Suscription.objects.filter(event=obj, status='A', size='M').count()

  def L(self, obj):
    return Suscription.objects.filter(event=obj, status='A', size='L').count()

  def XL(self, obj):
    return Suscription.objects.filter(event=obj, status='A', size='XL').count()

  XL.short_description = "XL"

  def XXL(self, obj):
    return Suscription.objects.filter(event=obj, status='A', size='XXL').count()

  XXL.short_description = "XXL"



class CyclistAdmin(admin.ModelAdmin):
  pass


"""
class SuscriptionAdmin(admin.ModelAdmin):

  list_display = ('event', 'cyclist', 'number', 'jersey', 'medal', 'ride', 'package', 'status')

  def get_form(self, request, obj=None, **kwargs):
    self.exclude = ('number', 'user')
    form = super(SuscriptionAdmin, self).get_form(request, obj, **kwargs)
    #import pdb; pdb.set_trace()
    form.fields['cyclist'] = AutoCompleteSelectField('cyclists')
    return form

  def save_model(self, request, obj, form, change):
  	obj.user = request.user
  	obj.save()
"""

class PendingSucription(admin.SimpleListFilter):
  title = u'Estado Asignacion' # a label for our filter
  parameter_name = 'pendientes' # you can put anything here

  def lookups(self, request, model_admin):
    # This is where you create filter options; we have two:
    return [
        ('pending', 'Pendientes'),
        ('available', 'Disponibles'),
        ('assigned', 'Asignadas'),
        ('all', 'Todas'),
    ] 

  def queryset(self, request, queryset):
    if self.value() == 'pending':
      return queryset.filter(cyclist__isnull=False, status__exact='P')
    if self.value() == 'available':
      return queryset.filter(cyclist__isnull=True)
    if self.value() == 'assigned':
      return queryset.filter(cyclist__isnull=False, status__exact='A')      
    if self.value() == 'all':
      return queryset.all()



class SuscriptionAdmin(admin.ModelAdmin):

  #list_display = ('number', 'cyclist', 'get_cyclist_city', 'get_cyclist_club',  'get_cyclist_sex', 'size', 'distance', 'package_type', 'paid_date', 'account', 'comments', 'logo', 'jersey', 'medal', 'status', 'user')
  list_display = ('number', 'cyclist', 'get_cyclist_city', 'get_cyclist_club',  'get_cyclist_sex', 'size', 'distance', 'package_type', 'paid_date', 'account', 'comments', 'jersey', 'status', 'user')
  list_filter = (PendingSucription, 'event',  'status', 'jersey', 'medal', 'package_type')
  #list_filter = ( ('event', RelatedDropdownFilter), ('status', DropdownFilter), ('jersey', DropdownFilter), ('medal', DropdownFilter), ('package', DropdownFilter), ('number', DropdownFilter))
  form = SuscriptionForm

  def save_model(self, request, obj, form, change):
  	obj.user = request.user
  	obj.save()

  def get_cyclist_city(self, suscription):
    return suscription.cyclist.city if suscription.cyclist is not None else '--'
  get_cyclist_city.admin_order_field = 'city'
  get_cyclist_city.short_description = 'Ciudad'

  def get_cyclist_club(self, suscription):
    return suscription.cyclist.club if suscription.cyclist is not None else '--'
  get_cyclist_club.admin_order_field = 'club'
  get_cyclist_club.short_description = 'Equipo'

  def get_cyclist_sex(self, suscription):
    return suscription.cyclist.sex if suscription.cyclist is not None else '--'
  get_cyclist_sex.admin_order_field = 'sex'
  get_cyclist_sex.short_description = 'Sexo'

  #def has_delete_permission(self, request, obj=None):
  #  return False

  def has_add_permission(self, request, obj=None):
    return False

  def get_actions(self, request):
    actions = super(SuscriptionAdmin, self).get_actions(request)
    if 'delete_selected' in actions:
      del actions['delete_selected']
    return actions

admin.site.register(Event, EventAdmin)
admin.site.register(Cyclist, CyclistAdmin)
admin.site.register(Suscription, SuscriptionAdmin)
