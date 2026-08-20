---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOGlobalID.html
archived_at: '2026-07-15T08:11:39.825815Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOGlobalID

> **__Inherits
> from:__**
> : NSObject

> **__Conforms to:__**
> : NSCopying
> : NSObject (NSObject)

> __Declared in:__ : EOControl/EOGlobalID.h

---

## Class Description

---

An EOGlobalID is a compact, universal identifier for a persistent
object, forming the basis for uniquing in Enterprise Objects Framework.
An EOGlobalID uniquely identifies the same object or record both between
EOEditingContexts in a single application and in multiple applications
(as in distributed systems). EOGlobalID is an abstract class, declaring
only the methods needed for identification. A concrete subclass
must define appropriate storage for identifying values (such as
primary keys), as well as an initialization or creation method to
build IDs. See the [EOKeyGlobalID](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOKeyGlobalID.html#EOKeyGlobalID) class specification
for an example of a concrete ID class.

## Temporary Identifiers

EOEditingContexts and other object stores support the insertion
of new objects without established IDs, creating temporary IDs that
get replaced with permanent ones as soon as the new objects are
saved to their persistent stores. The temporary IDs are instances
of the [EOTemporaryGlobalID](EOTemporaryGlobalID-2.md#apple-ivhvizlnobxxeylspfdwy33cmfwesra) class.

When an EOObjectStore saves these newly inserted objects,
it must replace the temporary IDs with persistent ones. When it
does this, it must post an [EOGlobalIDChangedNotification](#apple-inbukqsjifeee) announcing
the change so that observers can update their accounts of which
objects are identified by which global IDs. The notification's
userInfo dictionary contains a mapping from the temporary IDs (the
keys) to their permanent replacements (the values).

## Constants

---

In EOGlobalID.h, EOControl defines NSString
constants for the names of the notifications it posts. For more
information, see the section ["Notifications"](#apple-inbukqsbivdus) below.

## Adopted Protocols

---

> NSCopying: __- copyWithZone:__

## Instance Methods

---

### isTemporary

`- (BOOL)isTemporary`

Returns NO. See the class description for more
information.

---

## Notifications

---

### EOGlobalIDChangedNotification

`EOCONTROL_EXTERN NSString *EOGlobalIDChangedNotification`

Posted whenever EOTemporaryGlobalIDs are
replaced by permanent EOGlobalIDs. The notification contains:

|  |  |
| --- | --- |
| Notification Object | __nil__ |
| Userinfo | A mapping from the temporary IDs (keys) to permanent IDs (values) |

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
