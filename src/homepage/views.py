from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.shortcuts import redirect
from django.conf import settings

# Create your views here.
class HomeView(View):
    template_name = "home.html"
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = "about.html"

class DashboardView(TemplateView):
    template_name = "dashboard.html"

 
    def get(self, request, *args, **kwargs):
        context = {'upkeep': 40000, 'overall': 100000, 'reports': 100, 'pending': 10}

        return render(request, self.template_name, context)