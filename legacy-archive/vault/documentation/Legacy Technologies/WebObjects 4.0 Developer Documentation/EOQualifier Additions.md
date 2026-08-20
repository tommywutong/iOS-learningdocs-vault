---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOQualifierAdditions.html
archived_at: '2026-07-18T01:28:17.070996Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOObjectStoreCoordinator%20Additions.md)
[!](EORelationship-2.md)

---

# EOQualifier Additions

__Inherits From:__
NSObject

__Declared in:__
EOAccess/EOSQLQualifier.h

---

## Class Description

The access layer adds one method to the EOQualifier class, for "rerooting" a qualifier to another entity. EOQualifiers (except EOSQLQualifier) aren't based on SQL and they don't rely upon an EOModel. Because this method reroots a qualifier in terms of model objects, it is only useful to the classes in the access layer. It is not used in in-memory searches.

---

## Instance Methods

---

### qualifierMigratedFromEntity:relationshipPath:

- (EOQualifier \*)`qualifierMigratedFromEntity:`(EOEntity \*)_entity_`relationshipPath:`(NSString \*)_relationshipPath_

Creates a copy of the receiver, translates all the copy's keys to work with the entity specified in _relationshipPath_, and returns the copy. The receiver's keys are all specified in terms of _entity_. For example, assume that an Employee entity has a relationship to a Department entity named "department". You could migrate a qualifier described in terms of the Employee entity (department.name = `Finance', for example) to a qualifier described in terms of the Department entity (name = `Finance'). To do so, you send a `qualifierMigratedFromEntity:relationshipPath:` message with the Employee entity as the entity and "department" as the relationship path.

---

[!](EOObjectStoreCoordinator%20Additions.md)
[!](EORelationship-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
