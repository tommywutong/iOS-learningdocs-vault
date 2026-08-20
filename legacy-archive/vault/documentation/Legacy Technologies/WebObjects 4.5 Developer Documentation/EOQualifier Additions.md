---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOQualifierAdditions.html
archived_at: '2026-07-15T08:11:33.771687Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EOQualifier Additions

> __Category
> of:__ EOQualifier

> __Declared in:__  EOAccess/EOSQLQualifier.h

---

## Category Description

---

The access layer adds one method to the EOQualifier class,
for "rerooting" a qualifier to another entity. EOQualifiers
(except EOSQLQualifier) aren't based on SQL and they don't rely
upon an EOModel. Because this method reroots a qualifier in terms
of model objects, it is only useful to the classes in the access
layer. It is not used in in-memory searches.

## Instance Methods

---

### qualifierMigratedFromEntity:relationshipPath:

`- (EOQualifier *)qualifierMigratedFromEntity:(EOEntity
*)entity
relationshipPath:(NSString *)relationshipPath`

Creates a copy of the receiver, translates all
the copy's keys to work with the entity specified in _relationshipPath_,
and returns the copy. The receiver's keys are all specified in
terms of _entity_. For example, assume
that an Employee entity has a relationship to a Department entity
named "department". You could migrate a qualifier described
in terms of the Employee entity (department.name = ‘Finance',
for example) to a qualifier described in terms of the Department
entity (name = ‘Finance'). To do so, you send a __qualifierMigratedFromEntity:relationshipPath:__ message with
the Employee entity as the entity and "department" as the relationship
path.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
