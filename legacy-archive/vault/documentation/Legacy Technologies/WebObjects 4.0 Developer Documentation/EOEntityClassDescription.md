---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOEntityClassDescription.html
archived_at: '2026-07-18T01:28:09.915901Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](Creating%20an%20Entity.md)
[!](EOJoin.md)

---

# EOEntityClassDescription

__Inherits From:__
com.apple.yellow.eocontrol.EOClassDescription : NSObject

__Inherits From:__
com.apple.yellow.eoaccess

---

## Class Description

EOEntityClassDescription is the subclass of the control layer's EOClassDescription. The EOClassDescription class provides a mechanism for extending classes by giving them access to metadata not available in the run-time system. EOEntityClassDescription extends the behavior of enterprise objects by deriving information about them (such as NULL constraints and referential integrity rules) from an associated EOModel.

In the typical scenario in which an enterprise object has a corresponding model file, the first time a particular operation is performed on a class (such as validating a value), an EOClassDescriptionNeeded... notification (either an EOClassDescriptionNeededForClassNotification or an EOClassDescriptionNeededForEntityNameNotification) is broadcast. When an EOModel object receives this notification it registers the metadata (class description) for the EOEntity on which the enterprise object is based. This class description is used from that point on.

For a more detailed discussion of this subject, see the EOClassDescription class specification.

---

## Constructors

---

### EOEntityClassDescription

public `EOEntityClassDescription`()

public `EOEntityClassDescription`(next.eo.Entity _entity_)

Creates a new EOEntityClassDescription and assigns _entity_ to it.

__See also:__
[`entity`](#apple-giztq)

---

## Instance Methods

---

### entity

public next.eo.Entity `entity`()

Returns the entity associated with the receiver.

__See also:__
["Constructors"](#apple-geydanbv)

---

[!](Creating%20an%20Entity.md)
[!](EOJoin.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
