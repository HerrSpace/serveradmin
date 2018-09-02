"""Serveradmin - Graphite Integration

Copyright (c) 2018 InnoGames GmbH
"""

from django.urls import path

from serveradmin.graphite.views import graph, graph_table

urlpatterns = [
    path('graph_table', graph_table, name='graphite_graph_table'),
    path('graph', graph, name='graphite_graph'),
]
