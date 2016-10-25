Wagtail Redactor
========================

Fork of [django-wysiwyg-redactor](https://github.com/douglasmiranda/django-wysiwyg-redactor), that works with WagtailCMS.

## Requirements

- wagtail>=1.5

This package comes with [Codemirror](https://codemirror.net/)

## What's inside

- wagtail_redactor.fields.RedactorField - Django field
- wagtail_redactor.blocks.RedactorFieldBlock - Wagtail StreamField block

## Quick start

* Install:
    ```
       pip install -e git+https://github.com/diveru4i/wagtail-redactor.git#egg=wagtail_redactor
    ```
* Add "wagtail_redactor" to your INSTALLED_APPS
    ```python
       INSTALLED_APPS = (
           ...
           'wagtail_redactor',
           ...

       )
    ```
*. Add url(r'^redactor/', include(wagtail_redactor.urls)), to urls.py
```python
import wagtail_redactor.urls

urlpatterns = [
    # ...
    url(r'^redactor/', include(wagtail_redactor.urls)),
    # ...
]
```
* Add default config in settings.py
```python
REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = 'uploads/'
FILE_UPLOAD_PERMISSIONS = 0644
```
* If you wish to use RedactorFieldBlock as part of a more complex StreamField block, you should add ```icon-redactor``` to it's Meta:
```python
class MoreComplexBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    text = RedactorFieldBlock(label=u'Text', required=False)

    class Meta:
        icon = 'pick icon-redactor'
```

## Documentation
 - [WagtailCMS](https://github.com/torchbox/wagtail)
 - [django-wysiwyg-redactor](https://github.com/douglasmiranda/django-wysiwyg-redactor)
 - [Imperavi Redactor](http://imperavi.com/redactor/)
