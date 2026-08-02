---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOGlobalID.html
archived_at: '2026-07-15T08:13:46.938920Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOGlobalID

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : Cloneable: Serializable

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

An EOGlobalID is a compact, universal identifier for a persistent object, forming the basis for uniquing in Enterprise Objects Framework. An EOGlobalID uniquely identifies the same object or record both between EOEditingContexts in a single application and in multiple applications (as in distributed systems). EOGlobalID is an abstract class, declaring only the methods needed for identification. A concrete subclass must define appropriate storage for identifying values (such as primary keys), as well as an initialization or creation method to build IDs. See the EOKeyGlobalID class specification for an example of a concrete ID class.

## Temporary Identifiers

EOEditingContexts and other object stores support the insertion of new objects without established IDs, creating temporary IDs that get replaced with permanent ones as soon as the new objects are saved to their persistent stores. The temporary IDs are instances of the EOTemporaryGlobalID class.

When an EOObjectStore saves these newly inserted objects, it must replace the temporary IDs with persistent ones. When it does this, it must post an [GlobalIDChangedNotification](#apple-inbukqsjifeee) announcing the change so that observers can update their accounts of which objects are identified by which global IDs. The notification's userInfo dictionary contains a mapping from the temporary IDs (the keys) to their permanent replacements (the values).

## Constants

---

EOGlobalIDdefines String constants for the names of the notifications it posts. For more information, see the section ["Notifications" (page 232)](#apple-inbukqsbivdus) below.

## Interfaces Implemented

---

> : Cloneable: [clone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpi5wg6ytbnreuil3dnrxw4zi):

## Constructors

---

### EOGlobaIID

`public EOGlobalID()`

Description forthcoming.

---

## Instance Methods

---

### clone

`public Object clone()`

Conformance to Cloneable.

---

### __equals__

`public abstract boolean equals(Object anObject)`

Description forthcoming.

---

### __hashCode__

`public abstract int hashCode()`

Description forthcoming.

---

### isTemporary

`public boolean isTemporary()`

Returns false. See the class description for more information.

---

## Notifications

---

### GlobalIDChangedNotification

`public static final String GlobalIDChangedNotification`

Posted whenever EOTemporaryGlobalIDs are replaced by permanent EOGlobalIDs. The notification contains:

|  |  |
| --- | --- |
| Notification Object | __null__ |
| Userinfo | A mapping from the temporary IDs (keys) to permanent IDs (values) |

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
