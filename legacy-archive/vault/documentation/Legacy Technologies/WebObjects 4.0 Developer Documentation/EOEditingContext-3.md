---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOEditingContext.html
archived_at: '2026-07-18T01:28:35.659136Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EODetailDataSource-2.md)
[!](EOEditingContext-4.md)

---

# EOEditingContext

__Inherits From:__
EOObjectStore : NSObject

__Conforms To:__ EOObserving
NSLocking

__Declared in:__ EOControl/EOEditingContext.h

---

### Class At a Glance:

**---

#### Purpose**

An EOEditingContext object manages a graph of enterprise objects in an application; this object graph represents an internally consistent view of one or more external stores (most often a database).

| __Principal Attributes__ |
| The set of enterprise objects managed by the EOEditingContext |
| The EOEditingContext's parent EOObjectStore |
| The set of EOEditor objects messaged by the EOEditingContext |
| The EOEditingContext's EOMessageHandler |

```
```

**---

####

| __`Creation`__ | __`Creation`__ |
| - initWithParentObjectStore: | Designated initializer. |

```
```

**---

####

| __Commonly Used Methods__ | __Commonly Used Methods__ |
| - objectsWithFetchSpecification: | Fetches objects from an external store. |
| - insertObject: | Registers a new object to be inserted into the parent EOObjectStore when changes are saved. |
| - deleteObject: | Registers that an object should be removed from the parent EOObjectStore when changes are saved. |
| - lockObject: | Attempts to lock an object in the external store. |
| - hasChanges | Returns YES if any of the receiver has any pending changes to the parent EOObjectStore. |
| - saveChanges | Commits changes made in the receiver to the parent EOObjectStore. |
| - revert | Removes everything from the undo stack, discards all insertions and deletions, and restores updated objects to their original values. |
| - objectForGlobalID: | Given a globalID, returns its associated object. |
| - globalIDForObject: | Given an object, returns its globalID. |
| - setDelegate: | Sets the receiver's delegate. |
| - parentObjectStore | Returns the receiver's parent EOObjectStore. |
| - rootObjectStore | Returns the receiver's root EOObjectStore. |

|  |
| --- |
|  |****

An EOEditingContext object represents a single "object space" or document in an application. Its primary responsibility is managing a graph of enterprise objects. This _object graph_ is a group of related business objects that represent an internally consistent view of one or more external stores (usually a database).

All objects fetched from an external store are registered in an editing context along with a global identifier (EOGlobalID) that's used to uniquely identify each object to the external store. The editing context is responsible for watching for changes in its objects (using the EOObserving protocol) and recording snapshots for object-based undo. A single enterprise object instance exists in one and only one editing context, but multiple copies of an object can exist in different editing contexts. Thus object uniquing is scoped to a particular editing context.

For more information on EOEditingContext, see the sections:

- [Other Classes that Participate in Object Graph Management](EOEditingContext-4.md)
- [Programmatically Creating an EOEditingContext](EOEditingContext-4.md)
- [Using EOEditingContexts in Different Configurations](EOEditingContext-4.md)
- [Fetching Objects](EOEditingContext-4.md)
- [Managing Changes in Your Application](EOEditingContext-4.md)
- [Methods for Managing the Object Graph](EOEditingContext-4.md)
- [General Guidelines for Managing the Object Graph](EOEditingContext-4.md)
- [Using EOEditingContext to Archive Custom Objects in Web Objects Framework](EOEditingContext-4.md)

## Constants

The following string constants name notifications EOEditingContext posts:

- EOEditingContextDidSaveChangesNotification
- EOObjectsChangedInEditingContextNotification

See the Notifications section for more information on the notifications.

The following string constants are the keys to the EOObjectsChangedInEditingContextNotification's user info dictionary:

- updated
- deleted
- inserted
- invalidated

EditingContextFlushChangesRunLoopOrdering, is an integer that defines the order in which the editing context performs end of event processing in __processRecentChanges__ . Messages with lower order numbers are processed before messages with higher order numbers. In an application built with the Application Kit, the constant order value schedules the editing context to perform its processing before the undo stack group is closed or window display is updated.

---

## Adopted Protocols

**EOObserving**

**[- objectWillChange:](EOObserving-2.md)**

**NSLocking**

**- lock

**- unlock****

**Initializing an EOEditingContext**

**- initWithParentObjectStore:**

**Controlling EOEditingContext's memory management strategy**

****

**Fetching objects**

**- objectsWithFetchSpecification:**

**Committing or discarding changes**

**- saveChanges

**- saveChanges:

**- tryToSaveChanges

**- refaultObjects

**- refault:

**- refetch:

**- revert

**- revert:

**- invalidateAllObjects******************

**Registering changes**

**- deleteObject:

**- insertObject:

**- insertObject:withGlobalID:

**- objectWillChange:

**- processRecentChanges**********

**Checking changes**

**- deletedObjects

**- insertedObjects

**- updatedObjects

**- hasChanges********

**Object registration and snapshotting**

**- forgetObject:

**- recordObject:globalID:

**- committedSnapshotForObject:

**- currentEventSnapshotForObject:

**- objectForGlobalID:

**- globalIDForObject:

**- registeredObjects**************

**Locking objects**

**- lockObject:

**- lockObjectWithGlobalID:editingContext:

**- isObjectLockedWithGlobalID:editingContext:

**- setLocksObjectsBeforeFirstModification:

**- locksObjectsBeforeFirstModification**********

**Undoing operations**

**- redo:

**- undo:

**- setUndoManager:

**- undoManager********

