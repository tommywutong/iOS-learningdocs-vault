---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOGenericRecordAdditions.html
archived_at: '2026-07-18T01:28:16.560370Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOEntityClassDescription-2.md)
[!](EOJoin-2.md)

---

# EOGenericRecord Additions

__Inherits From:__
NSObject

__Declared in:__
EOAccess/EOGenericRecord.h

---

## Class Description

The access layer adds one method to the control layer's EOGenericRecord class, for returning a generic record's associated EOEntity. Strictly speaking, EOGenericRecord doesn't rely on the access layer. However, in applications that access a relational database, the access layer's modeling objects are an important part of how generic records map to database rows: If an EOModel doesn't have a custom enterprise object class defined for a particular entity, an EODatabaseChannel using that model creates EOGenericRecords when fetching objects for that entity from the database server. During this process, an EODatabaseChannel also sets each generic record's `classDescription` to an EOEntityClassDescription, providing the link to the record's associated modeling objects.

---

## Instance Methods

---

### entity

- (EOEntity \*)`entity`

Returns the receiver's EOEntity.

---

[!](EOEntityClassDescription-2.md)
[!](EOJoin-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
