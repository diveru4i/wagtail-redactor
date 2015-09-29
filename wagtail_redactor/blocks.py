# -*- coding: utf-8 -*-
from wagtail.wagtailcore import blocks

from .fields import RedactorField


class RedactorFieldBlock(blocks.FieldBlock):
    def __init__(self, **kwargs):
        self.field = RedactorField()
        super(RedactorFieldBlock, self).__init__(**kwargs)

    class Meta:
        icon = 'pilcrow icon-redactor'
        template = 'redactor.html'
