# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max

# Create your models here.

EVENT_CATEGORIES = (
    ('P', 'Principiante'),
    ('I', 'Intermedia'),
    ('A', 'Avanzada'),
)

CYCLIST_CATEGORIES = (
    ('P', 'Principiante'),
    ('I', 'Intermedia'),
    ('A', 'Avanzada'),
)

SIZE_OPTIONS  = (
    ('N', 'None'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    ('XXL', 'Doble Extra Large'),
)

PACKAGE_OPTIONS  = (
    ('D', 'Entregado'),
    ('U', 'Pendiente'),
)

SUPPLY_OPTIONS  = (
    ('N', 'Nada'),
    ('B', 'Frijol'),
    ('R', 'Arroz'),
    ('D', 'Despensa'),
    ('O', 'Otro'),    
)

SUSCRIPTION_STATUS  = (
    ('A', 'Aceptado'),
    ('P', 'En Proceso'),
)

class Event(models.Model):
    name = models.CharField('Nombre', max_length=50)
    created = models.DateField(auto_now_add=True)
    date = models.DateField('Fecha', auto_now_add=True)
    cost = models.DecimalField('Costo', max_digits=10, decimal_places=2)
    distance = models.DecimalField('Distancia', max_digits=10, decimal_places=2)
    category =  models.CharField('Categoria', max_length=1, choices=EVENT_CATEGORIES, default='P')
    suscriptions =  models.PositiveIntegerField('Total Registros', default=0)
    medals = models.PositiveIntegerField('Total Medallas', default=0)
    jerseys = models.PositiveIntegerField('Total Jerseys', default=0)
    left_medals = models.PositiveIntegerField('Medallas Disponibles', default=0)
    left_jerseys = models.PositiveIntegerField('Jerseys Disponibles', default=0)
    left_suscriptions = models.PositiveIntegerField('Registros Disponibles', default=0)

    def save(self, *args, **kwargs):
      is_new = False
      if self.pk is None:
        is_new = True
        self.left_jerseys = self.jerseys
        self.left_medals = self.medals
        self.left_suscriptions = self.suscriptions

      super(Event, self).save(*args, **kwargs)

      # Create the number of suscriptions with default values
      if is_new:
        for s in range(1, self.suscriptions+1):
          s_obj = Suscription(event=self, number=s)
          s_obj.save()
    
    def __unicode__(self):
        return unicode(self.name)


class Cyclist(models.Model):
    firstname = models.CharField('Nombre', max_length=50, db_index=True)
    lastname = models.CharField('Apellido1', max_length=50, db_index=True)
    secondlastname = models.CharField('Apellido2', max_length=50, db_index=True, blank=True)
    email = models.EmailField('Email', db_index=True)
    age = models.PositiveIntegerField('Edad', blank=True)
    birthday = models.DateField('Fecha Nacimiento', blank=True) 
    created = models.DateField(auto_now_add=True)
    phone = models.CharField('Telefono', max_length=50, blank=True)
    category = models. CharField('Clasificación', max_length=1, choices=CYCLIST_CATEGORIES, default='P', blank=True)
    nickname = models.CharField('Apodo', max_length=50, db_index=True, null=True, blank=True)
    club = models.CharField('Club', max_length=50, db_index=True, blank=True)
    emergency_phone = models.CharField('Telefono Emergencia', max_length=50, blank=True)
    contact_name = models.CharField('Nombre Contacto', max_length=50, blank=True)
    contact_phone = models.CharField('Telefono Contacto', max_length=50, blank=True)
    blood = models.CharField('Tipo Sangre', max_length=7, default='', blank=True)

    def __unicode__(self):
        if self.nickname:
          return u'{f} {l} {s} ({n})'.format(f=self.firstname, l=self.lastname, s=self.secondlastname, n=self.nickname)
        return u'{f} {l} {s}'.format(f=self.firstname, l=self.lastname, s=self.secondlastname)


class Suscription(models.Model):
    user= models.ForeignKey(User, null=True, blank=True)
    event = models.ForeignKey(Event, verbose_name='Evento')
    cyclist = models.ForeignKey(Cyclist, verbose_name='Ciclista', null=True)
    number = models.PositiveIntegerField('Numero')
    jersey = models.BooleanField('Jersey', default=False)
    medal = models.BooleanField('Medalla', default=False)
    ride = models.BooleanField('Transporte', default=False)    
    size = models.CharField('Talla', max_length=3, choices=SIZE_OPTIONS, default='N')
    package = models.CharField('Paquete Entregado', max_length=1, choices=PACKAGE_OPTIONS, default='U')
    status = models.CharField('Estado Inscripcion', max_length=1, choices=SUSCRIPTION_STATUS, default='P')
    supply = models.CharField('Kilo de Ayuda', max_length=1, choices=SUPPLY_OPTIONS, default='N')

    class Meta:
      unique_together = (('event', 'number'), ('event', 'cyclist'))

    def __unicode__(self):
        return u'{e} {c} {n}'.format(e=self.event, c=self.cyclist, n=self.number)

    def save(self, *args, **kwargs):
      new = False
      if self.pk is None and self.number is None:
        new = True
        max_num = Suscription.objects.filter(event=self.event).aggregate(max=Max('number'))
        self.number  = max_num['max'] + 1 if max_num['max'] is not None else 1
      super(Suscription, self).save(*args, **kwargs)        
      if new:
        if self.jersey:
          self.event.left_jerseys -= 1
        if self.medal:
          self.event.left_medals -= 1
        self.event.left_suscriptions -= 1
        self.event.save()

      left_suscriptions = self.event.suscriptions - Suscription.objects.filter(event=self.event, status='A').count()
      left_jerseys = self.event.jerseys  - Suscription.objects.filter(event=self.event, jersey=True, status='A').count()
      left_medals = self.event.medals - Suscription.objects.filter(event=self.event, medal=True, status='A').count()
      self.event.left_suscriptions = left_suscriptions
      self.event.left_jerseys = left_jerseys
      self.event.left_medals = left_medals      
      self.event.save()

    def delete(self, *args,**kwargs):
      self.cyclist = None
      self.jersey = False
      self.medal = False
      self.ride = False
      self.size = 'N'      
      self.package = 'U'
      self.status = 'N'
      self.supply = 'N'
      self.save()

      

