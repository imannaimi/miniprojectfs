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
import io
import urllib, base64

warnings.filterwarnings("ignore")
from scipy.stats import norm, poisson, uniform, skew, kurtosis, iqr 
from matplotlib.backends.backend_pdf import PdfPages

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'airbnbgraph/index.html', context=None)

class Api(TemplateView):
    def getNums(request):
        file_path = MEDIA_ROOT+"/clean_data.csv"
        data = pd.read_csv(file_path)
        response = HttpResponse(content_type="image/png")

        plt.figure(figsize = (13,8))
        ax = sb.countplot(y="Location", palette= "RdPu", data=data)
        ax.set_ylabel('Count')
        ax.set_title('Airbnb Location in Kuala Lumpur and Selangor')
        for container in ax.containers:
            ax.bar_label(container)

        ax.figure.savefig(response , format="png")

        return response

    def getwc(request):
        file_path = MEDIA_ROOT+"/airbnb_wordcloud.png"
        word_cloud = pd.read_csv(file_path)
        response = HttpResponse(content_type="image/png")
        # mask = np.array(Image.open(MEDIA_ROOT+"/airbnb.png")) 

        # color= ImageColorGenerator(mask)

        # word_cloud = WordCloud(width = 480, height = 480, background_color='white', colormap='plasma', mask=mask).generate(titles)
        # plt.figure(figsize=(9,8),facecolor = 'white')
        # plt.imshow(word_cloud,interpolation='bilinear')
        # plt.axis('off')
        # plt.tight_layout(pad=0)
        # plt.show()
        word_cloud.figure.savefig(response , format="png")

        return response
    
    # Wordcloud 1
    def getGraph(request):
        file_path = MEDIA_ROOT+"/clean_data.csv"
        data = pd.read_csv(file_path)
        response = HttpResponse(content_type="image/png")

        plt.figure(figsize = (13,8))
        ax = sb.stripplot(x="Price", y="Location", data=data, jitter=2.0, hue="Location")
        ax.set_title('Price of Airbnb based on Location')

        ax.figure.savefig(response , format="png")
        return response
 
    def getData(request):
        file_path = MEDIA_ROOT+"/clean_data.csv"
        df = pd.read_csv(file_path)
        return HttpResponse(df.to_html(classes='table table-bordered'))

    def getSeabornGraph(request):
        # response = HttpResponse(PdfPages("output.pdf"))
        # response = HttpResponse(response.content, content_type='application/pdf')
        # pdfFile = PdfPages("output.pdf")
        file_path = MEDIA_ROOT+"/clean_data.csv"
        data = pd.read_csv(file_path)
        response = HttpResponse(content_type="image/jpeg")

        price_range = []

        for x in data["Price"]:
            if x <=200:
                price_range.append('0-200')
            elif 200< x <=400:
                price_range.append('201-400')
            elif 400< x <=600:
                price_range.append('401-600')
            elif 600< x <=800:
                price_range.append('601-800')
            elif 800< x <=1000:
                price_range.append('801-1000')
            else:
                price_range.append('More than 1000')
        
        data["Price_Range"] = price_range
        
        data.Price_Range=data.Price_Range.astype('category')
        
        percent_pool = pd.crosstab(data.loc[:, "Price_Range"], 
                             data.loc[:, "Pool"])

        percent_pool = pd.crosstab(data.loc[:, "Price_Range"], 
               data.loc[:, "Pool"], 
               normalize = "index") * 100 #Normalized by index so that all rows equals to 100

        c = ["#FEA3AA","#FFE4E1"]
        ax = percent_pool.plot(kind='bar', stacked=False, rot=0, color= c, figsize=(13, 8)) 
        ax.set_ylabel('Percentage %')
        ax.set_title('Percentage of Pool Accessibility based on Price Range')
        for container in ax.containers:
            ax.bar_label(container,fmt='%.1f%%')    
        ax.figure.savefig(response , format="png")
        return response

    def getSeabornGraph1(request):
        file_path = MEDIA_ROOT+"/clean_data.csv"
        data = pd.read_csv(file_path)
        response = HttpResponse(content_type="image/jpeg")

        percent_wifi = pd.crosstab(data.loc[:, "Price_Range"], 
               data.loc[:, "Wifi"], 
               normalize = "index") * 100 #Normalized by index so that all rows equals to 100
               
        c = ["#C25283","#FDD7E4"]
        ax = percent_wifi.plot(kind='bar', stacked=False, rot=0, color= c, figsize=(13, 8)) 
        ax.set_ylabel('Percentage %')
        ax.set_title('Percentage of Wifi Accessibility based on Price Range')
        for container in ax.containers:
            ax.bar_label(container,fmt='%.1f%%') 

        ax.figure.savefig(response , format="png")
        return response
 
# Chapter 4: CHART.JS (Involves Javascript)
 
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

