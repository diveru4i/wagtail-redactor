from django import forms
from django.forms import widgets
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

from wagtail_redactor.utils import json_dumps
from wagtail_redactor.default_settings import REDACTOR_OPTIONS


class RedactorEditor(widgets.Textarea):
    def __init__(self, *args, **kwargs):
        upload_to = kwargs.pop('upload_to', '')
        self.options = getattr(settings, 'REDACTOR_OPTIONS', REDACTOR_OPTIONS)
        self.options.update(kwargs.pop('redactor_options', {}))

        if kwargs.pop('allow_file_upload', True):
            self.options['fileUpload'] = reverse_lazy(
                'redactor_upload_file', kwargs={'upload_to': upload_to}
            )
        if kwargs.pop('allow_image_upload', True):
            self.options['imageUpload'] = reverse_lazy(
                'redactor_upload_image', kwargs={'upload_to': upload_to}
            )

        widget_attrs = {'class': 'redactor-box'}
        widget_attrs.update(kwargs.get('attrs', {}))
        widget_attrs.update({'data-redactor-options': self.options})

        kwargs['attrs'] = widget_attrs
        super(RedactorEditor, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        """
        Must parse self.options with json_dumps on self.render.
        Because at some point Django calls RedactorEditor.__init__ before
        loading the urls, and it will break.
        """
        attrs['data-redactor-options'] = json_dumps(self.options)
        html = super(RedactorEditor, self).render(name, value, attrs)
        return mark_safe(html)

    def _media(self):
        js = (
            'redactor/codemirror/lib/codemirror.js',
            'redactor/codemirror/mode/xml/xml.js',
            'redactor/codemirror/addon/edit/matchtags.js',
            'redactor/codemirror/addon/fold/xml-fold.js',
            'redactor/redactorWithCodemirror.init.js',
            'redactor/fixed-redactor.js',
            'redactor/langs/ru.js',
            'redactor/redactor_init_hook.js',
        )

        if 'plugins' in self.options:
            plugins = self.options.get('plugins')
            for plugin in plugins:
                js = js + (
                    'redactor/plugins/{0}.js'.format(plugin),
                )

        css = {
            'all': (
                'redactor/codemirror/lib/codemirror.css',
                'redactor/css/fixed-redactor.css',
                'redactor/css/django_admin.css',
                'redactor/css/admin_styles.css',
            )
        }
        return forms.Media(css=css, js=js)

    media = property(_media)
