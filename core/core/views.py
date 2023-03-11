from django.views.generic.base import TemplateView, RedirectView

class IndexView(TemplateView):
    template_name = 'home.html'