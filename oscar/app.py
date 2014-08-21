# flake8: noqa, because URL syntax is more readable with long lines

import django
from django.conf.urls import patterns, url, include
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

from oscar.core.application import Application
from oscar.apps.customer import forms
from oscar.core.loading import get_class
from oscar.views.decorators import login_forbidden


class Shop(Application):
    name = None

    catalogue_app = get_class('catalogue.app', 'application')
    customer_app = get_class('customer.app', 'application')
    basket_app = get_class('basket.app', 'application')
    checkout_app = get_class('checkout.app', 'application')
    promotions_app = get_class('promotions.app', 'application')
    search_app = get_class('search.app', 'application')
    dashboard_app = get_class('dashboard.app', 'application')
    offer_app = get_class('offer.app', 'application')

    def get_urls(self):
        urls = [
            (r'^catalogue/', include(self.catalogue_app.urls)),
            (r'^basket/', include(self.basket_app.urls)),
            (r'^checkout/', include(self.checkout_app.urls)),
            (r'^accounts/', include(self.customer_app.urls)),
            (r'^search/', include(self.search_app.urls)),
            (r'^dashboard/', include(self.dashboard_app.urls)),
            (r'^offers/', include(self.offer_app.urls)),
        ]

        urls += [
            (r'', include(self.promotions_app.urls)),
        ]
        return patterns('', *urls)


# 'shop' kept for legacy projects - 'application' is a better name
shop = application = Shop()
