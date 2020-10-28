from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser, User
from eshop.models import *

from eshop.utils import cartData
from eshop.views import cart

class ViewTest(TestCase):

    def test_root_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_root_title(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>Eshopping</title>')
    
    def test_cart_page(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_cart_template(self):
        response = self.client.get('/cart/')
        self.assertTemplateUsed(response, template_name='cart.html')

        # No longer valid due to the need of a user. Guest checkout test
        # is below in seperate class.

    # def test_checkout_page(self):
    #     response = self.client.get('/checkout/')
    #     self.assertEqual(response.status_code, 203)
    
    def test_checkout_template(self):
        response = self.client.get('/checkout/')
        self.assertTemplateUsed(response, template_name='checkout.html')
    
    def test_store_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, template_name='store.html')

    def test_help(self):
        self.assertTrue(True)

    # No template used to create admin page 
    # also cannot access the admin page from here because our 
    # test is for eShop not the whole project    
"""    
    def test_admin_page(self):
        response = self.client.get('admin')
        self.assertEqual(response.status_code, 205)
    
    
     def test_admin_template(self):
        response = self.client.get('admin')
        self.assertTemplateUsed(response, template_name='admin.html') """

class ModelsTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='Eddie2020', email='test@work.com', password='secret')
        self.customer = Customer.create(user=self.user) 
        self.customer.save()
        self.product = Product.objects.create(name='Guitar', price=500, digital= False)
        self.product.save()
        self.order = Order.objects.create(customer=self.customer, complete= False, transaction_id= 56178)
        self.order.save()
        self.orderitem = OrderItem.objects.create(product=self.product, order=self.order, quantity= 2)
        self.orderitem.save()
        self.shipping = ShippingAddress.objects.create(customer=self.customer, order=self.order, address= '123 drive st', city='Denver', state='CO', zipcode=80123,)
        self.shipping.save()
        # Test objects ^

    def test_Customer(self):
        x = self.customer

        self.assertEqual(x.user, self.user)
        self.assertEqual(x.name, 'Eddie2020')
        self.assertEqual(x.email, 'test@work.com')

    def test_product(self):
        x = self.product
        self.assertEqual(x.name, 'Guitar')
        self.assertEqual(x.price, 500)
        self.assertEqual(x.digital, False)
    
    def test_Order(self):
        x = self.order
        self.assertEqual(x.customer, self.customer)
        self.assertEqual(x.complete, False)
        self.assertEqual(x.transaction_id, 56178)
    
    def test_OrderItem(self):
        x = self.orderitem
        self.assertEqual(x.product, self.product)
        self.assertEqual(x.order, self.order)
        self.assertEqual(x.quantity, 2)
    
    def test_Shipping(self):
        x = self.shipping
        self.assertEqual(x.customer, self.customer)
        self.assertEqual(x.order, self.order)
        self.assertEqual(x.address, '123 drive st')
        self.assertEqual(x.city, 'Denver')
        self.assertEqual(x.state, 'CO')
        self.assertEqual(x.zipcode, 80123)

    def test_help(self):
        self.assertTrue(True)


class GuestCheckoutTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_guest_cart(self):
        cook = {1:{'quantity': 1}, 2:{'quantity': 1}, 3:{'quantity': 1}}

        request = self.factory.get('/cart')
        request.test_cart = cook
        request.user = User
        request.user.is_authenticated = False

        response = cart(request)

        self.assertEqual(response.status_code, 200) # Make sure everything comes back OK