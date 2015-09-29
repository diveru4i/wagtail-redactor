# -*- coding: utf-8 -*-
from django.utils.html import format_html, format_html_join
from django.conf import settings

from wagtail.wagtailcore import hooks


@hooks.register('insert_editor_js')
def redactor_media():
    js = [
        '/static/redactor/codemirror/lib/codemirror.js',
        '/static/redactor/codemirror/mode/xml/xml.js',
        '/static/redactor/codemirror/addon/edit/matchtags.js',
        '/static/redactor/codemirror/addon/fold/xml-fold.js',
        '/static/redactor/redactorWithCodemirror.init.js',
        '/static/redactor/redactor.js',
        '/static/redactor/langs/ru.js',
        '/static/redactor/redactor_init_hook.js',
    ]
    css = [
        '/static/redactor/codemirror/lib/codemirror.css',
        '/static/redactor/css/redactor.css',
        '/static/redactor/css/django_admin.css',
        '/static/redactor/css/admin_styles.css',
    ]

    js_includes = '\n'.join(['<script type="text/javascript" src="%s"></script>' % filename for filename in js])
    css_includes = '\n'.join(['<link type="text/css" rel="stylesheet" href="%s">' % filename for filename in css])

    return js_includes + css_includes
