from django.db import models
from django.utils.timezone import now


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


class Product(models.Model):
    title = models.CharField(
        max_length=36,
        verbose_name='название',
        help_text='Макс. 36 символов'
    )
    descr = models.CharField(
        max_length=140,
        null=True,
        blank=True,
        verbose_name='описание',
        help_text='Макс. 140 символов'
    )
    article = models.CharField(
        max_length=16,
        unique=True,
        verbose_name='Артикль',
        help_text='Макс. 16 символов'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='публикация'
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        default=0,
        verbose_name='цена',
        help_text='Макс. 999999.99'
    )
    count = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='количество'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name='категория'
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name='картинка',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_products'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('price', 'title', 'article')


class Feedback(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='имя'
    )
    email = models.EmailField(
        verbose_name='почта'
    )
    phone_number = models.CharField(
        max_length=13,
        verbose_name='номер телефона'
    )
    message = models.CharField(
        max_length=140,
        verbose_name= 'сообщение'
    )
    date_created = models.DateTimeField(
        default=now(),
        verbose_name='дата публикации'
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'app_feedbacks'
        ordering = ('date_created', )
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'