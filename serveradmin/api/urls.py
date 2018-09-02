"""Serveradmin - Remote HTTP API

Copyright (c) 2018 InnoGames GmbH
"""

from django.urls import path

from serveradmin.api.views import (
    doc_functions,
    dataset_query,
    dataset_commit,
    dataset_new_object,
    dataset_create,
    api_call,
)

urlpatterns = [
    path('functions', doc_functions),
    path('dataset/query', dataset_query),
    path('dataset/commit', dataset_commit),
    path('dataset/new_object', dataset_new_object),
    path('dataset/create', dataset_create),
    path('call', api_call),
]
