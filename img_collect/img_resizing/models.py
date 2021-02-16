from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from PIL import Image as Im


class Image(models.Model):
    image_file = models.ImageField(blank=True, null=True, upload_to='images/')
    image_url = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if self.image_url and not self.image_file:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.image_url).read())
            img_temp.flush()
            self.image_file.save(f"image_{self.pk}", File(img_temp))
        super(Image, self).save(*args, **kwargs)

    def img_resizing(self):
        img = Im.open(self.image_file.path)
        output_size = (1000, 1000)
        img = img.resize(output_size, Im.ANTIALIAS)
        img.save(self.image_file.path)
        super(Image, self).save()


    '''def save2(self):
        new_img = (1142, 2200)
        img = Im.open(self.image_file.path).thumbnail(new_img)  # Open image using self
        super(Image, img).save()'''

    '''def save2(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
        img = Im.open(self.image_file.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image_file.path)'''