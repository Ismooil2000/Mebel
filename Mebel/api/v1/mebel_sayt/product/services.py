from collections import OrderedDict

from mebel_sayt.models import ProductImg


def prod_format(data):

    imgs = ProductImg.objects.filter(product=data)
    img = [x.img.path for x in imgs]
    return OrderedDict([
        ('id', data.id),
        ('name', data.name),
        ('ctg_id', data.ctg.id),
        ('ctg_content', data.ctg.content),
        ('ctg_slug', data.ctg.slug),
        ('img', img),
        ("price", data.price),
        ("color", data.color),
        ("material", data.material),
        ("fillIn", data.fillIn),
        ("is_bed", data.is_bed),
        ("wide", data.wide),
        ("height", data.height),
        ("bed_length", data.bed_length),
        ("bed_wide", data.bed_wide),
        ("bed_height", data.bed_height)
    ])
