from django.core.management import BaseCommand

from blog.models import BlogListingPage
from home.models import HomePage


class Command(BaseCommand):
    help = 'Feeds data into a system initially.'

    @staticmethod
    def create_all_blogs_page(root):
        if not BlogListingPage.objects.all().exists():
            page = BlogListingPage(
                title="All Blogs",
                draft_title="All Blogs",
                slug="blogs",
            )
            root.add_child(instance=page)

    def handle(self, *args, **options):
        root = HomePage.objects.first()
        if root:
            self.create_all_blogs_page(root)
