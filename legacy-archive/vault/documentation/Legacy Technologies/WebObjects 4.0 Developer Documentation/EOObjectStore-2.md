---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOObjectStore.html
archived_at: '2026-07-18T01:28:36.764609Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EONull.md)
[!](EOObjectStoreCoordinator-2.md)

---

# EOObjectStore

__Inherits From:__
NSObject

__Conforms To:__ NSObject (NSObject)

__Declared in:__ EOControl/EOObjectStore.h

EOObjectStore is the abstract class that defines the API for an "intelligent" repository of objects, the control layer's object storage abstraction. An object store is responsible for constructing and registering objects, servicing object faults, and saving changes made to objects. For more information on the object storage abstraction, see ["Object Storage Abstraction"](The%20EOControl%20Framework-2.md) in the introduction to the EOControl Framework.

EOEditingContext is the principal EOObjectStore subclass and is used for managing objects in memory-in fact, the primary purpose of the EOObjectStore class is to define an API for servicing editing contexts, not to define a completely general API. Other subclasses of EOObjectStore are:

- [EOCooperatingObjectStore](EOCooperatingObjectStore-2.md)
- [EOObjectStoreCoordinator](EOObjectStoreCoordinator-2.md)
- [EODatabaseContext](EODatabaseContext-3.md)(EOAccess)

A subclass of EOObjectStore must implement all of its methods. The default implementations simply raise exceptions.

**Initializing objects**

**- initializeObject:withGlobalID:editingContext:**

**Getting objects**

**- objectsWithFetchSpecification:editingContext:

**- objectsForSourceGlobalID:relationshipName:editingContext:****

**Getting faults**

**- faultForGlobalID:editingContext:

**- arrayFaultWithSourceGlobalID:relationshipName:editingContext:

**- refaultObject:withGlobalID:editingContext:

**- faultForRawRow:entityNamed:editingContext:********

**Locking objects**

**- lockObjectWithGlobalID:editingContext:

**- isObjectLockedWithGlobalID:editingContext:****

**Saving changes to objects**

**- saveChangesInEditingContext:**

**Invalidating objects**

**- invalidateAllObjects

**- invalidateObjectsWithGlobalIDs:****

---

#### arrayFaultWithSourceGlobalID:relationshipName:editingContext:

- (NSArray \*)__arrayFaultWithSourceGlobalID:__ (EOGlobalID \*)_globalID___relationshipName:__ (NSString \*)_relationshipName___editingContext:__ (EOEditingContext \*)_anEditingContext_

