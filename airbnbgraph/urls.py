from airbnbgraph import views
from django.urls import path

app_name = 'airbnbgraph'

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('getnum/', views.Api.getNums, name="get-num"),
    path('getwc/',views.Api.getwc, name='get-wc'),
    path('getgraph/',views.Api.getGraph, name='get-graph'),
    path('getdata/',views.Api.getData, name='get-data'),
    path('get-seaborn-graph/',views.Api.getSeabornGraph, name='get-seaborn-graph'),
    path('get-seaborn-graph1/',views.Api.getSeabornGraph1, name='get-seaborn-graph1'),
    path('chart/',views.HomeView.as_view(), name='home-view'),
    path('chart-api/',views.ChartData.as_view(), name='chart-api'),
    path('plotly-chart/',views.PlotlyChartView.as_view(), name='plotly-chart'),
    path('book-table/',views.BookTableView.as_view(), name='book-table'),
    path('user-table/',views.UserTableView.as_view())
]