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
        list_suscriptions = list_suscriptions[start:start+length]
        list_result = []
        for suscription in list_suscriptions:
          list_result.append({
            'number': suscription.number,
            'cyclist': suscription.cyclist.__str__(),
            'club': suscription.cyclist.club,
            'jersey': u'<i class="fa fa-check" aria-hidden="true" value="Sí"></i>' if suscription.jersey else u'<i class="fa fa-times" aria-hidden="true" value="No"></i>',
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
        list_suscriptions = list_suscriptions[start:start+length]
        list_result = []
        for suscription in list_suscriptions:
          list_result.append({
            'number': suscription.number,
            'cyclist': suscription.cyclist.__str__(),
            'club': suscription.cyclist.club,
            'jersey': u'<i class="fa fa-check" aria-hidden="true" value="Sí"></i>' if suscription.jersey else u'<i class="fa fa-times" aria-hidden="true" value="No"></i>',
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
    return render(request, 'register.html')
