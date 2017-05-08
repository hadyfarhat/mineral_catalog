from django import template

from minerals.models import Mineral

register = template.Library()


# @register.filter(name='check_if_available')
# def check_if_available(mineral, attribute):
#     if mineral.attribute == '':
#         return "No description available"
#     return mineral.attribute


@register.filter('title_case')
def title_case(name):
    '''title case a word'''
    if name != None:
        return name.title()
    return name
