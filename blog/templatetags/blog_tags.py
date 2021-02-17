from django import template

from blog.models import BlogListingPage

register = template.Library()


@register.simple_tag()
def get_blog_list_pages():
    return BlogListingPage.objects.live().public()
