---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOAccessArrayFaultHandler.html
archived_at: '2026-07-18T01:28:07.728213Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](The%20EOAccess%20Framework.md)
[!](EOAccessFaultHandler.md)

---

# EOAccessArrayFaultHandler

__Inherits From:__
EOAccessGenericFaultHandler : com.apple.yellow.eocontrol.EOFaultHandler :
NSObject

__Inherits From:__
com.apple.yellow.eoaccess

---

## Class Description

EOAccessArrayFaultHandler is a subclass of [EOAccessGenericFaultHandler](EOAccessGenericFaultHandler.md) that implements a fault for an array of enterprise objects.

---

## Constructors

---

### EOAccessArrayFaultHandler

public `EOAccessArrayFaultHandler`()

Returns an uninitialized array fault handler.

public `EOAccessArrayFaultHandler`(com.apple.yellow.eocontrol.EOKeyGlobalID _sourceGID_,
java.lang.String _relationshipName_,
EODatabaseContext _databaseContext_,
com.apple.yellow.eocontrol.EOEditingContext _editingContext_)

Returns a handler initialized with all of the information necessary to fetch the appropriate objects when the fault is fired. When the fault is fired, the database context asks the editing context for the required objects using the EOObjectStore protocol.

---

## Instance Methods

---

### completeInitializationOfObject

public void `completeInitializationOfObject`(java.lang.Object _anObject_)

Asks the receiver's database context to fetch the object if it is not already in memory. This method is called when the fault is fired and uses the EOObjectStore protocol to get the information from the reciever's editing context

---

### databaseContext

public EODatabaseContext `databaseContext`()

Returns the receiver's database context.

---

### editingContext

public com.apple.yellow.eocontrol.EOEditingContext `editingContext`()

Returns the receiver's editing context.

---

### relationshipName

public java.lang.String `relationshipName`()

Returns the receiver's relationship name.

---

### sourceGlobalID

public com.apple.yellow.eocontrol.EOKeyGlobalID `sourceGlobalID`()

Returns the receiver's source global ID.

---

[!](The%20EOAccess%20Framework.md)
[!](EOAccessFaultHandler.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
