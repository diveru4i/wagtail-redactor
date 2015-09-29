Wagtail Redactor
========================

Wagtail's default WYSIWYG editor sucks balls (*by design*). Here's an attempt to integrate a better option into WagtailCMS - [Imperavi Redactor](http://imperavi.com/redactor/)

![proof](https://raw.githubusercontent.com/diveru4i/wagtail-redactor/master/screen.png)

## Requirements

- wagtail>=1.0
- django-wysiwyg-redactor==0.4.9

This package comes with [Codemirror](https://codemirror.net/)

## What's inside

- wagtail_redactor.fields.RedactorField - Django field
- wagtail_redactor.blocks.RedactorFieldBlock - Wagtail StreamField block

## Quick start

1. Install:
    ```
       pip install -e git+https://github.com/diveru4i/wagtail-redactor.git#egg=wagtail_redactor
    ```
2. Add "wagtail_redactor" to your INSTALLED_APPS
    ```python
       INSTALLED_APPS = (
           ...
           'wagtail_redactor',
           ...
           
       )
    ```
3. If you wish to use RedactorFieldBlock as part of a more complex StreamField block, you should add ```icon-redactor``` to it's Meta:
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
