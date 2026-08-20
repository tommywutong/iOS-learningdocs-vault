---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EOAccessFaultHandler.html
archived_at: '2026-07-15T08:13:41.134587Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOAccessFaultHandler

> **__Inherits from:__**
> : [EOAccessGenericFaultHandler](EOAccessGenericFaultHandler.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhucy3dmvzxgr3fnzsxe2ldizqxk3dujbqw4zdmmvza)

> **__Package:__**
> : com.webobjects.eoaccess

---

## Class Description

---

EOAccessFaultHandler is a subclass of EOAccessGenericFaultHandler that implements an object fault for enterprise objects.

## Constructors

---

### EOAccessFaultHandler

`public EOAccessFaultHandler( com.webobjects.eocontrol.EOKeyGlobalID globalID, EODatabaseContext databaseContext, com.webobjects.eocontrol.EOEditingContext editingContext)`

Returns a handler initialized with all of the information necessary to fetch the object when the fault is fired.

---

## Instance Methods

---

### completeInitializationOfObject

`public void completeInitializationOfObject(Object anObject)`

Asks the receiver's database context to fetch _anObject_ if it is not already in memory. This method is called when the fault is fired and uses the EOObjectStore protocol to get the information from the receiver's editing context.

---

### __descriptionForObject__

`public String descriptionForObject(Object anObject)`

Description forthcoming.

---

### globalID

`public com.webobjects.eocontrol.EOKeyGlobalID globalID()`

Returns the receiver's global ID.

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
