from django.db import models

# Create your models here.


class Clinic(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название клиники",
    )
    booking_url = models.URLField(
        verbose_name="Ссылка для записи",
        help_text="https://ya.ru",
    )
    maps_app_url = models.CharField(
        verbose_name="Ссылка для Яндекс.Картах",
        help_text="https://ya.ru",
    )

    class Meta:
        verbose_name = "Клиника"
        verbose_name_plural = "Клиники"
        ordering = ["name"]

    def __str__(self) -> str:
        return str(self.name)

