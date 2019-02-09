"""Views for one home website."""
from django.views.generic import TemplateView
import pdb


class HomeView(TemplateView):
    """Function to display the home page."""

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        """Get specific data for homepage."""
        context = super(HomeView, self).get_context_data(**kwargs)
        # pdb.set_trace()
        return context
