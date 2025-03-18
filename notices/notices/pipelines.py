# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class NoticesPipeline:
    def process_item(self, item, spider):
        return item

class CnpqPipeline:
    def process_item(self, item, spider):
        if isinstance(item, str):
            # Log or handle the unexpected string item
            spider.logger.warning(f"Unexpected string item: {item}")
            return item

        adapter = ItemAdapter(item)
        
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name == 'description':
                description = adapter['description']
                transformed_description = []
                for desc_item in description:
                    if desc_item.startswith('\n') and transformed_description:
                        transformed_description[-1] += desc_item.strip()
                    else:
                        transformed_description.append(desc_item)
                adapter['description'] = transformed_description
        return item
