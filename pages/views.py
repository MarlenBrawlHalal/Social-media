from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'social_media/home.html'
    