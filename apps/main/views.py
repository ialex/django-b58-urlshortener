from apps.main.models import Url
from apps.main.forms import UrlForm
from apps.main.utils import JsonResponse
from apps.main.base58 import encode, decode


from django.conf import settings
from django.core.validators import URLValidator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect


def shortener(request):
    return HttpResponse('Are you lost? maybe you are looking for <a href="http://www.pixfirst.com?lost=true">Pixfirst</a>')


@csrf_exempt
def api(request):
    ''' Creates urls via GET
       requiere url eg. http://pixfirst.com
       returns json
    '''
    form = UrlForm(request.GET)
    if form.is_valid():
        url = Url.objects.create()
        url.url = form.cleaned_data['url']
        url.save()
        # +1000 cheating to have a number to have bigger base58 hashes
        url.short = "%s%s/" % (settings.DOMAIN, encode(url.id + 1000))
        url.save()
        print url.short
        return JsonResponse({'success': True, 'short': url.short, 'long': url.url})
    return JsonResponse({'success': False, 'large': request.POST.get('url')})


def redirect(request, hash):
    ''' Redirect the user to the large url based on hash '''
    try:
        print settings.DOMAIN + hash
        url = Url.objects.get(short__contains="%s%s/" % (settings.DOMAIN, hash))
        return HttpResponseRedirect(url.url)
    except Url.DoesNotExist:
        pass
    return HttpResponseRedirect('http://pixfirst.com?unknown=true')