from django.test import TestCase
from django.urls import reverse
from .models import Nike

class MainTestCase(TestCase):
    
    def test_view(self):
        path = reverse('str1')
        response = self.client.get(path)
        nike = Nike.objects.all()
        
        self.assertTemplateUsed(response, 'index.html')
       
