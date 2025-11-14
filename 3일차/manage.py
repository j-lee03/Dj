#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.db import models

class Blog(models.Model):
    category=modls.charField('카테고리',max_length=20)
    title=models.CharField('제목',max_length=100)
    content=models.TexField('본문')

    created_at=models.DateTimeField('수령일자',auto_niw_add=True)
    updated_at-mode






