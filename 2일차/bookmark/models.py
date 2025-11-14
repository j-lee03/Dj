from django.db import models

# Create your models here.
class Bookmark(models.Model):
    name = models.CharField('이름',max_length=100)
    url = models.URLField('URL')
    credits_at = models.DateTimeField('생성일',auto_now_add=True)
    updated_at = models.DateTimeField('수정일',auto_now=True)

    class Meta:
        verbose_name = '북마크'
        verbose_name_plural = '북마크목록'












