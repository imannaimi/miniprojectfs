from django.shortcuts import render
from django.http import HttpResponse
from airbnb.settings import MEDIA_ROOT
from django.views.generic import TemplateView

# from rest_framework.views import APIView
# from rest_framework.response import Response

# Create your views here.
import numpy as np
import pandas as pd
import matplotlib as pl
pl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sb
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import urllib
# from IPython.display import display
import random
import warnings
warnings.filterwarnings("ignore")
from scipy.stats import norm, poisson, uniform, skew, kurtosis, iqr 
from matplotlib.backends.backend_pdf import PdfPages

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'airbnbgraph/index.html', context=None)

class Api(TemplateView):
    def getNums(request):
        n = np.array([2,3,4])
        name1 = "name-1" + str(n[1])
        return HttpResponse('{"name:":'+name1+',"age":31,"city":"New York"}')

    def getAvg(request):
        s1=request.GET.get("val", "")
        print(s1)
        if len(s1)==0:
            return HttpResponse("none")
        l1=s1.split(',')
        ar=np.array(l1,dtype=int)

        return HttpResponse(str(np.average(ar)))
    
    # Wordcloud 1
    def getGraph(request):
        file_path = MEDIA_ROOT+"/clean_data.csv"
        data = pd.read_csv(file_path)
        response = HttpResponse(content_type="image/jpeg")

        name = data["Name"].astype("string")

        str1 = "" 
    
        # traverse in the string  
        for ele in name: 
            str1 += ele
        
        titles = listToString(name)

        wordcloud = WordCloud(width = 600, 
                      height = 800,
                      max_words=1000,
#                       mask=mask,
                      background_color='white',
                      random_state=42).generate(titles)
        
        plt.figure(figsize=(12,12)) # inches
        plt.axis("off")
        ax = plt.imshow(wordcloud,interpolation='bilinear')

        # x=np.arange(0, 2 * np.pi, 0.01)
        # s=np.cos(x)**2
        # plt.plot(x,s)
 
        # plt.xlabel('xlabel(X)')
        # plt.ylabel('ylabel(y)')
        # plt.title('Basic Graph!')
        # plt.grid(True)

        ax.figure.savefig(response , format="png")
        return response
 
    def getData(request):
        file_path = MEDIA_ROOT+"/clean_data.csv"
        df = pd.read_csv(file_path)
        return HttpResponse(df.to_html(classes='table table-bordered'))

    def getSeabornGraph(request):
        # response = HttpResponse(PdfPages("output.pdf"))
        # response = HttpResponse(response.content, content_type='application/pdf')
        pdfFile = PdfPages("output.pdf")
        response = HttpResponse(pdfFile, content_type='application/pdf')

        file_path = MEDIA_ROOT+"/clean_data.csv"
        data = pd.read_csv(file_path)

        # Graph 1
        plt.figure(figsize = (13,8))
        ax = sb.countplot(x="Location", palette= "RdPu", data=data)
        ax.set_ylabel('Count')
        ax.set_title('Airbnb Location in Selangor')
        for container in ax.containers:
            ax.bar_label(container)
        # ax.figure.savefig(response , format="png")        
        pdfFile.savefig(ax.figure)

        # Graph 2
        plt.figure(figsize = (13,8))
        ax = sb.countplot(y="Location", palette= "RdPu", data=data)
        ax.set_ylabel('Count')
        ax.set_title('Airbnb Location in Selangor')
        for container in ax.containers:
            ax.bar_label(container)
        pdfFile.savefig(ax.figure)
        # graph = sb.factorplot(x='Survived',hue='Sex',data=df, col='Pclass',kind='count') #passenger class
        # graph = sb.factorplot(x='Price',hue='Rating',data=df, col='Location',kind='count')
        # graph.savefig(response, format="png")

        pdfFile.close()
        return response
 
# # Chapter 4: CHART.JS (Involves Javascript)
 
from rest_framework.views import APIView #Using the APIView class is pretty much the same as using a regular View class
from rest_framework.response import Response
 
class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'airbnbgraph/charts.html')
 
class ChartData(APIView):
    def get(self, request, format=None):
        labels=['January','February',"March","April","May","June","July"]
        chartLabel="My Data"
        chartData=[0,10,5,2,20,30,45]
        data = {
            "labels":labels, 
            "chartLabel":chartLabel, 
            "chartdata":chartData, 
        }
        return Response(data)
 
 
# # Chapter 5: Plot.ly (Involves Javascript)
from plotly.offline import plot
import plotly.graph_objs as go
 
class PlotlyChartView(TemplateView):
    def get(self, request, *args, **kwargs):
        x_data=[0,1,2,3]
        y_data=[x**2 for x in x_data]
        plot_div = plot([go.Scatter(
            x=x_data,
            y=y_data,
            mode='lines',
            name='My Plotly Chart',
            opacity=0.8,
            marker_color='green'
        )], output_type='div')
 
        return render(request, 'airbnbgraph/plotly.html', context={'plot_div':plot_div})
 
# # Part 6: DJANGO-TABLES (Does not involves Javascript) #An app for creating HTML tables
import django_tables2 as tables
from homestay.models import Homestay
from hello_world.models import User, UserProfileInfo
 
# Table Class
class BookTable(tables.Table):
    class Meta:
        model = Homestay
 
# View
class BookTableView(tables.SingleTableView):
    table_class=BookTable
    queryset=Homestay.objects.all()
    template_name="airbnbgraph/table.html"
 
# Table Class
class UserTable(tables.Table):
    class Meta:
        model = UserProfileInfo
 
# View
class UserTableView(tables.SingleTableView):
    table_class=UserTable
    queryset=UserProfileInfo.objects.all()
    template_name="airbnbgraph/table.html"