Implemented by subclasses to return the destination objects for a to-many relationship, whether as real instances or as faults (EOFault objects). _globalID_ identifies the source object for the relationship (which doesn't necessarily exist in memory yet), and _relationshipName_ is the name of the relationship. The object identified by _globalID_ and the destination objects for the relationship all belong to _anEditingContext_.

If you implement this method to return a fault, you must define an EOFaultHandler subclass that stores _globalID_ and _relationshipName_, using them to fetch the objects in a later __objectsForSourceGlobalID:relationshipName:editingContext:__ message and that turns the fault into an array containing those objects. See the [EOFaultHandler](EOFaultHandler-2.md) and [EOFault](EOFault.md) class specifications for more information on faults.

See the [EOEditingContext](EOEditingContext-3.md) and EODatabaseContext (EOAccess) class specifications for more information on how this method works in concrete subclasses.

__See also:__ - __faultForGlobalID:editingContext:__

---

#### faultForGlobalID:editingContext:

- (id)__faultForGlobalID:__ (EOGlobalID \*)_globalID___editingContext:__ (EOEditingContext \*)_anEditingContext_

If the receiver is _anEditingContext_ and the object associated with _globalID_ is already registered in _anEditingContext_, this method returns that object. Otherwise it creates a to-one fault, registers it in _anEditingContext_, and returns the fault. This method is always directed first at _anEditingContext_, which forwards the message to its parent object store if needed to create a fault.

If you implement this method to return a fault (an EOFault object), you must define an EOFaultHandler subclass that stores _globalID_, uses it to fetch the object and turn the EOFault into that object, and initializes the object with EOObjectStore's __initializeObject:withGlobalID:editingContext:__ . See the [EOFaultHandler](EOFaultHandler-2.md) and [EOFault](EOFault.md) class specifications for more information on faults.

See the [EOEditingContext](EOEditingContext-3.md) and EODatabaseContext (EOAccess) class specifications for more information on how this method works in concrete subclasses.

__See also:__ - __arrayFaultWithSourceGlobalID:relationshipName:editingContext:__ , [- __recordObject: globalID:__](EOEditingContext-3.md)(EOEditingContext)

---

#### faultForRawRow:entityNamed:editingContext:

- (id)__faultForRawRow:__ (id)_row___entityNamed:__ (NSString \*)_entityName___editingContext:__ (EOEditingContext \*)_anEditingContext_

Returns a fault for the enterprise object corresponding to _row_, which is a dictionary of values containing at least the primary key of the corresponding enterprise object. This is especially useful if you have fetched raw rows and now want a unique enterprise object.

---

#### initializeObject:withGlobalID:editingContext:

- (void)__initializeObject:__ (id)_anObject___withGlobalID:__ (EOGlobalID \*)_globalID___editingContext:__ (EOEditingContext \*)_anEditingContext_

Implemented by subclasses to set _anObject_'s properties, as obtained for _globalID_. This method is typically invoked after _anObject_ has been created using EOClassDescription's __[createInstanceWithEditingContext:globalID:zone:](EOClassDescription-3.md)__ or using NSObject's __initWithEditingContext:classDescription:globalID:__ . This method is also invoked after a fault has been fired.

__See also:__ - __initWithEditingContext:classDescription:globalID:__ (NSObject Additions), - __awakeFromInsertionInEditingContext:__ (NSObject Additions), - __awakeFromFetchInEditingContext:__ (NSObject Additions)

---

#### invalidateAllObjects

- (void)__invalidateAllObjects__

Discards the values of all objects held by the receiver and turns them into faults (EOFault objects). This causes all locks to be dropped and any transaction to be rolled back. The next time any object is accessed, its data is fetched anew. Any child object stores are also notified that the objects are no longer valid. See the [EOEditingContext](EOEditingContext-3.md) class specification for more information on how this method works in concrete subclasses.

This method should also post an EOInvalidatedAllObjectsInStoreNotification.

__See also:__ - __invalidateObjectsWithGlobalIDs:__ , - __refaultObject:withGlobalID:editingContext:__

---

#### invalidateObjectsWithGlobalIDs:

- (void)__invalidateObjectsWithGlobalIDs:__ (NSArray \*)_globalIDs_

Signals that the objects identified by the EOGlobalIDs in _globalIDs_ should no longer be considered valid and that they should be turned into faults (EOFault objects). This causes data for each object to be refetched the next time it's accessed. Any child object stores are also notified that the objects are no longer valid.

__See also:__ - __invalidateAllObjects__ , - __refaultObject:withGlobalID:editingContext:__

---

#### isObjectLockedWithGlobalID:editingContext:

- (BOOL)__isObjectLockedWithGlobalID:__ (EOGlobalID \*)_globalID___editingContext:__ (EOEditingContext \*)_anEditingContext_

Returns YES if the object identified by _globalID_ is locked, NO if it isn't. See the EODatabaseContext (EOAccess) class specification for more information on how this method works in concrete subclasses.

---

#### lockObjectWithGlobalID:editingContext:

- (void)__lockObjectWithGlobalID:__ (EOGlobalID \*)_globalID___editingContext:__ (EOEditingContext \*)_anEditingContext_

Locks the object identified by _globalID_. See the EODatabaseContext (EOAccess) class specification for more information on how this method works in concrete subclasses.

---

#### objectsForSourceGlobalID:relationshipName:editingContext:

- (NSArray \*)__objectsForSourceGlobalID:__ (EOGlobalID \*)_globalID___relationshipName:__ (NSString \*)_relationshipName___editingContext:__ (EOEditingContext \*)_anEditingContext_

Returns the destination objects for a to-many relationship. This method is used by an array fault previously constructed using __arrayFaultWithSourceGlobalID:relationshipName:editingContext:__ . _globalID_ identifies the source object for the relationship (which doesn't necessarily exist in memory yet), and _relationshipName_ is the name of the relationship. The object identified by _globalID_ and the destination objects for the relationship all belong to _anEditingContext_.

See the [EOEditingContext](EOEditingContext-3.md) and EODatabaseContext (EOAccess) class specifications for more information on how this method works in concrete subclasses.

---

#### objectsWithFetchSpecification:editingContext:

- (NSArray \*)__objectsWithFetchSpecification:__ (EOFetchSpecification \*)_aFetchSpecification___editingContext:__ (EOEditingContext \*)_anEditingContext_

Fetches objects from an external store according to the criteria specified by _fetchSpecification_ and returns them in an array for inclusion in _anEditingContext_. If one of these objects is already present in memory, this method doesn't overwrite its values with the new values from the database. Raises an exception if an error occurs.

See the [EOEditingContext](EOEditingContext-3.md) and EODatabaseContext (EOAccess) class specifications for more information on how this method works in concrete subclasses.

---

#### refaultObject:withGlobalID:editingContext:

- (void)__refaultObject:__ (id)_anObject___withGlobalID:__ (EOGlobalID \*)_globalID___editingContext:__ (EOEditingContext \*)_anEditingContext_

Turns _anObject_ into a fault (an EOFault), identified by _globalID_ in _anEditingContext_. Objects that have been inserted but not saved, or that have been deleted, shouldn't be refaulted. When using the Yellow Box, use this method with caution since refaulting an object doesn't remove the object snapshot from the undo stack.

---

#### saveChangesInEditingContext:

- (void)__saveChangesInEditingContext:__ (EOEditingContext \*)_anEditingContext_

Saves any changes in _anEditingContext_ to the receiver's repository. Sends [__insertedObjects__](EOEditingContext-3.md), [__deletedObjects__](EOEditingContext-3.md), and [__updatedObjects__](EOEditingContext-3.md)messages to _anEditingContext_ and applies the changes to the receiver's data repository as appropriate. For example, EODatabaseContext (EOAccess) implements this method to send operations to an EOAdaptor (EOAccess) for making the changes in a database.

## Notification

---

### EOInvalidatedAllObjectsInStoreNotification

Posted whenever an EOObjectStore receives an __invalidateAllObjects__ message. The notification contains:

| __`Notification Object`__ | The EOObjectStore that received the __invalidateAllObjects__ message. |
| __Userinfo__ | None |

```
```


---

### EOObjectsChangedInStoreNotification

Posted whenever an EOObjectStore observes changes to its objects. The notification contains:

| __Notification Object__ | The EOObjectStore that observed the change. |
| Userinfo | Userinfo |
| __Key__ | __Value__ |
| updated | An NSArray of EOGlobalIDs for objects whose properties have changed. A receiving EOEditingContext typically responds by refaulting its corresponding objects. |
| inserted | An NSArray of EOGlobalIDs for objects that have been inserted into the EOObjectStore. |
| deleted | An NSArray of EOGlobalIDs for objects that have been deleted from the EOObjectStore. |
| invalidated | An NSArray of EOGlobalIDs for objects that have been turned into faults. |

```
```

---

[!](EONull.md)
[!](EOObjectStoreCoordinator-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
