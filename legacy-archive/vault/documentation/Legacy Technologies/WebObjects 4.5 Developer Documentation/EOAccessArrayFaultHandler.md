---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/EOAccessArrayFaultHandler.html
archived_at: '2026-07-15T08:11:31.439009Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOAccessArrayFaultHandler

> __Inherits
> from:__  [EOAccessGenericFaultHandler](EOAccessGenericFaultHandler.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhucy3dmvzxgr3fnzsxe2ldizqxk3dujbqw4zdmmvza) : EOFaultHandler (EOControl) : NSObject

> __Package:__ com.apple.yellow.eoaccess

---

## Class Description

---

EOAccessArrayFaultHandler is a subclass of [EOAccessGenericFaultHandler](EOAccessGenericFaultHandler.md#apple-ivhucy3dmvzxgr3fnzsxe2ldizqxk3dujbqw4zdmmvza) that
implements a fault for an array of enterprise objects.

## Constructors

---

### EOAccessArrayFaultHandler

`public EOAccessArrayFaultHandler(
com.apple.yellow.eocontrol.EOKeyGlobalID sourceGID,
String relationshipName,
EODatabaseContext databaseContext,
com.apple.yellow.eocontrol.EOEditingContext editingContext)`

Returns a handler initialized with all of the
information necessary to fetch the appropriate objects when the
fault is fired. When the fault is fired, the database context asks
the editing context for the required objects using the EOObjectStore
protocol.

---

## Instance Methods

---

### completeInitializationOfObject

`public void completeInitializationOfObject(Object anObject)`

Asks the receiver's database context to fetch _anObject_ if
it is not already in memory. This method is called when a fault
is fired and uses the EOObjectStore interface to get the information
from the receiver's editing context

---

### databaseContext

`public EODatabaseContext databaseContext()`

Returns the receiver's database context.

---

### editingContext

`public com.apple.yellow.eocontrol.EOEditingContext editingContext()`

Returns the receiver's editing context.

---

### relationshipName

`public String relationshipName()`

Returns the receiver's relationship name.

---

### sourceGlobalID

`public com.apple.yellow.eocontrol.EOKeyGlobalID sourceGlobalID()`

Returns the receiver's source global ID.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
