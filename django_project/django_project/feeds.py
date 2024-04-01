from django.contrib.syndication.views import Feed
from django.urls import reverse

from classviews.models import Contact


class ContactTutorialsFeeds(Feed):
    title = "Contact"
    link = "/latesttutorials/"
    description = "Recent free Contact on Django Tutorial."

    def items(self):
        return Contact.objects.order_by('-first_name')[:5]

    def item_title(self, item):
        return item.first_name

    def item_description(self, item):
        return item.first_name + " "+ item.last_name

    def item_link(self, item):
        return reverse('cbv-detail-view', args=[item.pk])