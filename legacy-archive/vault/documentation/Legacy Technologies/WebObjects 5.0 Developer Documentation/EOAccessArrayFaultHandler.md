---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EOAccessArrayFaultHandler.html
archived_at: '2026-07-15T08:13:40.779085Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOAccessArrayFaultHandler

> **__Inherits from:__**
> : [EOAccessGenericFaultHandler](EOAccessGenericFaultHandler.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhucy3dmvzxgr3fnzsxe2ldizqxk3dujbqw4zdmmvza)

> **__Package:__**
> : com.webobjects.eoaccess

---

## Class Description

---

EOAccessArrayFaultHandler is a subclass of EOAccessGenericFaultHandler that implements a fault for an array of enterprise objects.

## Constructors

---

### EOAccessArrayFaultHandler

`public EOAccessArrayFaultHandler( com.webobjects.eocontrol.EOKeyGlobalID sourceGID, String relationshipName, EODatabaseContext databaseContext, com.webobjects.eocontrol.EOEditingContext editingContext)`

Returns a handler initialized with all of the information necessary to fetch the appropriate objects when the fault is fired. When the fault is fired, the database context asks the editing context for the required objects using the EOObjectStore protocol.

---

## Instance Methods

---

### completeInitializationOfObject

`public void completeInitializationOfObject(Object anObject)`

Asks the receiver's database context to fetch _anObject_ if it is not already in memory. This method is called when a fault is fired and uses the EOObjectStore interface to get the information from the receiver's editing context

---

### relationshipName

`public String relationshipName()`

Returns the receiver's relationship name.

---

### sourceGlobalID

`public com.webobjects.eocontrol.EOKeyGlobalID sourceGlobalID()`

Returns the receiver's source global ID.

---

### __toString__

`public String toString()`

Returns a String representation of the receiver.

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
