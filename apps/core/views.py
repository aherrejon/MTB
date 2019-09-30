# -*- encoding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from dal import autocomplete
from .models import Cyclist
from django.db.models import Q
from django.http import Http404 
from django.http import HttpResponseRedirect
from .models import Suscription
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.db.models import Avg, Max, Min
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


class CyclistAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Cyclist.objects.none()

        qs = Cyclist.objects.all()
        if self.q:
            qs = qs.filter( Q(firstname__icontains=self.q) | Q(lastname__icontains=self.q) | Q(secondlastname__icontains=self.q) | Q(nickname__icontains=self.q) )
        return qs


def home(request):
  if request.user.is_authenticated():
    return HttpResponseRedirect('/admin/')
  return render(request, 'base.html')


def records(request):
  if request.method == 'POST':
    if request.is_ajax():
      try:
        ssearch = request.POST.get('sSearch')
        start = int(request.POST.get('iDisplayStart'))
        length = int(request.POST.get('iDisplayLength'))
        #list_suscriptions =  Suscription.objects.all()
        
        

        list_suscriptions =  Suscription.objects.filter(event__id=10, status='A')
        if ssearch:
          list_suscriptions = list_suscriptions.filter(
            Q(cyclist__firstname__icontains=ssearch) |
            Q(cyclist__nickname__icontains=ssearch) |
            Q(cyclist__lastname__icontains=ssearch) |
            Q(cyclist__club__icontains=ssearch) |
            Q(cyclist__secondlastname__icontains=ssearch) 
          )
        total = list_suscriptions.count()
        if length < 0:
          length = total
        list_suscriptions = list_suscriptions[start:start+length]
        list_result = []
        for suscription in list_suscriptions:
          list_result.append({
            'number': suscription.number,
            'cyclist': suscription.cyclist.__str__(),
            'club': suscription.cyclist.club,
            # 'jersey': u'<i class="fa fa-check" aria-hidden="true" value="Sí"></i>' if suscription.jersey else u'<i class="fa fa-times" aria-hidden="true" value="No"></i>',
            'jersey': 'Si' if suscription.jersey else u'No',
            #'supply': '<i class="fa fa-check" aria-hidden="true"></i>' if suscription.supply != 'N' else '<i class="fa fa-times" aria-hidden="true"></i>',
            #'ride': '<i class="fa fa-check" aria-hidden="true"></i>' if suscription.ride else '<i class="fa fa-times" aria-hidden="true"></i>',
            'city': suscription.cyclist.city,
            'distance': '%s KM' % suscription.distance,
          })
        result = {
          'data': list_result,
          'iTotalRecords': total,
          'iTotalDisplayRecords': total,
          #'aiDisplay': total,
          #'aiDisplayMaster': total,
          'iRecordsDisplay': total,
        }
        return JsonResponse(result)
      except Exception, e:
        print str(e)
        raise Http404
  else:
    raise Http404


def register(request):
  if request.method == 'POST':
    if request.FILES['payment']:
      firstname = request.POST.get('firstname')
      lastname = request.POST.get('lastname')
      secondlastname = request.POST.get('secondlastname')
      email = request.POST.get('email')
      age = request.POST.get('age')
      phone = request.POST.get('phone')
      category = request.POST.get('category')
      nickname = request.POST.get('nickname')
      club = request.POST.get('club')
      emergency_phone = request.POST.get('emergency_phone')
      contact_name = request.POST.get('contact_name')
      contact_phone = request.POST.get('contact_phone')
      blood = request.POST.get('blood')
      city = request.POST.get('city')
      sex = request.POST.get('sex')

      cyclist, created = Cyclist.objects.get_or_create(email=email)

      cyclist.firstname = firstname
      cyclist.lastname = lastname
      cyclist.secondlastname = secondlastname
      cyclist.age = age
      #cyclist.birthday = birthday
      cyclist.phone = phone
      cyclist.category = category
      cyclist.nickname = nickname
      cyclist.club = club
      cyclist.emergency_phone = emergency_phone
      cyclist.contact_name = contact_name
      cyclist.contact_phone = contact_phone
      cyclist.blood = blood
      cyclist.city = city
      cyclist.sex = sex
      cyclist.save()
      
      number = Suscription.objects.filter(event_id=10, cyclist__isnull=True).aggregate(Min('number'))
      suscription = Suscription.objects.get(event_id=10, number=number)
      suscription.cyclist = cyclist
      suscription.save()

      payment_file = request.FILES['payment']
      payment_name = '%s__%s' % (number, payment_file.name)
      fs = FileSystemStorage()
      filename = fs.save('', payment_file)  
      
      msg_plain = render_to_string('templates/email/register_thanks.txt', {'firstname': firstname, 'lastname': lastname})
      msg_html = render_to_string('templates/email/register_thanks.html', {'firstname': firstname, 'lastname': lastname})
      send_mail('Bienvenido 6toReto Los Miradores', msg_plain, settings.EMAIL_HOST_USER, [email], fail_silently=False, html_message=msg_html)

      msg_plain = render_to_string('templates/email/register_new.txt', {'fistname': fistname, 'lastname':lastname,  'number':number,  'city':city, 'club':club, 'package':package})
      msg_html = render_to_string('templates/email/register_new.html', {'fistname': fistname, 'lastname':lastname,  'number':number,  'city':city, 'club':club, 'package':package})
      email = EmailMessage(
          'Nuevo Registro al 6to Reto los Miradores',
          msg_html,
          settings.EMAIL_HOST_USER,
          settings.REGISTER_EMAILS,
      )
      message.attach(payment_name, payment_file)
      #send_mail('Nuevo Registro al 6to Reto los Miradores', msg_plain, settings.EMAIL_HOST_USER, settings.REGISTER_EMAILS, fail_silently=False, html_message=msg_html)
    
      return render(request, 'register_thanks.html')  
    else:
      error = "PAGO NO ADJUNTADO"

  else:
    return render(request, 'register.html')
