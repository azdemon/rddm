from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _



class Templates(models.Model):
    title = models.CharField(max_length=50, verbose_name = _('Title'))
    file = models.FileField(_("Members"), upload_to='templates', max_length=100)
    headerfont = models.CharField(_("Header font"), max_length=50)
    headersize = models.IntegerField(_("Header size"))
    headermtop = models.IntegerField(_("Header Margin Top"))
    headerln = models.IntegerField(_("Header line height"))
    textfont = models.CharField(_("Text font"), max_length=50)
    textsize = models.IntegerField(_("Text size"))
    textmtop = models.IntegerField(_("Text Margin Top"))
    textln = models.IntegerField(_("Text line height"))

    class Meta:
        verbose_name = _("Template")
        verbose_name_plural = _("Templates")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Templates_detail", kwargs={"pk": self.id})


class Events(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    template = models.ForeignKey(Templates, verbose_name=_("Template"), on_delete=models.CASCADE, null=True)
    userlist = models.FileField(_("Members"), upload_to='members', max_length=100, blank=True)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Events_detail", kwargs={"pk": self.pk})


class Fields(models.Model):
    template = models.ForeignKey(Events, verbose_name=_("Events"), on_delete=models.CASCADE)
    text = models.CharField(_("Text"), max_length=200)

    class Meta:
        verbose_name = _("Field")
        verbose_name_plural = _("Fields")

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("Fields_detail", kwargs={"pk": self.pk})
