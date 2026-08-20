---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOAccessArrayFaultHandler.html
archived_at: '2026-07-18T01:28:15.072329Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](The%20EOAccess%20Framework-2.md)
[!](EOAccessFaultHandler-2.md)

---

# EOAccessArrayFaultHandler

__Inherits From:__
EOAccessGenericFaultHandler :EOFaultHandler (EOControl) : NSObject

__Declared in:__
EOAccess/EOAccessFault.h

---

## Class Description

EOAccessArrayFaultHandler is a subclass of [EOAccessGenericFaultHandler](EOAccessGenericFaultHandler-2.md) that implements a fault for an array of enterprise objects.

---

## Instance Methods

---

### completeInitializationOfObject

- (void)completeInitializationOfObject:(id)object;

Asks the receiver's database context to fetch the object if it is not already in memory. This method is called when the fault is fired and uses the EOObjectStore protocol to get the information from the reciever's editing context

---

### databaseContext

- (EODatabaseContext \*)`databaseContext`

Returns the receiver's database context.

---

### editingContext

- (EOEditingContext \*)`editingContext`

Returns the receiver's editing context.

---

### initWithSourceGlobalID:relationshipName:databaseContext:editingContext:

- `initWithSourceGlobalID:`(EOKeyGlobalID \*)_sourceGID_
`relationshipName:`(NSString \*)_relationshipName_
`databaseContext:`(EODatabaseContext \*)_databaseContext_
`editingContext:`(EOEditingContext \*)_editingContext_

Initializes the handler with all of the information necessary to fetch the appropriate objects when the fault is fired. When the fault is fired, the database context asks the editing context for the required objects using the EOObjectStore protocol.

---

### relationshipName

- (NSString \*)`relationshipName`

Returns the receiver's relationship name.

---

### sourceGlobalID

- (EOKeyGlobalID \*)`sourceGlobalID`

Returns the receiver's source global ID.

---

[!](The%20EOAccess%20Framework-2.md)
[!](EOAccessFaultHandler-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
