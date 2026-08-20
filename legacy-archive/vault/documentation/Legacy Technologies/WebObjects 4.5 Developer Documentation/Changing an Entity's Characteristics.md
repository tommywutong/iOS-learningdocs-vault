---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/EOTools/Entities1.html
archived_at: '2026-07-15T08:03:56.116087Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Tools and Techniques

[!Table of Contents](Working%20with%20Entities.md) [!Previous Section](Working%20with%20Entities.md)

# Changing an Entity's Characteristics

To display a model's entities in table mode, select the model (the first icon) in the tree view.

!

Figure 34. Displaying an Entity's Attributes

Each table column corresponds to a single characteristic of an entity, such as its name or the name of its database table. By default, the columns included in the table-Open Entity, Name, Table, and Class Name-only represent a subset of the possible characteristics you can set for a given entity. To add columns for additional characteristics, you use the Add Column menu in the lower left corner of the table.
The following table describes the characteristics you can set for an entity in the Model Editor.

|  Characteristic |  What it is |
|  Class Name |  The name of the class that corresponds to the entity. If you don't define a custom enterprise object class for an entity, by default its class is EOGenericRecord. |
|  Client-Side Class Name |  The name of the class that corresponds to the entity in the client-side of a Java Client application. If you don't define a client-side class, the Framework looks for a class in the client with the same name as the server-side enterprise object class. If no such class exists on the client, it uses EOGenericRecord. |
|  External Query |  Any SQL statement that will be executed as is-on Sybase, this can be a stored procedure. |
|  Name |  The name your application uses for the entity. By default, EOModeler supplies a name based on the name of the corresponding table in the database. |
|  Open Entity |  Adds a column with the Open Entity icon, which you can double-click on to display an entity's attributes. |
|  Parent |  Indicates an entity's parent-used to model inheritance. |
|  Read Only |  Indicates whether the entity is read-only or not. |
|  Table |  The name of the database table that corresponds to the entity. |

```
```


__Note:__  There are numerous other characteristics that you set using the Entity Inspectors

[!Table of Contents](Working%20with%20Entities.md) [!Next Section](Using%20the%20Entity%20Inspector.md)
