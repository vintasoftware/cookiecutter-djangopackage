# -*- coding: utf-8 -*-
from django.conf.urls import url
{% if cookiecutter.models == "Comma-separated list of models" -%}from django.views.generic import TemplateView{% endif -%}

from . import views


app_name = '{{ cookiecutter.app_name }}'
urlpatterns = [
    {% if cookiecutter.models == "Comma-separated list of models" -%}
    url(r'', TemplateView.as_view(template_name="base.html")),
    {% else -%}
    {% for model in cookiecutter.models.split(',') -%}
    url(
        regex=r"^{{ model.strip() }}/~create/$",
        view=views.{{ model.strip() }}CreateView.as_view(),
        name='{{ model.strip() }}_create',
    ),
    url(
        regex=r"^{{ model.strip() }}/(?P<pk>\d+)/~delete/$",
        view=views.{{ model.strip() }}DeleteView.as_view(),
        name='{{ model.strip() }}_delete',
    ),
    url(
        regex=r"^{{ model.strip() }}/(?P<pk>\d+)/$",
        view=views.{{ model.strip() }}DetailView.as_view(),
        name='{{ model.strip() }}_detail',
    ),
    url(
        regex=r"^{{ model.strip() }}/(?P<pk>\d+)/~update/$",
        view=views.{{ model.strip() }}UpdateView.as_view(),
        name='{{ model.strip() }}_update',
    ),
    url(
        regex=r"^{{ model.strip() }}/$",
        view=views.{{ model.strip() }}ListView.as_view(),
        name='{{ model.strip() }}_list',
    ),
{{ '    ' if not loop.last else '' }}{% endfor -%}
{% endif -%}
]
