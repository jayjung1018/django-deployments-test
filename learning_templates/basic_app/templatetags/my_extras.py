from django import template

register = template.Library()

@register.filter(name="cutty")
def cut(value,arg):
    """
    This cuts out all values of "Arg" from the string
    """

    return value.replace(arg, "")
