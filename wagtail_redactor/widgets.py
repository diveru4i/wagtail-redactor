from redactor.widgets import RedactorEditor, GLOBAL_OPTIONS

from django import forms
from django.conf import settings


class PatchedRedactorEditor(RedactorEditor):
    def _media(self):
        js = (
            # 'redactor/jquery.redactor.init.js',    ## conflicts with /static/redactor/redactorWithCodemirror.init.js
            'redactor/redactor{0}.js'.format('' if settings.DEBUG else '.min'),
            'redactor/langs/{0}.js'.format(GLOBAL_OPTIONS.get('lang', 'en')),
        )

        if 'plugins' in self.options:
            plugins = self.options.get('plugins')
            for plugin in plugins:
                js = js + (
                    'redactor/plugins/{0}.js'.format(plugin),
                )

        css = {
            'all': (
                'redactor/css/redactor.css',
                'redactor/css/django_admin.css',
            )
        }
        return forms.Media(css=css, js=js)
    media = property(_media)
