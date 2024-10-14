# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader.processors import TakeFirst, MapCompose, Compose
from scrapy.loader import ItemLoader


def remove_line_breaks(value):
    return value.replace("\n", "")


def take_last(value):
    return value[-1]


class MovieItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    duration_in = MapCompose(remove_line_breaks)
    original_title_in = Compose(take_last)


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    duration = scrapy.Field()
    original_title = scrapy.Field()
