---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOGenericRecordAdditions.html
archived_at: '2026-07-15T08:11:33.669179Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EOGenericRecord Additions

> __Category
> of:__ EOGenericRecord

> __Declared in:__  EOAccess/EOGenericRecord.h

---

## Category Description

---

The access layer adds one method to the control layer's
EOGenericRecord class, for returning a generic record's associated
EOEntity. Strictly speaking, EOGenericRecord doesn't rely on the
access layer. However, in applications that access a relational
database, the access layer's modeling objects are an important
part of how generic records map to database rows: If an EOModel
doesn't have a custom enterprise object class defined for a particular
entity, an EODatabaseChannel using that model creates EOGenericRecords
when fetching objects for that entity from the database server.
During this process, an EODatabaseChannel also sets each generic
record's __classDescription__ to an EOEntityClassDescription,
providing the link to the record's associated modeling objects.

## Instance Methods

---

### entity

`- (EOEntity *)entity`

Returns the receiver's EOEntity.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
