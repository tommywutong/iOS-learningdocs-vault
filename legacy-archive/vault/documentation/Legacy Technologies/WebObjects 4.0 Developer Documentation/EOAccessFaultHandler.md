---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOAccessFaultHandler.html
archived_at: '2026-07-18T01:28:08.381333Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOAccessArrayFaultHandler.md)
[!](EOAccessGenericFaultHandler.md)

---

# EOAccessFaultHandler

__Inherits From:__
EOAccessGenericFaultHandler : com.apple.yellow.eocontrol.EOFaultHandler :
NSObject

__Inherits From:__
com.apple.yellow.eoaccess

---

## Class Description

EOAccessFaultHandler is a subclass of [EOAccessGenericFaultHandler](EOAccessGenericFaultHandler.md) that implements an object fault for enterprise objects.

---

## Constructors

---

### EOAccessFaultHandler

public `EOAccessFaultHandler`()

Returns an uninitialized array fault handler.

public `EOAccessFaultHandler`(com.apple.yellow.eocontrol.EOKeyGlobalID _globalID_,
EODatabaseContext _databaseContext_,
com.apple.yellow.eocontrol.EOEditingContext _editingContext_)

Returns a handler initialized with all of the information necessary to fetch the object when the fault is fired.

---

## Instance Methods

---

### completeInitializationOfObject

public void `completeInitializationOfObject`(java.lang.Object _anObject_)

Asks the receiver's database context to fetch _anObject_ if it is not already in memory. This method is called called when the fault is fired and uses the EOObjectStore protocol to get the information from the receiver's editing context.

---

### databaseContext

public EODatabaseContext `databaseContext`()

Returns the receiver's database context.

---

### editingContext

public com.apple.yellow.eocontrol.EOEditingContext `editingContext`()

Returns the receiver's editing context.

---

### globalID

public com.apple.yellow.eocontrol.EOKeyGlobalID `globalID`()

Returns the receiver's global ID.

---

### 

---

[!](EOAccessArrayFaultHandler.md)
[!](EOAccessGenericFaultHandler.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
