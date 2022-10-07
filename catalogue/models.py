from django.db import models


class Category(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(
        max_length=32,
        verbose_name='название',
        help_text='Макс. 32 символов'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='публикация'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категория'
        db_table = 'catalogue_categories'
        ordering = ('id',)

class SubCategory(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(
        max_length=32,
        verbose_name='наименование',
        help_text='Максю 32 символа'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='род. категория'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='публикация'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'catalogue_subcategories'
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегория'
        ordering = ('category', 'id')
