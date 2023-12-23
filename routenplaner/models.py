from django.db import models
from django.utils.html import mark_safe
from django.utils.http import urlencode

# Create your models here.


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


class Route(models.Model):
    name = models.CharField("Name", max_length=50)

    def get_orte(self):
        return self.orte.filter(aktiv=True).order_by("pos")

    def get_google_maps_routes(self):
        url = "https://www.google.com/maps/dir/"
        urls = []
        for chunk in chunks([ort.adresse for ort in self.orte.all()], 9):
            urls.append(url + "/".join(chunk))
        print(urls)

    def __str__(self):
        return self.name
    __str__.short_description = "Route"

    class Meta:
        verbose_name = "Route"
        verbose_name_plural = "Routen"


class Ort(models.Model):
    pos = models.IntegerField("Position", default=0)
    aktiv = models.BooleanField("Aktiv", default=True)

    name = models.CharField("Name", max_length=50)
    adresse = models.CharField("Adresse", max_length=100)

    route = models.ForeignKey(
        Route, on_delete=models.CASCADE, related_name="orte")

    def get_maps_link(self):
        if self.pk:
            link = "https://maps.apple.com/?"
            args = urlencode(
                {
                    'daddr': self.adresse,
                    'dirflg': 'd'
                }
            )
            return link + args
        else:
            return "-"

    def html_link(self):
        if self.pk:
            html = ('<a href="' + self.get_maps_link() +
                    '" target="_blank">Maps</a>')
            print(html)
            return mark_safe(html)
        else:
            return "-"
    html_link.short_description = "Link"

    def html_adresse(self):
        return mark_safe(self.adresse.replace(",", "<br>"))

    def __str__(self):
        return self.name + " - " + self.adresse
    __str__.short_description = "Ort"

    class Meta:
        verbose_name = "Ort"
        verbose_name_plural = "Orte"
