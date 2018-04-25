# -*- coding: utf-8 -*-
{% if cookiecutter.models != "Comma-separated list of models" %}from model_utils.models import TimeStampedModel

{% for model in cookiecutter.models.split(',') %}
class {{ model.strip() }}(TimeStampedModel):
    pass{{ '\n' if not loop.last else '' }}
{% endfor -%}
{% else -%}from django.db import models
{% endif -%}
