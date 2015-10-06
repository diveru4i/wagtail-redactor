# -*- coding: utf-8 -*-
from wagtail.wagtailcore import blocks

from .fields import RedactorField


class RedactorFieldBlock(blocks.FieldBlock):
    def __init__(self, required=True, help_text=None, **kwargs):
        self.field = RedactorField(required=required, help_text=help_text)
        super(RedactorFieldBlock, self).__init__(required=required, help_text=help_text, **kwargs)

    class Meta:
        icon = 'pilcrow icon-redactor'
        template = 'redactor.html'

    def get_searchable_content(self, value):
        return [force_text(value)]
