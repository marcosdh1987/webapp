from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, View
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from numpy.core.numeric import flatnonzero

#the default view
class HomeView(View):
    
    def get(self, *args, **kwargs):
        cur = 'main'
 
        context = {             'cur': cur,
                    }                                                             

        return render(self.request, 'home.html', context)