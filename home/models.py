from django.db import models

from wagtail.core.models import Page

from blog.models import BlogPage, BlogListingPage


class HomePage(Page):

    @property
    def all_blogs(self):
        return BlogPage.objects.live().public()[:10]