**Deletion and Validation Behavior**

**- setPropagatesDeletesAtEndOfEvent:

**- propagatesDeletesAtEndOfEvent

**- setStopsValidationAfterFirstError:

**- stopsValidationAfterFirstError********

**Returning related object stores**

**- parentObjectStore

**- rootObjectStore****

**Managing editors**

**- editors

**- addEditor:

**- removeEditor:******

**Setting the delegate**

**- setDelegate:

**- delegate****

**Setting the message handler**

**- setMessageHandler:

**- messageHandler****

**Invalidating objects**

**- setInvalidatesObjectsWhenFreed:

**- invalidatesObjectsWhenFreed****

**Locking**

**- lock**

**- unlockWorking with raw rows**

**- faultForRawRow:entityNamed:**

**Unarchiving from nib**

**+ defaultParentObjectStore

**+ setDefaultParentObjectStore:

**+ setSubstitutionEditingContext:

**+ substitutionEditingContext********

**Nested EOEditingContext support**

**- objectsWithFetchSpecification:editingContext:

**- objectsForSourceGlobalID:relationshipName:editingContext:

**- arrayFaultWithSourceGlobalID:relationshipName:editingContext:

**- faultForGlobalID:editingContext:

**- saveChangesInEditingContext:

**- refaultObject:withGlobalID:editingContext:

**- invalidateObjectsWithGlobalIDs:

**- initializeObject:withGlobalID:editingContext:****************

**Archiving and unarchiving objects**

**+ encodeObject:withCoder:

**+ initObject:withCoder:

**+ setUsesContextRelativeEncoding:

**+ usesContextRelativeEncoding********

---

#### defaultParentObjectStore

+ (EOObjectStore \*)`defaultParentObjectStore`

Returns the EOObjectStore that is the default parent object store for new editing contexts. Normally this is the EOObjectStoreCoordinator returned from the EOObjectStoreCoordinator class method [__defaultCoordinator__](EOObjectStoreCoordinator-2.md).

__See also:__ + __setDefaultParentObjectStore:__

---

#### encodeObject:withCoder:

+ (void)`encodeObject:`(id)_object_`withCoder:`(NSCoder \*)_encoder_

Invoked by an enterprise object _object_ to ask the EOEditingContext to encode _object_ using _encoder_. For more discussion of this subject, see ["Using EOEditingContext to Archive Custom Objects in Web Objects Framework"](EOEditingContext-4.md) in the class description.

__See also:__ + __initObject:withCoder:__ , + __setUsesContextRelativeEncoding:__ , + __usesContextRelativeEncoding__

---

#### initObject:withCoder:

+ (id)`initObject:`(id)_object_`withCoder:`(NSCoder \*)_decoder_

Invoked by an enterprise object _object_ to ask the EOEditingContext to initialize _object_ from data in _decoder_. For more discussion of this subject, see ["Using EOEditingContext to Archive Custom Objects in Web Objects Framework"](EOEditingContext-4.md) in the class description.

__See also:__ + __encodeObject:withCoder:__ , + __setUsesContextRelativeEncoding:__ , + __usesContextRelativeEncoding__

---

#### setDefaultParentObjectStore:

+ (void)`setDefaultParentObjectStore:`(EOObjectStore \*)_store_

