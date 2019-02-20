"""Views for one home website."""
from django.views.generic import TemplateView, ListView, DetailView, View
from item.models import Room, Cart
import braintree
from django.shortcuts import redirect
# from gateway import generate_client_token, transact, find_transaction
import pdb

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="wkzr2hw78rb78kmr",
        public_key="bmbsgz9q9g8d8df6",
        private_key="0b3bd7493b849981972c76bc8ba6f35a"
    )
)


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
        total = 0
        client_token = gateway.client_token.generate()
        for item in context['cart'].item_set.all():
            total += item.cost
        context['total'] = total
        context['client_token'] = client_token
        # pdb.set_trace()
        return context


class ProcessPaymentView(View):
    """View that will process the payment info and redirect."""

    # template_name = 'home.html'

    # def get_context_data(self, **kwargs):
    #     """Get specific data for homepage."""
    #     context = super(ProcessPaymentView, self).get_context_data(**kwargs)
    #     pdb.set_trace()
    #     return context

    def post(self, request):
        """Trying to capture payment info."""
        body = request.body.decode('utf-8')
        blist = body.split('&')
        nonce = blist[1].split('=')[1]
        amount = blist[2].split('=')[1]
        result = gateway.transaction.sale({'amount': amount,
                                           'payment_method_nonce': nonce,
                                           'options': {"submit_for_settlement": True}})
        # pdb.set_trace()
        if result.is_success or result.transaction:
            return redirect('success')
        else:
            pass


class SuccessView(TemplateView):
    """View to show a successfull transaction."""

    template_name = 'success.html'
