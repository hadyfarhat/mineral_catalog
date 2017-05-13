from django import template


register = template.Library()


# @register.filter(name='check_if_available')
# def check_if_available(mineral, attribute):
#     if mineral.attribute == '':
#         return "No description available"
#     return mineral.attribute


@register.filter('title_case')
def title_case(name):
    '''title case a word'''
    # if name != None:
    if name is not None:
        return name.title()
    return name


@register.filter('truncate')
def truncate(name):
    '''truncates a word to 20 characters'''
    if len(name) > 20:
        return "{}... more details".format(name[:20])
    return name


@register.inclusion_tag('minerals/important_detail.html', takes_context=True)
def important_detail(context, mineral):
    '''
    displays the most important detail of a mineral
    which has the most number of letters
    '''
    fields = mineral._meta.get_fields()
    max_length = ""
    important_field = ""
    for field in fields:
        if len(str(getattr(mineral, field.name))) > len(str(max_length)):
            max_length = str(getattr(mineral, field.name))
            important_field = field.name
    return {
        'important_field': important_field,
        'max_length': max_length
    }


@register.filter('check_if_empty')
def check_if_empty(field):
    '''
    check if a mineral field is empty
    if its is => display that this field has no description
    '''
    if field == '':
        return "no description available"
    return field


# @register.inclusion_tag('minerals/truncate_mineral_list.html')
# def truncate_mineral_list(minerals):
#     '''
#     takes a list of minerals and truncates it to 54 items
#     '''
#     truncated_minerals = minerals[:54]
#     return {'truncated_minerals': truncated_minerals}
