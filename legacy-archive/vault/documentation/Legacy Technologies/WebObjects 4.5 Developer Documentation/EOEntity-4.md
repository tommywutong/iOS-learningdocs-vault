---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/More/EOEntity.html
archived_at: '2026-07-15T08:11:35.821191Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md)

# EOEntity

## Creating an Entity

An EOEntity requires at least the following to be usable:

- A name
- The name of a table in the database (the external name)
- The name of an enterprise object class
- A set of attributes to be used as the primary key

Note that if an entity has no enterprise object class name,
the database-level objects use EOGenericRecord.

This code excerpt gives an example of creating an EOEntity
and adding it to an EOModel:

> ```
> EOModel *myModel;          /* Assume this exists. */
> NSArray *keyAttributes;    /* Assume this exists. */
> EOEntity *employeeEntity;
> BOOL result;
>
> employeeEntity = [[[EOEntity alloc] init] autorelease];
> [employeeEntity setName:@"employee"];
> [employeeEntity setExternalName:@"EMPLOYEE"];
> [employeeEntity setClassName:@"Employee"];
>
> /* Create at least the primary key attributes. */
> result = [employeeEntity setPrimaryKeyAttributes:keyAttributes];
>
> /* Add the entity to the model. */
> [myModel addEntity:employeeEntity];
> ```

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md)
