from django.db import models


class Menu(models.Model):
    name = models.CharField(verbose_name="Название", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

class Item(models.Model):
    name = models.CharField(verbose_name="Название", max_length=200)
    parent_id = models.ForeignKey("self", verbose_name="id Родителя", null=True, blank=True)
    menu_id = models.ForeignKey(Menu, verbose_name="id Меню")
    url = models.CharField(verbose_name="URL", max_length=200)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
