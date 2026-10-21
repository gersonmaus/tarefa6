from django.db import models


class Product(models.Model):
    name = models.CharField("Nome", max_length=100)
    description = models.TextField("Descrição", blank=True, null=True)
    price = models.DecimalField("Preço", max_digits=10, decimal_places=2)
    quantity = models.IntegerField("Quantidade", default=0)
    active = models.BooleanField("Ativo", default=True)
    created_at = models.DateTimeField("Data de cadastro", auto_now_add=True)

    def save(self, *args, **kwargs):
        self.name = self.name.strip().title()
        super().save(*args, **kwargs)

    def __str__(self):

        return self.name
