from django.test import TestCase
from django.urls import reverse
from .models import Document

class ViewsTest(TestCase):
    def setUp(self):
        self.document = Document.objects.create(title='Test Document', description='This is a test document.')

    def test_document_list_view(self):
        """
        Test the document list view.
        """
        response = self.client.get(reverse('app:documents'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'document_list.html')
        self.assertContains(response, self.document.title)

    def test_document_detail_view(self):
        """
        Test the document detail view.
        """
        response = self.client.get(reverse('app:document_detail', kwargs={'pk': self.document.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'document_detail.html')
        self.assertContains(response, self.document.title)

    def test_document_create_view(self):
        """
        Test the document create view.
        """
        response = self.client.get(reverse('app:document_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'document_create.html')

    def test_document_update_view(self):
        """
        Test the document update view.
        """
        response = self.client.get(reverse('app:document_update', kwargs={'pk': self.document.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'document_update.html')

    def test_document_delete_view(self):
        """
        Test the document delete view.
        """
        response = self.client.get(reverse('app:document_delete', kwargs={'pk': self.document.pk}))
        self.assertEqual(response.status_code, 302) # Redirect status to the document list view. there is no confirmation page as it will be handled before visiting the delete view.
        self.assertEqual(response.url, reverse('app:documents'))
