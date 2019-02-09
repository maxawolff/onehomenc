"""Views for one home website."""
from django.views.generic import TemplateView
from item.models import Item, Room
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
