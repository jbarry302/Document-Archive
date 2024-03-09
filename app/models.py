from django.db import models

__author__ = "jbarry302"

class BaseModel(models.Model):
    """
    An abstract base model providing common fields for tracking creation and modification timestamps.

    Attributes:
        created_at (DateTimeField): The timestamp representing the creation date and time.
        updated_at (DateTimeField): The timestamp representing the last modification date and time.

    Meta:
        abstract (bool): Specifies that this model is abstract and should not be created as a database table.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Document(BaseModel):
    """
    A model representing a document with various attributes such as title, description, and file attachments.

    Attributes:
        title (CharField): The title of the document.
        description (TextField): A field for providing a detailed description of the document.
        file_document (FileField): A file attachment representing the document content.
        document_url (URLField): An optional URL for an online resource related to the document.
        picture (ImageField): An image attachment representing the document.
        note (TextField): Additional notes or comments related to the document.

    Methods:
        __str__(): Returns a string representation of the document, displaying its title.

    Meta:
        ordering (list): Specifies the default ordering of documents based on the creation timestamp.
    """
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    file_document = models.FileField(upload_to='documents/', blank=True, null=True, verbose_name='File Document')
    document_url = models.URLField(blank=True, null=True, verbose_name='Document URL')
    picture = models.ImageField(upload_to='documents/', blank=True, null=True, verbose_name='Picture')
    note = models.TextField(blank=True, null=True, verbose_name='Note')

    def __str__(self):
        """
        Returns a string representation of the document, displaying its title.

        Returns:
            str: The title of the document.
        """
        return self.title

    class Meta:
        ordering = ['-created_at']
