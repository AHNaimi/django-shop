from django.db import models


class CategoryModel(models.Model):
    """ a model for classify products """
    cat_name = models.CharField(max_length=100)
    cat_description = models.TextField()
    cat_slug = models.SlugField()
    cat_sub = models.ForeignKey('self', on_delete=models.CASCADE, related_name='cat_model', null=True, blank=True)
    cat_is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.cat_name} with {self.id} id'


class ProductModel(models.Model):
    """ a model for store products """
    pro_name = models.CharField(max_length=100)
    pro_cat = models.ManyToManyField(CategoryModel, related_name='pro_model')
    pro_price = models.CharField(max_length=100)
    pro_desc = models.TextField()
    pro_active = models.BooleanField(default=False)
    pro_numb = models.SmallIntegerField()
    pro_slug = models.SlugField(unique=True)
    pro_image = models.ImageField(upload_to='pro_image')
    pro_sizes = models.CharField(max_length=255, help_text='separate sizes with comma (,)', blank=True, null=True)




