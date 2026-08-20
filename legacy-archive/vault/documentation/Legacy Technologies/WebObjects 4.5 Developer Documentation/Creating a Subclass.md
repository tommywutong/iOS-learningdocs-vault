---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/EOTools/Entities5.html
archived_at: '2026-07-18T01:29:07.852338Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Tools and Techniques

[!Table of Contents](Changing%20an%20Entity%27s%20Characteristics.md) [!Previous Section](Generating%20Source%20Files-2.md)

# Creating a Subclass

Enterprise Objects Framework supports mapping database tables to inheritance hierarchies of enterprise object classes using three different approaches. For one of the approaches-single table mapping-EOModeler provides support to help you model the mapping. In the single table mapping, all the enterprise object classes in the inheritance hierarchy map to the same database table; each class makes use, however, of different sets of the tables columns. Consequently, you need to create an entity for each enterprise object class in the hierarchy, and each of the entities map to the same table.EOModeler facilitates this by creating "subclass entities" and setting up the parent-child relationships for you.
To create a "subclass" entity, select the entity you want to use as the parent and choose Property ! Create Subclass. A new entity is created that maps to the same database table as the parent entity.
For more discussion of inheritance, see the chapter "Advanced Enterprise Object Modeling" in the book _Enterprise Objects Framework Developer's Guide_.

[!Table of Contents](Changing%20an%20Entity%27s%20Characteristics.md) [!Next Section](Setting%20Other%20Information%20for%20an%20Entity.md)
