---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOEntityClassDescription.html
archived_at: '2026-07-15T08:11:33.655448Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOEntityClassDescription

> __Inherits
> from:__  EOClassDescription : NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  EOAccess/EOEntity.h

---

## Class Description

---

EOEntityClassDescription is the subclass of the control layer's
EOClassDescription. The EOClassDescription class provides a mechanism
for extending classes by giving them access to metadata not available
in the run-time system. EOEntityClassDescription extends the behavior
of enterprise objects by deriving information about them (such as
NULL constraints and referential integrity rules) from an associated
EOModel. For detailed information on the methods, see the EOClassDescription
class specification.

In the typical scenario in which an enterprise object has
a corresponding model file, the first time a particular operation
is performed on a class (such as validating a value), an `EOClassDescriptionNeeded...` notification
(either an `EOClassDescriptionNeededForClassNotification` or
an `EOClassDescriptionNeededForEntityNameNotification`)
is broadcast. When an EOModel object receives this notification
it registers the metadata (class description) for the EOEntity on
which the enterprise object is based. This class description is
used from that point on.

## Instance Methods

---

### entity

`- (EOEntity *)entity`

Returns the entity associated with the receiver.

__See
Also:__  [- initWithEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzinwgc43tirsxgy3snfyhi2lpnyxws3tjorlws5diivxhi2lupe5a)

---

### initWithEntity:

`- initWithEntity:(EOEntity
*)anEntity`

Initializes a newly allocated EOEntityClassDescription
with _anEntity_. Returns __self__.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
