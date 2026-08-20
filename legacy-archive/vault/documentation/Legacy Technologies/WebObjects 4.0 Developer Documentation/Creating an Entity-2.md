---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/More/CreatingAnEntity.html
archived_at: '2026-07-18T01:28:17.685780Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOEntity-2.md)
[!](EOEntityClassDescription-2.md)

---

# Creating an Entity

An EOEntity requires at least the following to be usable:

- A name
- The name of a table in the database (the external name)
- The name of an enterprise object class
- A set of attributes to be used as the primary key

Note that if an entity has no enterprise object class name, the database-level objects use EOGenericRecord. This code excerpt gives an example of creating an EOEntity and adding it to an EOModel:
> ```
> EOModel *myModel;          /* Assume this exists. */NSArray *keyAttributes;    /* Assume this exists. */EOEntity *employeeEntity;BOOL result;employeeEntity = [[[EOEntity alloc] init] autorelease];[employeeEntity setName:@"employee"];[employeeEntity setExternalName:@"EMPLOYEE"];[employeeEntity setClassName:@"Employee"];/* Create at least the primary key attributes. */result = [employeeEntity setPrimaryKeyAttributes:keyAttributes];/* Add the entity to the model. */[myModel addEntity:employeeEntity];
> ```

****

---

[!](EOEntity-2.md)
[!](EOEntityClassDescription-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
