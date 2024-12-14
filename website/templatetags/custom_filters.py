from django import template
from persiantools.jdatetime import JalaliDate

register = template.Library()

@register.filter
def persian_date(value):
    if value:
        # Convert the datetime to Persian date
        persian_date = JalaliDate(value)
        return persian_date.strftime('%Y/%m/%d')
    return value
