---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOAccessFaultHandler.html
archived_at: '2026-07-18T01:28:15.125523Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOAccessArrayFaultHandler-2.md)
[!](EOAccessGenericFaultHandler-2.md)

---

# EOAccessFaultHandler

__Inherits From:__
EOAccessGenericFaultHandler :EOFaultHandler (EOControl) : NSObject

__Declared in:__
EOAccess/EOAccessFault.h

---

## Class Description

EOAccessFaultHandler is a subclass of [EOAccessGenericFaultHandler](EOAccessGenericFaultHandler-2.md) that implements an object fault for enterprise objects.

---

## Instance Methods

---

### completeInitializationOfObject

- (void)`completeInitializationOfObject:`(id)_anObject_;

Asks the receiver's database context to fetch _anObject_ if it is not already in memory. This method is called called when the fault is fired and uses the EOObjectStore protocol to get the information from the receiver's editing context.

---

### databaseContext

- (EODatabaseContext \*)`databaseContext`

Returns the receiver's database context.

---

### editingContext

- (EOEditingContext \*)`editingContext`

Returns the receiver's editing context.

---

### globalID

- (EOKeyGlobalID \*)`globalID`

Returns the receiver's global ID.

---

### initWithglobalID:relationshipName:databaseContext:editingContext:

- `initWithGlobalID:`(EOKeyGlobalID \*)_globalID_
`databaseContext:`(EODatabaseContext \*)_databaseContext_
`editingContext:`(EOEditingContext \*)_editingContext_

Initializes the handler with all of the information necessary to fetch the object when the fault is fired. When the fault is fired, this object calls [`completeInitializationOfObject`](#apple-g43dcmy) on the object.

---

### 

---

[!](EOAccessArrayFaultHandler-2.md)
[!](EOAccessGenericFaultHandler-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
