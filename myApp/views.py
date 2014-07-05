from django.http import HttpResponse
from django.template import RequestContext, loader
from myApp.models import Owner, House


def index(request):
    all_owners = House.objects.all()
    template = loader.get_template('myApp/index.html')
    context = RequestContext(request, {
        'all_owners': all_owners,
    })
    return HttpResponse(template.render(context))

