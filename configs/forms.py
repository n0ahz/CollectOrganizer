from django import forms

from configs.models import LibraryPath


class LibraryPathForm(forms.ModelForm):
    """Auto django model form"""
    class Meta(object):
        model = LibraryPath
        fields = ['media_type', 'media_path']