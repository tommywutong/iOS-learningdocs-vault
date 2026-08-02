---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOGlobalID.html
archived_at: '2026-07-18T01:28:26.284920Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOGenericRecord.md)
[!](EOKeyComparisonQualifier.md)

---

# EOGlobalID

__Inherits From:__
Object (Java Client)
NSObject (Yellow Box)

__Implements:__
java.lang.Cloneable (Java Client only)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (WebObjects and Yellow Box)

## Class Description

An EOGlobalID is a compact, universal identifier for a persistent object, forming the basis for uniquing in Enterprise Objects Framework. An EOGlobalID uniquely identifies the same object or record both between EOEditingContexts in a single application and in multiple applications (as in distributed systems). EOGlobalID is an abstract class, declaring only the methods needed for identification. A concrete subclass must define appropriate storage for identifying values (such as primary keys), as well as an initialization or creation method to build IDs. See the [EOKeyGlobalID](EOKeyGlobalID.md) class specification for an example of a concrete ID class.

---

### Temporary Identifiers

EOEditingContexts and other object stores support the insertion of new objects without established IDs, creating temporary IDs that get replaced with permanent ones as soon as the new objects are saved to their persistent stores. The temporary IDs are instances of the [EOTemporaryGlobalID](EOTemporaryGlobalID.md) class.

When an EOObjectStore saves these newly inserted objects, it must replace the temporary IDs with persistent ones. When it does this, it must post an GlobalIDChangedNotification announcing the change so that observers can update their accounts of which objects are identified by which global IDs. The notification's __userInfo__ dictionary contains a mapping from the temporary IDs (the keys) to their permanent replacements (the values).

## Constants

The string constant, GlobalIDChangedNotification, defines the name of EOGlobalID's single notification. For more information, see the section "Notifications" below.

## Interfaces Implemented

**java.lang.Cloneable (Java Client only)**

## Instance Methods

---

#### isTemporary

public boolean __isTemporary__ ()

Returns __false__ . See the class description for more information.

## Notification

---

### GlobalIDChangedNotification

Posted whenever EOTemporaryGlobalIDs are replaced by permanent EOGlobalIDs. The notification contains:

| __`Notification Object`__ | __null__ |
| __Userinfo__ | A mapping from the temporary IDs (keys) to permanent IDs (values) |

```
```

---

[!](EOGenericRecord.md)
[!](EOKeyComparisonQualifier.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
