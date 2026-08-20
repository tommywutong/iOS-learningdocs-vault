---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOAccessFaultHandler.html
archived_at: '2026-07-15T08:11:33.290832Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOAccessFaultHandler

> __Inherits
> from:__  [EOAccessGenericFaultHandler](EOAccessGenericFaultHandler-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5awgy3fonzuozlomvzgsy2gmf2wy5cimfxgi3dfoi) : EOFaultHandler (EOControl) : NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  EOAccess/EOAccessFault.h

---

## Class Description

---

EOAccessFaultHandler is a subclass of [EOAccessGenericFaultHandler](EOAccessGenericFaultHandler-2.md#apple-ivhucy3dmvzxgr3fnzsxe2ldizqxk3dujbqw4zdmmvza) that
implements an object fault for enterprise objects.

## Instance Methods

---

### completeInitializationOfObject

`- (void)completeInitializationOfObject:(id)anObject`

Asks the receiver's database context to fetch _anObject_ if
it is not already in memory. This method is called when the fault
is fired and uses the EOObjectStore protocol to get the information
from the receiver's editing context.

---

### databaseContext

`- (EODatabaseContext *)databaseContext`

Returns the receiver's database context.

---

### editingContext

`- (EOEditingContext *)editingContext`

Returns the receiver's editing context.

---

### globalID

`- (EOKeyGlobalID *)globalID`

Returns the receiver's global ID.

---

### initWithglobalID:relationshipName:databaseContext:editingContext:

`- initWithGlobalID:(EOKeyGlobalID
*)globalID databaseContext:(EODatabaseContext
*)databaseContext
editingContext:(EOEditingContext
*)editingContext`

Initializes the handler with all of the information
necessary to fetch the object when the fault is fired. When the
fault is fired, this object calls [completeInitializationOfObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmnrwk43tizqxk3dujbqw4zdmmvzc6y3pnvygyzlumvew42lunfqwy2l2mf2gs33oj5te6ytkmvrxi) on
the object.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
