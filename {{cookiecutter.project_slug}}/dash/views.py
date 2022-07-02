from django.shortcuts import render
from django.views.generic import  View
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from django.contrib.staticfiles.storage import staticfiles_storage

import plotly.graph_objects as go
from plotly.offline import plot

# Create random data with numpy
import numpy as np
np.random.seed(1)

N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5



#the default view
class HomeView(View):
    
    def get(self, *args, **kwargs):
        cur = 'main'
 
        context = {             'cur': cur,
                    }                                                             

        return render(self.request, 'home.html', context)

#Main dashboard view, with overall information, based on analytics view
class dashboardView(View):
    
    def get(self, *args, **kwargs):

        # Create traces
        fig = go.Figure()

        fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                    mode='lines',
                    name='lines'))
        fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                            mode='lines+markers',
                            name='lines+markers'))
        fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                            mode='markers', name='markers'))


        # Setting layout of the figure.
        layout = {
            'title': 'MAPBOX',
            'xaxis_title': 'X',
            'yaxis_title': 'Y',
        }

        # Getting HTML needed to render the plot.
        plot_div = plot({'data': fig, 'layout': layout}, 
                        output_type='div')
        
        context = {  'plot_div' : plot_div,  
                    }                                                            

        return render(self.request, 'dashboard.html', context)