Sets thedefault parent EOObjectStore to _store_. You use this method before loading a nib file to change the default parent EOObjectStores of the EOEditingContexts in the nib file. The object you supply for _store_ can be a different EOObjectStoreCoordinator or another EOEditingContext (if you're using a nested EOEditingContext). After loading a nib with an EOEditingContext substituted as the default parent EOObjectStore, you should restore the default behavior by setting the default parent EOObjectStore to `nil`. For example:

> ```
> [EOEditingContext setDefaultParentObjectStore:editingContext];
> nibLoaded = [NSBundle loadNibNamed:@"thirdNib" owner:self];
> [EOEditingContext setDefaultObjectStore:nil]; // Restore default
> ```

A default parent object store is global until it is changed again. For more discussion of this topic, see the chapter "Application Configurations" in the _Enterprise Objects Framework Developer's Guide_.

__See also:__ + __defaultParentObjectStore__

---

#### setSubstitutionEditingContext:

+ (void)`setSubstitutionEditingContext:`(EOEditingContext \*)_anEditingContext_

Assigns _anEditingContext_ as the EOEditingContext to substitute for the one specified in a nib file you're about to load. Using this method causes all of the connections in your nib file to be redirected to _anEditingContext_. This can be useful when you want an interface loaded from a second nib file to use an existing EOEditingContext. After loading a nib with a substitution EOEditingContext, you should restore the default behavior by setting the substitution EOEditingContext to `nil`. For example:

> ```
> [EOEditingContext setSubstitutionEditingContext:editingContext];
> nibLoaded = [NSBundle loadNibNamed:@"thirdNib" owner:self];
> [EOEditingContext setSubstitutionEditingContext:nil]; // Restore default
> ```

A substitution editing context is global until it is changed again. For more discussion of this topic, see the chapter "Application Configurations" in the _Enterprise Objects Framework Developer's Guide_.

__See also:__ + __substitutionEditingContext__

---

#### setUsesContextRelativeEncoding:

+ (void)`setUsesContextRelativeEncoding:`(BOOL)_flag_

Sets according to _flag_ whether __encodeObject:withCoder:__ uses context-relative encoding. For more discussion of this subject, see ["Using EOEditingContext to Archive Custom Objects in Web Objects Framework"](EOEditingContext-4.md) in the class description.

__See also:__ + __usesContextRelativeEncoding__ , + __encodeObject:withCoder:__ ,

---

#### substitutionEditingContext

+ (EOEditingContext \*)`substitutionEditingContext`

Returns the substitution EOEditingContext if one has been specified. Otherwise returns `nil`.

__See also:__ + __setSubstitutionEditingContext:__

---

#### usesContextRelativeEncoding

+ (BOOL)`usesContextRelativeEncoding`

Returns YES to indicate that __encodeObject:withCoder:__ uses context relative encoding, NO otherwise. For more discussion of this subject, see ["Using EOEditingContext to Archive Custom Objects in Web Objects Framework"](EOEditingContext-4.md) in the class description.

__See also:__ + __setUsesContextRelativeEncoding:__

---

#### addEditor:

- (void)`addEditor:`(id)_editor_

Adds _editor_ to the receiver's set of [EOEditors](EOEditors.md). For more explanation, see the method description for __editors__ and the [EOEditors](EOEditors.md) informal protocol specification.

__See also:__ `-` __removeEditor:__

---

#### arrayFaultWithSourceGlobalID:relationshipName:editingContext:

- (NSArray \*)`arrayFaultWithSourceGlobalID:`(EOGlobalID \*)_globalID_`relationshipName:`(NSString \*)_name_
`editingContext:`(EOEditingContext \*)_anEditingContext_

Overrides the implementation inherited from EOObjectStore. If the objects associated with the EOGlobalID _globalID_ are already registered in the receiver, returns those objects. Otherwise, propagates the message down the object store hierarchy, through the parent object store, ultimately to the associated EODatabaseContext. The EODatabaseContext creates and returns a to-many fault.

When a parent EOEditingContext receives this on behalf of a child EOEditingContext and the EOGlobalID _globalID_ identifies a newly inserted object in the parent, the parent returns a copy of its object's relationship array with the member objects translated into objects in the child EOEditingContext.

For more information on faults, see the EOObjectStore, EODatabaseContext (EOAccess), EOFault, and EOFaultHandler class specifications.

__See also:__ - __faultForGlobalID:editingContext:__

---

#### committedSnapshotForObject:

- (NSDictionary \*)`committedSnapshotForObject:`(id)_object_

Returns a dictionary containing a snapshot of _object_ that reflects its committed values (that is, its values as they were last committed to the database).In other words, this snapshot represents the state of the object before any modifications were made to it. The snapshot is updated to the newest object state after a save.

__See also:__ - __currentEventSnapshotForObject:__

---

#### currentEventSnapshotForObject:

- (NSDictionary \*)`currentEventSnapshotForObject:`(id)_object_

Returns a dictionary containing a snapshot of _object_ that reflects its state as it was at the beginning of the current event loop. After the end of the current event-upon invocation of __processRecentChanges__ -this snapshot is updated to hold the modified state of the object.

__See also:__ - __committedSnapshotForObject:__ , - __processRecentChanges__

---

#### delegate

- (id)`delegate`

Returns the receiver's delegate.

__See also:__ - __setDelegate:__

---

#### deleteObject:

- (void)`deleteObject:`(id)_object_

Specifies that _object_ should be removed from the receiver's parent EOObjectStore when changes are committed. At that time, the object will be removed from the uniquing tables.

__See also:__ - __deletedObjects__

---

#### deletedObjects

- (NSArray \*)`deletedObjects`

Returns the objects that have been deleted from the receiver's object graph.

__See also:__ `-` __updatedObjects__ , `-` __insertedObjects__

---

#### editors

- (NSArray \*)`editors`

Returns the receiver's editors. Editors are special-purpose delegate objects that may contain uncommitted changes that need to be validated and applied to enterprise objects before the EOEditingContext saves changes. For example, EODisplayGroups (EOInterface) register themselves as editors with the EOEditingContext of their data sources so that they can save any changes in the key text field. For more information, see the [EOEditors](EOEditors.md) informal protocol specification and the EODisplayGroup class specification.

__See also:__ `-` __addEditor:__ , `-` __removeEditor:__

---

#### faultForGlobalID:editingContext:

- (id)`faultForGlobalID:`(EOGlobalID \*)_globalID_`editingContext:`(EOEditingContext \*)_anEditingContext_

Overrides the implementation inherited from EOObjectStore. If the object associated with the EOGlobalID _globalID_ is already registered in the receiver, this method returns that object. Otherwise, the method propagates the message down the object store hierarchy, through the parent object store, ultimately to the associated EODatabaseContext. The EODatabaseContext creates and returns a to-one fault.

For example, suppose you want the department object whose __deptID__ has a particular value. The most efficient way to get it is to look it up by its globalID using __faultForGlobalID:editingContext:__ :

> ```
> EOEntity *entity = [[[editingContext rootObjectStore] modelGroup] entityNamed:entityName];
> EOGlobalID *gid = [entity globalIDForRow:[NSDictionary
>     dictionaryWithObjectsAndKeys:deptIdentifier, @"deptID", nil]];
> return [editingContext faultForGlobalID:gid editingContext:editingContext];
> ```

If the department object is already registered in the EOEditingContext, this code returns the object (without going to the database). If not, a fault for this object is created, and the object is fetched only when you trigger the fault.

In a nested editing context configuration, when a parent EOEditingContext is sent __faultForGlobalID:editingContext:__ on behalf of a child EOEditingContext and _globalID_ identifies a newly inserted object in the parent, the parent registers a copy of the object in the child.

For more discussion of this method, see the section ["Working with Objects Across Multiple EOEditingContexts"](EOEditingContext-4.md) in the class description. For more information on faults, see the EOObjectStore, EODatabaseContext (EOAccess), EOFault, and EOFaultHandler class specifications.

__See also:__ - __arrayFaultWithSourceGlobalID:relationshipName:editingContext:__

---

#### faultForRawRow:entityNamed:

- (id)`faultForRawRow:`(id)_row_`entityNamed:`(NSString \*)_entityName_

Returns a fault for the raw row _row_ by invoking [__faultForRawRow:entityNamed:editingContext:__](EOObjectStore-2.md)with __self__ as the editing context.

---

#### forgetObject:

- (void)`forgetObject:`(id)_object_

Removes _object_ from the uniquing tables and causes the receiver to remove itself as the object's observer. This method is invoked whenever an object being observed by an EOEditingContext is deallocated. Note that this method does _not_ have the effect of releasing and freeing the object. You should never invoke this method directly. The correct way to remove an object from its editing context is to remove every reference to the object by refaulting any object that references it (using __refaultObjects__ or __invalidateAllObjects__ ). Also note that this method does _not_ have the effect of deleting an object-to delete an object you should either use the __deleteObject:__ method or remove the object from an owning relationship.

---

#### globalIDForObject:

- (EOGlobalID \*)`globalIDForObject:`_object_

Returns the EOGlobalID for _object_. All objects fetched from an external store are registered in an EOEditingContext along with a global identifier (EOGlobalID) that's used to uniquely identify each object to the external store. If _object_ hasn't been registered in the EOEditingContext (that is, if no match is found), this method returns `nil`. Objects are registered in an EOEditingContext using the __insertObject:__ method, or, when fetching, with __recordObject:globalID:__ .

__See also:__ - __objectForGlobalID:__

---

#### hasChanges

- (BOOL)`hasChanges`

Returns YES if any of the objects in the receiver's object graph have been modified-that is, if any objects have been inserted, deleted, or updated.

---

#### initWithParentObjectStore:

- `initWithParentObjectStore:`(EOObjectStore \*)_anObjectStore_

Initializes the receiver with _anObjectStore_ as its parent EOObjectStore. Returns `self`. This method is the designated initializer for EOEditingContext. For more discussion of parent EOObjectStores, see ["Other Classes that Participate in Object Graph Management"](EOEditingContext-4.md) in the class description.

---

#### initializeObject:withGlobalID:editingContext:

- (void)`initializeObject:`(id)_object_`withGlobalID:`(EOGlobalID \*)_globalID_`editingContext:`(EOEditingContext \*)_anEditingContext_

Overrides the implementation inherited from EOObjectStore to build the properties for the _object_ identified by _globalID_. When a parent EOEditingContext receives this on behalf of a child EOEditingContext (as represented by _anEditingContext_), and the _globalID_ identifies an object instantiated in the parent, the parent returns properties extracted from its object and translated into the child's context. This ensures that a nested context "inherits" modified values from its parent EOEditingContext. If the receiver doesn't have _object_, the request is forwarded the receiver's parent EOObjectStore.

---

#### insertedObjects

- (NSArray \*)`insertedObjects`

Returns the objects that have been inserted into the receiver's object graph.

__See also:__ `-` __deletedObjects__ , `-` __updatedObjects__

---

#### insertObject:

- (void)`insertObject:`(id)_object_

Registers (by invoking __insertObject:withGlobalID:__ ) _object_ to be inserted in the receiver's parent EOObjectStore the next time changes are saved. In the meantime, _object_ is registered in the receiver with a temporary globalID.

__See also:__ - __insertedObjects__ , - __deletedObjects__ , - __insertObject:withGlobalID:__

---

#### insertObject:withGlobalID:

- (void)`insertObject:`_object_ `withGlobalID:`(EOGlobalID \*)_globalID_

Registers a new _object_ identified by _globalID_ that should be inserted in the parent EOObjectStore when changes are saved. Works by invoking __recordObject:globalID:__ , unless the receiver already contains the object. Sends _object_ the message [__awakeFromInsertionInEditingContext:__](EOEnterpriseObject-3.md). _globalID_ must respond YES to [__isTemporary__](EOGlobalID-2.md). When the external store commits _object_, it re-records it with the appropriate permanent globalID.

It is an error to insert an object that's already registered in an editing context unless you are effectively undeleting the object by reinserting it.

__See also:__ - __insertObject:__

---

#### invalidateAllObjects

- (void)`invalidateAllObjects`

Overrides the implementation inherited from EOObjectStore to discard the values of objects cached in memory and refault them, which causes them to be refetched from the external store the next time they're accessed. This method sends the message __invalidateObjectsWithGlobalIDs:__ to the parent object store with the globalIDs of all of the objects cached in the receiver. When an EOEditingContext receives this message, it propagates the message down the object store hierarchy. EODatabaseContexts discard their snapshots for invalidated objects and broadcast an EOObjectsChangedInStoreNotification. (EODatabaseContext is defined in EOAccess.)

The final effect of this method is to refault all objects currently in memory. This refaulting in turn releases all objects not retained by your application or by an EODisplayGroup. The next time you access one of these objects, it's refetched from the database.

To flush the entire application's cache of all values fetched from an external store, use a statement such as the following:

> ```
> [[editingContext rootObjectStore] invalidateAllObjects];
> ```

If you just want to discard uncommitted changes but you don't want to sacrifice the values cached in memory, use the EOEditingContext __revert__ method, which reverses all changes and clears the undo stack. For more discussion of this topic, see the section ["Methods for Managing the Object Graph"](EOEditingContext-4.md) in the class description.

__See also:__ - __refetch:__ , - __invalidateObjectsWithGlobalIDs:__

---

#### invalidateObjectsWithGlobalIDs:

- (void)`invalidateObjectsWithGlobalIDs:`(NSArray \*)_globalIDs_

Overrides the implementation inherited from EOObjectStore to signal to the parent object store that the cached values for the objects identified by _globalID_s should no longer be considered valid and that they should be refaulted. Invokes __processRecentChanges__ before refaulting the objects. This message is propagated to any underlying object store, resulting in a refetch the next time the objects are accessed. Any related (child or peer) object stores are notified that the objects are no longer valid. All uncommitted changed to the objects are lost. For more discussion of this topic, see the section ["Methods for Managing the Object Graph"](EOEditingContext-4.md) in the class description.

__See also:__ - __invalidateAllObjects__

---

#### invalidatesObjectsWhenFreed

- (BOOL)`invalidatesObjectsWhenFreed`

Returns YES to indicate that the receiver clears and "booby-traps" all of the objects registered with it when the receiver is deallocated, NO otherwise. The default is YES. In this method, "invalidate" has a different meaning than it does in the other `invalidate...` methods. For more discussion of this topic, see the method description for __setInvalidatesObjectsWhenFreed:__ .

---

#### isObjectLockedWithGlobalID:editingContext:

- (BOOL)`isObjectLockedWithGlobalID:`(EOGlobalID \*)_globalID_
`editingContext:`(EOEditingContext \*)_anEditingContext_

Returns YES if the object identified by _globalID_ in _anEditingContext_ is locked, NO otherwise. This method works by forwarding the message __isObjectLockedWithGlobalID:editingContext:__ to its parent object store.

__See also:__ - __lockObject:__ , - __lockObjectWithGlobalID:editingContext:__ ,
- __locksObjectsBeforeFirstModification__

---

#### lock

Locks access to the receiver to prevent other threads from accessing it. You should lock an editing context when you are accessing or modifying objects managed by the editing context. The thread-saftey provided by Enterprise Objects Framework allows one thread to be active in each EOEditingContext and one thread to be active in each EODatabaseContext (EOAccess). In other words, multiple threads can access and modify objects concurrently in different editing contexts, but only one thread can access the database at a time (to save, fetch, or fault).

---

__Warning:__ This method creates an NSAutoreleasePool that is released when __unlock__ is called. Consequently, objects that have been autoreleased within the scope of a __lock__ /__unlock__ pair may not be valid after the __unlock__ .

---

__See also:__ - __unlock__

---

#### lockObject:

- (void)`lockObject:`(id)_anObject_

Attempts to lock _anObject_ in the external store. This method works by invoking __lockObjectWithGlobalID:editingContext:__ . Raises an NSInvalidArgumentException if it can't find the globalID for _anObject_ to pass to __lockObjectWithGlobalID:editingContext:__ .

__See also:__ - __isObjectLockedWithGlobalID:editingContext:__ , - __locksObjectsBeforeFirstModification__

---

#### lockObjectWithGlobalID:editingContext:

- (void)`lockObjectWithGlobalID:`(EOGlobalID \*)_globalID_
`editingContext:`(EOEditingContext \*)_anEditingContext_

Overrides the implementation inherited from EOObjectStore to attempt to lock the object identified by _globalID_ in _anEditingContext_ in the external store. Raises an NSInternalInconsistencyException if unable to obtain the lock. This method works by forwarding the message __lockObjectWithGlobalID:editingContext:__ to its parent object store.

__See also:__ - __lockObject:__ , - __isObjectLockedWithGlobalID:editingContext:__ , - __locksObjectsBeforeFirstModification__

---

#### locksObjectsBeforeFirstModification

- (BOOL)`locksObjectsBeforeFirstModification`

Returns YES if the receiver locks _object_ in the external store (with __lockObject:__ ) the first time _object_ is modified.

__See also:__ - __setLocksObjectsBeforeFirstModification:__ , - __isObjectLockedWithGlobalID: editingContext:__ , - __lockObject:__ , - __lockObjectWithGlobalID:editingContext:__

---

#### messageHandler

- (id)`messageHandler`

Returns the EOEditingContext's message handler. A message handler is a special-purpose delegate responsible for presenting errors to the user. Typically, an EODisplayGroup (EOInterface) registers itself as the message handler for its EOEditingContext. For more information, see the [EOMessageHandlers](EOMessageHandlers.md) informal protocol specification.

__See also:__ - __setMessageHandler:__

---

#### objectForGlobalID:

- (id)`objectForGlobalID:`(EOGlobalID \*)_globalID_

Returns the object identified by _globalID_, or `nil` if no object has been registered in the EOEditingContext with _globalID_.

__See also:__ - __globalIDForObject:__

---

#### objectsForSourceGlobalID:relationshipName:editingContext:

- (NSArray \*)`objectsForSourceGlobalID:`(EOGlobalID \*)_globalID_
`relationshipName:`(NSString \*)_name_
`editingContext:`(EOEditingContext \*)_anEditingContext_

Overrides the implementation inherited from EOObjectStore to service a to-many fault for a relationship named _name_. When a parent EOEditingContext receives a __objectsForSourceGlobalID:relationshipName:editingContext:__ message on behalf of a child editing context and _globalID_ matches an object instantiated in the parent, the parent returns a copy of its relationship array and translates its objects into the child editing context. This ensures that a child editing context "inherits" modified values from its parent. If the receiving editing context does not have the specified object or if the parent's relationship property is still a fault, the request is fowarded to its parent object store.

---

#### objectsWithFetchSpecification:

- (NSArray \*)`objectsWithFetchSpecification:`(EOFetchSpecification \*)_fetchSpecification_

Invokes __objectsWithFetchSpecification:__ `editingContext:` with `self` as the EOEditingContext and returns the result.

---

#### objectsWithFetchSpecification:editingContext:

- (NSArray \*)`objectsWithFetchSpecification:`(EOFetchSpecification \*)_fetchSpecification_ `editingContext:`(EOEditingContext \*)_anEditingContext_

Overrides the implementation inherited from EOObjectStore to fetch objects from an external store according to the criteria specified by _fetchSpecification_ and return them in an array. If one of these objects is already present in memory, this method doesn't overwrite its values with the new values from the database. This method raises an exception if an error occurs; the error message indicates the nature of the problem.

When an EOEditingContext receives this message, it forwards the message to its root object store. Typically the root object store is an EOObjectStoreCoordinator with underlying EODatabaseContexts. In this case, the object store coordinator forwards the request to the appropriate database context based on the entity name in _fetchSpecification_. The database context then obtains an EODatabaseChannel and performs the fetch, registering all fetched objects in _anEditingContext_. (EODatabaseContext and EODatabaseChannel are defined in EOAccess.)

---

#### objectWillChange:

- (void)`objectWillChange:`(id)_object_

This method is automatically invoked when any of the objects registered in the receiver invokes its [__willChange__](EOEnterpriseObject-3.md)method. This method is EOEditingContext's implementation of the EOObserving protocol.

---

#### parentObjectStore

- (EOObjectStore \*)`parentObjectStore`

Returns the EOObjectStore from which the receiver fetches and to which it saves objects.

---

#### processRecentChanges

- (void)`processRecentChanges`

Forces the receiver to process pending insertions, deletions, and updates.Normally, when objects are changed, the processing of the changes is deferred until the end of the current event. At that point, an EOEditingContext moves objects to the inserted, updated, and deleted lists, delete propagation is performed, undos are registered, and EOObjectsChangedInStoreNotification and EOObjectsChangedInEditingContextNotification are posted (In a Yellow Box application, this usually causes the user interface to update). You can use this method to explicitly force changes to be processed. An EOEditingContext automatically invokes this method on itself before performing certain operations such as __saveChanges__ .

---

#### propagatesDeletesAtEndOfEvent

- (BOOL)`propagatesDeletesAtEndOfEvent`

Returns YES if the receiver propagates deletes at the end of the event in which a change was made, NO if it propagates deletes only right before saving changes. The default is YES.

__See also:__ - __setPropagatesDeletesAtEndOfEvent:__

---

#### recordObject:globalID:

- (void)`recordObject:`(id)_object_`globalID:`(EOGlobalID \*)_globalID_

Makes the receiver aware of an object identified by _globalID_ existing in its parent object store. EOObjectStores (such as the access layer's EODatabaseContext) usually invoke this method for each object fetched. When it receives this message, the receiver enters the object in its uniquing table and registers itself as an observer of the object.

---

#### redo:

- (void)`redo:`(id)_sender_

This method forwards a __redo__ message to the receiver's NSUndoManager, asking it to reverse the latest undo operation applied to objects in the object graph.

__See also:__ - __undo:__

---

#### refault:

- (void)`refault:`(id)_sender_

This action method simply invokes __refaultObjects__ .

---

#### refaultObjects

- (void)`refaultObjects`

Refaults all objects cached in the receiver that haven't been inserted, deleted, or updated. Invokes __processRecentChanges__ , then invokes __refaultObject:withGlobalID:editingContext:__ for all objects that haven't been inserted, deleted, or updated. For more discussion of this topic, see the section ["Methods for Managing the Object Graph"](EOEditingContext-4.md) in the class description.

---

#### refaultObject:withGlobalID:editingContext:

- (void)__refaultObject:__ (id)_anObject___withGlobalID:__ (EOGlobalID \*)_globalID___editingContext:__ (EOEditingContext \*)_anEditingContext_

Overrides the implementation inherited from EOObjectStore to refault the enterprise object _object_ identified by _globalID_ in _anEditingContext_. This method should be used with caution since refaulting an object does not remove the object snapshot from the undo stack. Objects that have been newly inserted or deleted should not be refaulted.

The main purpose of this method is to break retain cycles between enterprise objects. For example, suppose you have an Employee object that has a to-one relationship to its Department, and the Department object in turn has an array of Employee objects. You can use this method to break the retain cycle. Note that retain cycles are automatically broken if you release the EOEditingContext. For more discussion of this topic, see the section ["Methods for Managing the Object Graph"](EOEditingContext-4.md) in the class description.

__See also:__ - __invalidateObjectsWithGlobalIDs:__

---

#### refetch:

- (void)`refetch:`(id)_sender_

This action method simply invokes the __invalidateAllObjects__ method.

---

#### registeredObjects

- (NSArray \*)`registeredObjects`

Returns the enterprise objects managed by the receiver.

---

#### removeEditor:

- (void)`removeEditor:`(id)_editor_

Unregisters _editor_ from the receiver. For more discussion of EOEditors, see the __editors__ method description and the [EOEditors](EOEditors.md) informal protocol specification.

__See also:__ - __addEditor:__

---

#### revert

- (void)`revert`

Removes everything from the undo stack, discards all insertions and deletions, and restores updated objects to their last committed values. Does not refetch from the database. Note that __revert__ doesn't automatically cause higher level display groups (WebObject's WODisplayGroups or the interface layer's EODisplayGroups) to refetch. Display groups that allow insertion and deletion of objects need to be explicitly synchronized whenever this method is invoked on their EOEditingContext.

__See also:__ - __invalidateAllObjects__

---

#### revert:

- (void)`revert:`(id)_sender_

This action method simply invokes `revert`.

---

#### rootObjectStore

- (EOObjectStore \*)`rootObjectStore`

Returns the EOObjectStore at the base of the object store hierarchy (usually an EOObjectStoreCoordinator).

---

#### saveChanges

- (void)`saveChanges`

Commits changes made in the receiver to its parent EOObjectStore by sending it the message __saveChangesInEditingContext:__ . If the parent is an EOObjectStoreCoordinator, it guides its EOCooperatingObjectStores, typically EODatabaseContexts, through a multi-pass save operation (see the EOObjectStoreCoordinator class specification for more information). If a database error occurs, an exception is raised; the error message indicates the nature of the problem.

---

#### saveChanges:

- (void)`saveChanges`:(id)_sender_

This action method invokes __saveChanges__ , handling an exception by passing it to the message handler. For example, if a validation error occurs, the message handler (usually an EODisplayGroup) presents an alert panel with the text of the validation exception.

__See also:__ [- __editingContext:presentErrorMessage:__](EOMessageHandlers.md)(EOMessageHandlers), - __editingContext: shouldPresentException:__ (EOEditingContext Delegate)

---

#### saveChangesInEditingContext:

- (void)__saveChangesInEditingContext:__ (EOEditingContext \*)_anEditingContext_

Overrides the implementation inherited from EOObjectStore to tell the receiver's EOObjectStore to accept changes from a child EOEditingContext. This method shouldn't be invoked directly. It's invoked by a nested EOEditingContext when it's committing changes to a parent EOEditingContext. The receiving parent EOEditingContext incorporates all changes from the nested EOEditingContext into its own copies of the objects, but it doesn't immediately save those changes to the database. If the parent itself is later sent __saveChanges__ , it propagates any changes received from the child along with any other changes to its parent EOObjectStore. Raises an exception if an error occurs; the error message indicates the nature of the problem.

---

#### setDelegate:

- (void)`setDelegate:`(id)_anObject_

Set the receiver's delegate to be _anObject_, without retaining it.

__See also:__ - __delegate__

---

#### setInvalidatesObjectsWhenFreed:

- (void)`setInvalidatesObjectsWhenFreed:`(BOOL)_flag_

Sets according to _flag_ whether the receiver clears and "booby-traps" all of the objects registered with it when the receiver is deallocated. If an editing context invalidates objects when it's deallocated, it sends a [__clearProperties__](EOEnterpriseObject-3.md)message to all of its objects, thereby breaking any retain cycles between objects that would prevent them from being deallocated. This method leaves the objects in a state in which sending them any message other than `dealloc` or `release` raises an exception.

The default is YES, and as a general rule, this setting must be YES for enterprise objects with cyclic references to be freed when their EOEditingContext is freed.

Note that the word "invalidate" in this method name has a different meaning than it does in the other `invalidate...` methods, which discard object values and refault them.

__See also:__ - __invalidatesObjectsWhenFreed__

---

#### setLocksObjectsBeforeFirstModification:

- (void)`setLocksObjectsBeforeFirstModification:`(BOOL)_flag_

Sets according to _flag_ whether the receiver locks _object_ in the external store (with __lockObject:__ ) the first time _object_ is modified. The default is NO. If _flag_ is YES, an exception will be thrown raised if a lock can't be obtained when _object_ invokes [__willChange__](EOEnterpriseObject-3.md). There are two reasons a lock might fail: because the row is already locked in the server, or because your snapshot is out of date. If your snapshot is out of date, you can explicitly refetch the object using an EOFetchSpecification with [__setRefreshesRefetchedObjects:__](EOFetchSpecification-2.md)set to YES. To handle the exception, you can implement the EODatabaseContext delegate method __databaseContextShouldRaiseExceptionForLockFailure:__ .

You should avoid using this method or pessimistic locking in an interactive end-user application. For example, a user might make a change in a text field and neglect to save it, thereby leaving the data locked in the server indefinitely. Consider using optimistic locking or application level explicit check-in/check-out instead.

__See also:__ - __locksObjectsBeforeFirstModification__

---

#### setMessageHandler:

- (void)`setMessageHandler:`(id)_handler_

Set the receiver's message handler to be _handler_.

__See also:__ - __messageHandler__

---

#### setPropagatesDeletesAtEndOfEvent:

- (void)`setPropagatesDeletesAtEndOfEvent:`(BOOL)_flag_

Sets according to _flag_ whether the receiver propagates deletes at the end of the event in which a change was made, or only just before saving changes.

If _flag_ is YES, deleting an enterprise object triggers delete propagation at the end of the event in which the deletion occurred (this is the default behavior). If _flag_ is NO, delete propagation isn't performed until __saveChanges__ is invoked.

You can delete enterprise objects explicitly by using the __deleteObject:__ method or implicitly by removing the enterprise object from an owning relationship. Delete propagation uses the delete rules in the EOClassDescription to determine whether objects related to the deleted object should also be deleted (for more information, see the [EOClassDescription](EOClassDescription-3.md) class specification and the [EOEnterpriseObject](EOEnterpriseObject-3.md) informal protocol specification). If delete propagation fails (that is, if an enterprise object refuses to be deleted-possibly due to a deny rule), all changes made during the event are rolled back.

__See also:__ - __propagatesDeletesAtEndOfEvent__

---

#### setStopsValidationAfterFirstError:

- (void)`setStopsValidationAfterFirstError:`(BOOL)_flag_

Sets according to _flag_ whether the receiver stops validating after the first error is encountered, or continues for all objects (validation typically occurs during a save operation). The default is YES. Setting it to NO is useful if the delegate implements __editingContext:shouldPresentException:__ to handle the presentation of aggregate exceptions.

__See also:__ - __stopsValidationAfterFirstError__

---

#### setUndoManager:

- (void)`setUndoManager:`(NSUndoManager \*)_undoManager_

Sets the receiver's NSUndoManager to _undoManager_. You might invoke this method with __nil__ if your application doesn't need undo and you want to avoid the overhead of an undo stack. For more information on editing context's undo support, see the section "[Undo and Redo](EOEditingContext-4.md)."

__See also:__ - __undoManager__

---

#### stopsValidationAfterFirstError

- (BOOL)`stopsValidationAfterFirstError`

Returns YES to indicate that the receiver should stop validating after it encounters the first error, or NO to indicate that it should continue for all objects.

__See also:__ - __setStopsValidationAfterFirstError:__

---

#### tryToSaveChanges

- (NSException \*)`tryToSaveChanges`

Invokes the `saveChanges` method, and catches and returns any exceptions that are raised.

---

#### undo:

- (void)`undo:`(id)_sender_

This action method forwards an __undo__ message to the receiver's NSUndoManager, asking it to reverse the latest uncommitted changes applied to objects in the object graph. For more information on editing context's undo support, see the section "[Undo and Redo](EOEditingContext-4.md)."

__See also:__ __redo:__

---

#### undoManager

- (NSUndoManager \*)`undoManager`

Returns the receiver's NSUndoManager.

__See also:__ - __setUndoManager:__

---

#### unlock

- (void)`unlock`

Unlocks access to the receiver so that other threads may access it.

---

__Warning:__ This method creates an NSAutoreleasePool that is released when __unlock__ is called. Consequently, objects that have been autoreleased within the scope of a __lock__ /__unlock__ pair may not be valid after the __unlock__ .

---

__See also:__ - __lock__

---

#### updatedObjects

- (NSArray \*)`updatedObjects`

Returns the objects in the receiver's object graph that have been updated.

__See also:__ `-` __deletedObjects__ , `-` __insertedObjects__

## Notification

The following notifications are declared (except where otherwise noted) and posted by EOEditingContext.

---

### EOEditingContextDidSaveChangesNotification

This notification is broadcast after changes are saved to the EOEditingContext's parent EOObjectStore. The notification contains:

| __Notification Object__ | The EOEditingContext |
| userInfo Dictionary | userInfo Dictionary |
| __Key__ | __Value__ |
| updated | An NSArray containing the changed objects |
| deleted | An NSArray containing the deleted objects |
| inserted | An NSArray containing the inserted objects |

```
```


---

### EOInvalidatedAllObjectsInStoreNotification

This notification is defined by EOObjectStore. When posted by an EOEditingContext, it's the result of the editing context invalidating all its objects. When an EOEditingContext receives an [EOInvalidatedAllObjectsInStoreNotification](EOObjectStore-2.md) from its parent EOObjectStore, it clears its lists of inserted, updated, and deleted objects, and resets its undo stack. The notification contains:`| Notification Object | The EOEditingContext |
| userInfo Dictionary | None. |

|  |
| --- |
|  |`

An interface layer EODisplayGroup (not a WebObjects WODisplayGroup) listens for this notification to refetch its contents. See the EOObjectStore class specification for more information on this notification.

---

### EOObjectsChangedInStoreNotification

This notification is defined by EOObjectStore. When posted by an EOEditingContext, it's the result of the editing context processing __objectWillChange:__ observer notifications in __processRecentChanges__ , which is usually as the end of the event in which the changes occurred. See the EOObjectStore class specification for more information on [EOObjectsChangedInStoreNotification](EOObjectStore-2.md).

This notification contains:

| __Notification Object__ | The EOEditingContext |
| userInfo Dictionary | userInfo Dictionary |
| __Key__ | __Value__ |
| updated | An NSArray of EOGlobalIDs for objects whose properties have changed. A receiving EOEditingContext typically responds by refaulting the objects. |
| inserted | An NSArray of EOGlobalIDs for objects that have been inserted into the EOObjectStore. |
| deleted | An NSArray of EOGlobalIDs for objects that have been deleted from the EOObjectStore. |
| invalidated | An NSArray of EOGlobalIDs for objects that have been turned into faults. Invalidated objects are those for which the cached view should no longer be trusted. Invalidated objects should be refaulted so that they are refetched when they're next examined. |

```
```


---

### EOObjectsChangedInEditingContextNotification

This notification is broadcast whenever changes are made in an EOEditingContext. It's similar to EOObjectsChangedInStoreNotification, except that it contains objects rather than globalIDs. The notification contains:

| __Notification Object__ | The EOEditingContext |
| userInfo Dictionary | userInfo Dictionary |
| __Key__ | __Value__ |
| updated | An NSArray containing the changed objects |
| deleted | An NSArray containing the deleted objects |
| inserted | An NSArray containing the inserted objects |
| invalidated | An NSArray containing invalidated objects. |

```
```

Interface layer EODisplayGroups (not WebObjects WODisplayGroups) listen for this notification to redisplay their contents.

---

[!](EODetailDataSource-2.md)
[!](EOEditingContext-4.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
