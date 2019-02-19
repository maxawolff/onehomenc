"""Views for one home website."""
from django.views.generic import TemplateView, ListView, DetailView
from item.models import Room, Cart
import pdb


class HomeView(TemplateView):
    """Function to display the home page."""

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        """Get specific data for homepage."""
        context = super(HomeView, self).get_context_data(**kwargs)
        context['rooms'] = Room.objects.all()
        # pdb.set_trace()
        return context


class CheckoutView(DetailView):
    """Function to display the checkout page."""

    template_name = 'checkout.html'
    model = Cart
    context_object_name = 'cart'

    def get_context_data(self, **kwargs):
        """Get specific data for checkout page."""
        context = super(DetailView, self).get_context_data(**kwargs)
        pdb.set_trace()
        return context
