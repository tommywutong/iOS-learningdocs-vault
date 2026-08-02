---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOEditingContext.html
archived_at: '2026-07-18T01:28:25.751720Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EODetailDataSource.md)
[!](EOEditingContext-2.md)

---

# EOEditingContext

__Inherits From:__
EOObjectStore : Object (Java Client)
EOObjectStore : NSObject (Yellow Box)

__Implements:__
EOObserving
NSLocking (Yellow Box only)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

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

| __Commonly Used Methods__ | __Commonly Used Methods__ |
| - objectsWithFetchSpecification | Fetches objects from an external store. |
| - insertObject | Registers a new object to be inserted into the parent EOObjectStore when changes are saved. |
| - deleteObject | Registers that an object should be removed from the parent EOObjectStore when changes are saved. |
| - lockObject | Attempts to lock an object in the external store. |
| - hasChanges | Returns true if any of the receiver has any pending changes to the parent EOObjectStore. |
| - saveChanges | Commits changes made in the receiver to the parent EOObjectStore. |
| - revert | Removes everything from the undo stack, discards all insertions and deletions, and restores updated objects to their original values. |
| - objectForGlobalID | Given a globalID, returns its associated object. |
| - globalIDForObject | Given an object, returns its globalID. |
| - setDelegate | Sets the receiver's delegate. |
| - parentObjectStore | Returns the receiver's parent EOObjectStore. |
| - rootObjectStore | Returns the receiver's root EOObjectStore. |

|  |
| --- |
|  |**

## Class Description

An EOEditingContext object represents a single "object space" or document in an application. Its primary responsibility is managing a graph of enterprise objects. This _object graph_ is a group of related business objects that represent an internally consistent view of one or more external stores (usually a database).

All objects fetched from an external store are registered in an editing context along with a global identifier (EOGlobalID) that's used to uniquely identify each object to the external store. The editing context is responsible for watching for changes in its objects (using the EOObserving interface) and recording snapshots for object-based undo. A single enterprise object instance exists in one and only one editing context, but multiple copies of an object can exist in different editing contexts. Thus object uniquing is scoped to a particular editing context.

For more information on EOEditingContext, see the sections:

- [Other Classes that Participate in Object Graph Management](EOEditingContext-2.md)
- [Programmatically Creating an EOEditingContext](EOEditingContext-2.md)
- [Using EOEditingContexts in Different Configurations](EOEditingContext-2.md)
- [Fetching Objects](EOEditingContext-2.md)
- [Managing Changes in Your Application](EOEditingContext-2.md)
- [Methods for Managing the Object Graph](EOEditingContext-2.md)
- [General Guidelines for Managing the Object Graph](EOEditingContext-2.md)
- [Using EOEditingContext to Archive Custom Objects in Web Objects Framework](EOEditingContext-2.md)

## Constants

The following string constants name notifications EOEditingContext posts:

- EditingContextDidSaveChangesNotification
- ObjectsChangedInEditingContextNotification

See the Notifications section for more information on the notifications.

The following string constants are the keys to the ObjectsChangedInEditingContextNotification's user info dictionary:

- UpdatedKey
- DeletedKey
- InsertedKey
- InvalidatedKey

EditingContextFlushChangesRunLoopOrdering, is an integer that defines the order in which the editing context performs end of event processing in __processRecentChanges__ . Messages with lower order numbers are processed before messages with higher order numbers. In an application built with the Application Kit, the constant order value schedules the editing context to perform its processing before the undo stack group is closed or window display is updated.

## Interfaces Implemented

**EOObserving**

**[- objectWillChange](EOObserving.md)**

## Method Types

**Constructors**

**EOEditingContext**

**Controlling EOEditingContext's memory management strategy**

****

**Fetching objects**

**- objectsWithFetchSpecification**

**Committing or discarding changes**

**- saveChanges

**- refaultObjects

**- refetch

**- revert (Yellow Box only)

**- invalidateAllObjects**********

**Registering changes**

**- deleteObject

**- insertObject

**- insertObjectWithGlobalID

**- objectWillChange

**- processRecentChanges**********

**Checking changes**

**- deletedObjects

**- insertedObjects

**- updatedObjects

**- hasChanges********

**Object registration and snapshotting**

**- forgetObject

**- recordObject

**- committedSnapshotForObject

**- currentEventSnapshotForObject

**- objectForGlobalID

**- globalIDForObject

**- registeredObjects**************

**Locking objects**

**- lockObject

**- lockObjectWithGlobalID

**- isObjectLockedWithGlobalID

**- setLocksObjectsBeforeFirstModification

**- locksObjectsBeforeFirstModification**********

**Undoing operations (Yellow Box only)**

**- redo (Yellow Box only)

**- undo (Yellow Box only)

**- setUndoManager (Yellow Box only)

**- undoManager (Yellow Box only)********

**Deletion and Validation Behavior**

**- setPropagatesDeletesAtEndOfEvent

**- propagatesDeletesAtEndOfEvent

**- setStopsValidationAfterFirstError

**- stopsValidationAfterFirstError********

**Returning related object stores**

**- parentObjectStore

**- rootObjectStore****

**Managing editors**

**- editors

**- addEditor

**- removeEditor******

**Setting the delegate**

**- setDelegate

**- delegate****

**Setting the message handler**

**- setMessageHandler

**- messageHandler****

**Invalidating objects (Yellow Box only)**

**- setInvalidatesObjectsWhenFreed (Yellow Box only)

**- invalidatesObjectsWhenFreed (Yellow Box only)****

**Interacting with the server (Java Client only)**

**- invokeRemoteMethod (Java Client only)**

**Locking (Yellow Box only)**

**- lock (Yellow Box only)

**- unlock (Yellow Box only)****

**Working with raw rows (Yellow Box only)**

**- faultForRawRow (Yellow Box only)**

**Unarchiving from nib**

**+ defaultParentObjectStore

**+ setDefaultParentObjectStore

**+ setSubstitutionEditingContext

**+ substitutionEditingContext********

**Nested EOEditingContext support**

**- objectsWithFetchSpecification

**- objectsForSourceGlobalID

**- arrayFaultWithSourceGlobalID

**- faultForGlobalID

**- saveChangesInEditingContext

**- refaultObject

**- invalidateObjectsWithGlobalIDs

**- initializeObject****************

**Archiving and unarchiving objects (Yellow Box only)**

**+ encodeObjectWithCoder (Yellow Box only)

**+ initObjectWithCoder (Yellow Box only)

**+ setUsesContextRelativeEncoding (Yellow Box only)

**+ usesContextRelativeEncoding (Yellow Box only)********

## Constructors

---

#### EOEditingContext

public __EOEditingContext__ ()

Creates a new EOEditingContext object with the default parent object store as its parent object store.

public __EOEditingContext__ (EOObjectStore _anObjectStore_)

Creates a new EOEditingContext object with _anObjectStore_ as its parent object store. For more discussion of parent object stores, see ["Other Classes that Participate in Object Graph Management"](EOEditingContext-2.md) in the class description.

__See also:__ - __parentObjectStore__ , + __defaultParentObjectStore__

## Static Methods

---

#### defaultParentObjectStore

public static EOObjectStore __defaultParentObjectStore__ ()

Returns the EOObjectStore that is the default parent object store for new editing contexts. Normally this is the EOObjectStoreCoordinator returned from the EOObjectStoreCoordinator static method [__defaultCoordinator__](EOObjectStoreCoordinator.md).

__See also:__ + __setDefaultParentObjectStore__

---

#### encodeObjectWithCoder

public static void __encodeObjectWithCoder__ (
java.lang.Object _object_,
NSCoder _encoder_)

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Invoked by an enterprise object _object_ to ask the EOEditingContext to encode _object_ using _encoder_. For more discussion of this subject, see ["Using EOEditingContext to Archive Custom Objects in Web Objects Framework"](EOEditingContext-2.md) in the class description.

__See also:__ + __initObjectWithCoder__ , + __setUsesContextRelativeEncoding__ , + __usesContextRelativeEncoding__

---

#### initObjectWithCoder

public static java.lang.Object __initObjectWithCoder__ (
java.lang.Object _object_,
NSCoder _decoder_)

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Invoked by an enterprise object _object_ to ask the EOEditingContext to initialize _object_ from data in _decoder_. For more discussion of this subject, see ["Using EOEditingContext to Archive Custom Objects in Web Objects Framework"](EOEditingContext-2.md) in the class description.

__See also:__ + __encodeObjectWithCoder__ , + __setUsesContextRelativeEncoding__ , + __usesContextRelativeEncoding__

---

#### setDefaultParentObjectStore

public static void __setDefaultParentObjectStore__ (EOObjectStore _store_)

Sets thedefault parent EOObjectStore to _store_. You use this method before loading a nib file to change the default parent EOObjectStores of the EOEditingContexts in the nib file. The object you supply for _store_ can be a different EOObjectStoreCoordinator or another EOEditingContext (if you're using a nested EOEditingContext). After loading a nib with an EOEditingContext substituted as the default parent EOObjectStore, you should restore the default behavior by setting the default parent EOObjectStore to `null`.

A default parent object store is global until it is changed again. For more discussion of this topic, see the chapter "Application Configurations" in the _Enterprise Objects Framework Developer's Guide_.

__See also:__ + __defaultParentObjectStore__

---

#### setSubstitutionEditingContext

public static void __setSubstitutionEditingContext__ (EOEditingContext _anEditingContext_)

Assigns _anEditingContext_ as the EOEditingContext to substitute for the one specified in a nib file you're about to load. Using this method causes all of the connections in your nib file to be redirected to _anEditingContext_. This can be useful when you want an interface loaded from a second nib file to use an existing EOEditingContext. After loading a nib with a substitution EOEditingContext, you should restore the default behavior by setting the substitution EOEditingContext to `null`.

A substitution editing context is global until it is changed again. For more discussion of this topic, see the chapter "Application Configurations" in the _Enterprise Objects Framework Developer's Guide_.

__See also:__ + __substitutionEditingContext__

---

#### setUsesContextRelativeEncoding

public static void __setUsesContextRelativeEncoding__ (boolean _flag_)

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Sets according to _flag_ whether __encodeObjectWithCoder__ uses context-relative encoding. For more discussion of this subject, see ["Using EOEditingContext to Archive Custom Objects in Web Objects Framework"](EOEditingContext-2.md) in the class description.

__See also:__ + __usesContextRelativeEncoding__ , + __encodeObjectWithCoder__ ,

---

#### substitutionEditingContext

public static EOEditingContext __substitutionEditingContext__ ()

Returns the substitution EOEditingContext if one has been specified. Otherwise returns `null`.

__See also:__ + __setSubstitutionEditingContext__

---

#### usesContextRelativeEncoding

public static boolean __usesContextRelativeEncoding__ ()

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Returns __true__ to indicate that __encodeObjectWithCoder__ uses context relative encoding, __false__ otherwise. For more discussion of this subject, see ["Using EOEditingContext to Archive Custom Objects in Web Objects Framework"](EOEditingContext-2.md) in the class description.

__See also:__ + __setUsesContextRelativeEncoding__

## Instance Methods

---

#### addEditor

public void __addEditor__ (java.lang.Object _editor_)

Adds _editor_ to the receiver's set of [EOEditingContext.Editor](EOEditingContext.Editor.md). For more explanation, see the method description for __editors__ and the [EOEditingContext.Editor](EOEditingContext.Editor.md) interface specification.

__See also:__ `-` __removeEditor__

---

#### arrayFaultWithSourceGlobalID

public NSArray __arrayFaultWithSourceGlobalID__ (
EOGlobalID _globalID_,
java.lang.String _name_,
EOEditingContext _anEditingContext_)

Overrides the implementation inherited from EOObjectStore. If the objects associated with the EOGlobalID _globalID_ are already registered in the receiver, returns those objects. Otherwise, propagates the message down the object store hierarchy, through the parent object store, ultimately to the associated EODatabaseContext. The EODatabaseContext creates and returns a to-many fault.

When a parent EOEditingContext receives this on behalf of a child EOEditingContext and the EOGlobalID _globalID_ identifies a newly inserted object in the parent, the parent returns a copy of its object's relationship array with the member objects translated into objects in the child EOEditingContext.

For more information on faults, see the EOObjectStore, EODatabaseContext (EOAccess), and EOFaultHandler class specifications.

__See also:__ - __faultForGlobalID__

---

#### committedSnapshotForObject

public NSDictionary __committedSnapshotForObject__ (EOEnterpriseObject _object_)

This method is only available in Yellow Box; there is no Java Client equivalent.

Returns a dictionary containing a snapshot of _object_ that reflects its committed values (that is, its values as they were last committed to the database).In other words, this snapshot represents the state of the object before any modifications were made to it. The snapshot is updated to the newest object state after a save.

__See also:__ - __currentEventSnapshotForObject__

---

#### currentEventSnapshotForObject

public NSDictionary __currentEventSnapshotForObject__ (EOEnterpriseObject _object_)

This method is only available in Yellow Box; there is no Java Client equivalent.

Returns a dictionary containing a snapshot of _object_ that reflects its state as it was at the beginning of the current event loop. After the end of the current event-upon invocation of __processRecentChanges__ -this snapshot is updated to hold the modified state of the object.

__See also:__ - __committedSnapshotForObject__ , - __processRecentChanges__

---

#### delegate

public java.lang.Object __delegate__ ()

Returns the receiver's delegate.

__See also:__ - __setDelegate__

---

#### deleteObject

public void __deleteObject__ (EOEnterpriseObject _object_)

Specifies that _object_ should be removed from the receiver's parent EOObjectStore when changes are committed. At that time, the object will be removed from the uniquing tables.

__See also:__ - __deletedObjects__

---

#### deletedObjects

public NSArray __deletedObjects__ ()

Returns the objects that have been deleted from the receiver's object graph.

__See also:__ `-` __updatedObjects__ , `-` __insertedObjects__

---

#### editors

public NSArray __editors__ ()

Returns the receiver's editors. Editors are special-purpose delegate objects that may contain uncommitted changes that need to be validated and applied to enterprise objects before the EOEditingContext saves changes. For example, EODisplayGroups (EOInterface) register themselves as editors with the EOEditingContext of their data sources so that they can save any changes in the key text field. For more information, see the [EOEditingContext.Editor](EOEditingContext.Editor.md) interface specification and the EODisplayGroup class specification.

__See also:__ `-` __addEditor__ , `-` __removeEditor__

---

#### faultForGlobalID

public EOEnterpriseObject __faultForGlobalID__ (
EOGlobalID _globalID_,
EOEditingContext _anEditingContext_)

Overrides the implementation inherited from EOObjectStore. If the object associated with the EOGlobalID _globalID_ is already registered in the receiver, this method returns that object. Otherwise, the method propagates the message down the object store hierarchy, through the parent object store, ultimately to the associated EODatabaseContext. The EODatabaseContext creates and returns a to-one fault.

For example, suppose you want the department object whose __deptID__ has a particular value. The most efficient way to get it is to look it up by its globalID using __faultForGlobalID__ .

If the department object is already registered in the EOEditingContext, __faultForGlobalID__ returns the object (without going to the database). If not, a fault for this object is created, and the object is fetched only when you trigger the fault.

In a nested editing context configuration, when a parent EOEditingContext is sent __faultForGlobalID__ on behalf of a child EOEditingContext and _globalID_ identifies a newly inserted object in the parent, the parent registers a copy of the object in the child.

For more discussion of this method, see the section ["Working with Objects Across Multiple EOEditingContexts"](EOEditingContext-2.md) in the class description. For more information on faults, see the EOObjectStore, EODatabaseContext (EOAccess), and EOFaultHandler class specifications.

__See also:__ - __arrayFaultWithSourceGlobalID__

---

#### faultForRawRow

public EOEnterpriseObject __faultForRawRow__ (
java.lang.Object _row_,
java.lang.String _entityName_)

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Returns a fault for the raw row _row_ by invoking [__faultForRawRow__](EOObjectStore.md)with __this__ as the editing context.

---

#### forgetObject

public void __forgetObject__ (EOEnterpriseObject _object_)

Removes _object_ from the uniquing tables and causes the receiver to remove itself as the object's observer. This method is invoked whenever an object being observed by an EOEditingContext is finalized. You should never invoke this method directly. The correct way to remove an object from its editing context is to remove every reference to the object by refaulting any object that references it (using __refaultObjects__ or __invalidateAllObjects__ ). Also note that this method does _not_ have the effect of deleting an object-to delete an object you should either use the __deleteObject__ method or remove the object from an owning relationship.

---

#### globalIDForObject

public EOGlobalID __globalIDForObject__ (EOEnterpriseObject _object_)

Returns the EOGlobalID for _object_. All objects fetched from an external store are registered in an EOEditingContext along with a global identifier (EOGlobalID) that's used to uniquely identify each object to the external store. If _object_ hasn't been registered in the EOEditingContext (that is, if no match is found), this method returns `null`. Objects are registered in an EOEditingContext using the __insertObject__ method, or, when fetching, with __recordObject__ .

__See also:__ - __objectForGlobalID__

---

#### hasChanges

public boolean __hasChanges__ ()

()

Returns __true__ if any of the objects in the receiver's object graph have been modified-that is, if any objects have been inserted, deleted, or updated.

---

#### initializeObject

public void __initializeObject__ (
EOEnterpriseObject _object_,
EOGlobalID _globalID_,
EOEditingContext _anEditingContext_)

Overrides the implementation inherited from EOObjectStore to build the properties for the _object_ identified by _globalID_. When a parent EOEditingContext receives this on behalf of a child EOEditingContext (as represented by _anEditingContext_), and the _globalID_ identifies an object instantiated in the parent, the parent returns properties extracted from its object and translated into the child's context. This ensures that a nested context "inherits" modified values from its parent EOEditingContext. If the receiver doesn't have _object_, the request is forwarded the receiver's parent EOObjectStore.

---

#### insertedObjects

public NSArray __insertedObjects__ ()

Returns the objects that have been inserted into the receiver's object graph.

__See also:__ `-` __deletedObjects__ , `-` __updatedObjects__

---

#### insertObject

public void __insertObject__ (EOEnterpriseObject _object_)

Registers (by invoking __insertObjectWithGlobalID__ ) _object_ to be inserted in the receiver's parent EOObjectStore the next time changes are saved. In the meantime, _object_ is registered in the receiver with a temporary globalID.

__See also:__ - __insertedObjects__ , - __deletedObjects__ , - __insertObjectWithGlobalID__

---

#### insertObjectWithGlobalID

public void __insertObjectWithGlobalID__ (EOEnterpriseObject _anEOEnterpriseObject_, EOGlobalID _anEOGlobalID_)

Registers a new _object_ identified by _globalID_ that should be inserted in the parent EOObjectStore when changes are saved. Works by invoking __recordObject__ , unless the receiver already contains the object. Sends _object_ the message [__awakeFromInsertion__](EOEnterpriseObject.md). _globalID_ must respond __true__ to [__isTemporary__](EOGlobalID.md). When the external store commits _object_, it re-records it with the appropriate permanent globalID.

It is an error to insert an object that's already registered in an editing context unless you are effectively undeleting the object by reinserting it.

__See also:__ - __insertObject__

---

#### invalidateAllObjects

public void __invalidateAllObjects__ ()

()

Overrides the implementation inherited from EOObjectStore to discard the values of objects cached in memory and refault them, which causes them to be refetched from the external store the next time they're accessed. This method sends the message __invalidateObjectsWithGlobalIDs__ to the parent object store with the globalIDs of all of the objects cached in the receiver. When an EOEditingContext receives this message, it propagates the message down the object store hierarchy. EODatabaseContexts discard their snapshots for invalidated objects and broadcast an ObjectsChangedInStoreNotification. (EODatabaseContext is defined in EOAccess.)

The final effect of this method is to refault all objects currently in memory. The next time you access one of these objects, it's refetched from the database.

To flush the entire application's cache of all values fetched from an external store, use a statement such as the following:

> ```
> EOEditingContext.rootObjectStore().invalidateAllObjects();
> ```

If you just want to discard uncommitted changes but you don't want to sacrifice the values cached in memory, use the EOEditingContext __revert__ method (Yellow Box only), which reverses all changes and clears the undo stack. For more discussion of this topic, see the section ["Methods for Managing the Object Graph"](EOEditingContext-2.md) in the class description.

__See also:__ - __refetch__ , - __invalidateObjectsWithGlobalIDs__

---

#### invalidateObjectsWithGlobalIDs

public void __invalidateObjectsWithGlobalIDs__ (NSArray _globalIDs_)

Overrides the implementation inherited from EOObjectStore to signal to the parent object store that the cached values for the objects identified by _globalID_s should no longer be considered valid and that they should be refaulted. Invokes __processRecentChanges__ before refaulting the objects. This message is propagated to any underlying object store, resulting in a refetch the next time the objects are accessed. Any related (child or peer) object stores are notified that the objects are no longer valid. All uncommitted changed to the objects are lost. For more discussion of this topic, see the section ["Methods for Managing the Object Graph"](EOEditingContext-2.md) in the class description.

__See also:__ - __invalidateAllObjects__

---

#### invalidatesObjectsWhenFreed

public boolean __invalidatesObjectsWhenFreed__ ()

()

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Returns __true__ to indicate that the receiver clears and "booby-traps" all of the objects registered with it when the receiver is finalized, __false__ otherwise. The default is __true__ . In this method, "invalidate" has a different meaning than it does in the other `invalidate...` methods. For more discussion of this topic, see the method description for __setInvalidatesObjectsWhenFreed__ .

---

#### invokeRemoteMethod

public java.lang.Object __invokeRemoteMethod__ (
EOEditingContext _anEditingContext_,
EOGlobalID _globalID_,
java.lang.String _methodName_,
java.lang.Object[] _objects_)

This method is available for Java Client applications only; there is no Yellow Box equivalent.

__See also:__

---

#### isObjectLockedWithGlobalID

public boolean __isObjectLockedWithGlobalID__ (
EOGlobalID _globalID_,
EOEditingContext _anEditingContext_)

Returns __true__ if the object identified by _globalID_ in _anEditingContext_ is locked, __false__ otherwise. This method works by forwarding the message __isObjectLockedWithGlobalID__ to its parent object store.

__See also:__ - __lockObject__ , - __lockObjectWithGlobalID__ ,
- __locksObjectsBeforeFirstModification__

---

#### lock

public void __lock__ ()

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Locks access to the receiver to prevent other threads from accessing it. You should lock an editing context when you are accessing or modifying objects managed by the editing context. The thread-saftey provided by Enterprise Objects Framework allows one thread to be active in each EOEditingContext and one thread to be active in each EODatabaseContext (EOAccess). In other words, multiple threads can access and modify objects concurrently in different editing contexts, but only one thread can access the database at a time (to save, fetch, or fault).

---

__Warning:__ This method creates an NSAutoreleasePool that is released when __unlock__ is called. Consequently, objects that have been autoreleased within the scope of a __lock__ /__unlock__ pair may not be valid after the __unlock__ .

---

__See also:__ - __unlock__

---

#### lockObject

public void __lockObject__ (EOEnterpriseObject _anObject_)

Attempts to lock _anObject_ in the external store. This method works by invoking __lockObjectWithGlobalID__ . Throws an exception if it can't find the globalID for _anObject_ to pass to __lockObjectWithGlobalID__ .

__See also:__ - __isObjectLockedWithGlobalID__ , - __locksObjectsBeforeFirstModification__

---

#### lockObjectWithGlobalID

public void __lockObjectWithGlobalID__ (
EOGlobalID _globalID_,
EOEditingContext _anEditingContext_)

Overrides the implementation inherited from EOObjectStore to attempt to lock the object identified by _globalID_ in _anEditingContext_ in the external store. Throws an exception if unable to obtain the lock. This method works by forwarding the message __lockObjectWithGlobalID__ to its parent object store.

__See also:__ - __lockObject__ , - __isObjectLockedWithGlobalID__ , - __locksObjectsBeforeFirstModification__

---

#### locksObjectsBeforeFirstModification

public boolean __locksObjectsBeforeFirstModification__ ()

()

Returns __true__ if the receiver locks _object_ in the external store (with __lockObject__ ) the first time _object_ is modified.

__See also:__ - __setLocksObjectsBeforeFirstModification__ , - __isObjectLockedWithGlobalID__ , - __lockObject__ , - __lockObjectWithGlobalID__

---

#### messageHandler

public java.lang.Object __messageHandler__ ()

Returns the EOEditingContext's message handler. A message handler is a special-purpose delegate responsible for presenting errors to the user. Typically, an EODisplayGroup (EOInterface) registers itself as the message handler for its EOEditingContext. For more information, see the [EOEditingContext.MessageHandler](EOEditingContext.MessageHandler.md) interface specification.

__See also:__ - __setMessageHandler__

---

#### objectForGlobalID

public EOEnterpriseObject __objectForGlobalID__ (EOGlobalID _globalID_)

Returns the object identified by _globalID_, or `null` if no object has been registered in the EOEditingContext with _globalID_.

__See also:__ - __globalIDForObject__

---

#### objectsForSourceGlobalID

public NSArray __objectsForSourceGlobalID__ (
EOGlobalID _globalID_,
java.lang.String _name_,
EOEditingContext _anEditingContext_)

Overrides the implementation inherited from EOObjectStore to service a to-many fault for a relationship named _name_. When a parent EOEditingContext receives a __objectsForSourceGlobalID__ message on behalf of a child editing context and _globalID_ matches an object instantiated in the parent, the parent returns a copy of its relationship array and translates its objects into the child editing context. This ensures that a child editing context "inherits" modified values from its parent. If the receiving editing context does not have the specified object or if the parent's relationship property is still a fault, the request is fowarded to its parent object store.

---

#### objectsWithFetchSpecification

public NSArray __objectsWithFetchSpecification__ (EOFetchSpecification _fetchSpecification_)

public NSArray __objectsWithFetchSpecification__ (
EOFetchSpecification _fetchSpecification_,
EOEditingContext _anEditingContext_)

Overrides the implementation inherited from EOObjectStore to fetch objects from an external store according to the criteria specified by _fetchSpecification_ and return them in an array. If one of these objects is already present in memory, this method doesn't overwrite its values with the new values from the database. This method throws an exception if an error occurs; the error message indicates the nature of the problem.

When an EOEditingContext receives this message, it forwards the message to its root object store. Typically the root object store is an EOObjectStoreCoordinator with underlying EODatabaseContexts. In this case, the object store coordinator forwards the request to the appropriate database context based on the entity name in _fetchSpecification_. The database context then obtains an EODatabaseChannel and performs the fetch, registering all fetched objects in _anEditingContext_. (EODatabaseContext and EODatabaseChannel are defined in EOAccess.)

---

#### objectWillChange

public void __objectWillChange__ (java.lang.Object _object_)

This method is automatically invoked when any of the objects registered in the receiver invokes its [__willChange__](EOEnterpriseObject.md)method. This method is EOEditingContext's implementation of the EOObserving protocol.

---

#### parentObjectStore

public EOObjectStore __parentObjectStore__ ()

Returns the EOObjectStore from which the receiver fetches and to which it saves objects.

---

#### processRecentChanges

public void __processRecentChanges__ ()

()

Forces the receiver to process pending insertions, deletions, and updates.Normally, when objects are changed, the processing of the changes is deferred until the end of the current event. At that point, an EOEditingContext moves objects to the inserted, updated, and deleted lists, delete propagation is performed, undos are registered, and ObjectsChangedInStoreNotification and ObjectsChangedInEditingContextNotification are posted (In a Yellow Box application, this usually causes the user interface to update). You can use this method to explicitly force changes to be processed. An EOEditingContext automatically invokes this method on itself before performing certain operations such as __saveChanges__ . This method does nothing on Java Client.

---

#### propagatesDeletesAtEndOfEvent

public boolean __propagatesDeletesAtEndOfEvent__ ()

()

Returns __true__ if the receiver propagates deletes at the end of the event in which a change was made, __false__ if it propagates deletes only right before saving changes. The default is __true__ .

__See also:__ - __setPropagatesDeletesAtEndOfEvent__

---

#### recordObject

public void __recordObject__ (
EOEnterpriseObject _object_,
EOGlobalID _globalID_)

Makes the receiver aware of an object identified by _globalID_ existing in its parent object store. EOObjectStores (such as the access layer's EODatabaseContext) usually invoke this method for each object fetched. When it receives this message, the receiver enters the object in its uniquing table and registers itself as an observer of the object.

---

#### redo

public void __redo__ ()

This method is available for Yellow Box applications only; there is no Java Client equivalent.

This method forwards a __redo__ message to the receiver's NSUndoManager, asking it to reverse the latest undo operation applied to objects in the object graph.

__See also:__ - __undo__

---

#### refault:

public void __refault__ ()

This method is available for Yellow Box applications only; there is no Java Client equivalent.

This method simply invokes __refaultObjects__ .

---

#### refaultObject

public void __refaultObject__ (
EOEnterpriseObject _anObject_,
EOGlobalID _globalID_,
EOEditingContext _anEditingContext_)

Overrides the implementation inherited from EOObjectStore to refault the enterprise object _object_ identified by _globalID_ in _anEditingContext_. This method should be used with caution since refaulting an object does not remove the object snapshot from the undo stack. Objects that have been newly inserted or deleted should not be refaulted.

The main purpose of this method is to break reference cycles between enterprise objects. When you are using Java APIs to access Objective-C Enterprise Objects Framework classes, you have to take into consideration the way objects are deallocated on the Objective-C side of the Java Bridge. This means that you might still need to break reference cycles to help keep your application's memory in check. For example, suppose you have an Employee object that has a to-one relationship to its Department, and the Department object in turn has an array of Employee objects. You can use this method to break the reference cycle. Note that reference cycles are automatically broken if the EOEditingContext is finalized. For more discussion of this topic, see the section ["Methods for Managing the Object Graph"](EOEditingContext-2.md) in the class description.

__See also:__ - __invalidateObjectsWithGlobalIDs__

---

#### refaultObjects

public void __refaultObjects__ ()

()

Refaults all objects cached in the receiver that haven't been inserted, deleted, or updated. Invokes __processRecentChanges__ , then invokes __refaultObject__ for all objects that haven't been inserted, deleted, or updated. For more discussion of this topic, see the section ["Methods for Managing the Object Graph"](EOEditingContext-2.md) in the class description.

---

#### refetch

public void __refetch__ ()

This method simply invokes the __invalidateAllObjects__ method.

---

#### registeredObjects

public NSArray __registeredObjects__ ()

Returns the enterprise objects managed by the receiver.

---

#### removeEditor

public void __removeEditor__ (java.lang.Object _anObject_)

Unregisters _editor_ from the receiver. For more discussion of EOEditors, see the __editors__ method description and the [EOEditingContext.Editor](EOEditingContext.Editor.md) interface specification.

__See also:__ - __addEditor__

---

#### revert

public void __revert__ ()

()

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Removes everything from the undo stack, discards all insertions and deletions, and restores updated objects to their last committed values. Does not refetch from the database. Note that __revert__ doesn't automatically cause higher level display groups (WebObject's WODisplayGroups or the interface layer's EODisplayGroups) to refetch. Display groups that allow insertion and deletion of objects need to be explicitly synchronized whenever this method is invoked on their EOEditingContext.

__See also:__ - __invalidateAllObjects__

---

#### rootObjectStore

public EOObjectStore __rootObjectStore__ ()

Returns the EOObjectStore at the base of the object store hierarchy (usually an EOObjectStoreCoordinator).

---

#### saveChanges

public void __saveChanges__ ()

public void __saveChanges__ (java.lang.Object _anObject_) (Siva only)

()

Commits changes made in the receiver to its parent EOObjectStore by sending it the message __saveChangesInEditingContext__ . If the parent is an EOObjectStoreCoordinator, it guides its EOCooperatingObjectStores, typically EODatabaseContexts, through a multi-pass save operation (see the EOObjectStoreCoordinator class specification for more information). If a database error occurs, an exception is thrown; the error message indicates the nature of the problem.

---

#### saveChangesInEditingContext

public void __saveChangesInEditingContext__ (EOEditingContext _anEditingContext_)

Overrides the implementation inherited from EOObjectStore to tell the receiver's EOObjectStore to accept changes from a child EOEditingContext. This method shouldn't be invoked directly. It's invoked by a nested EOEditingContext when it's committing changes to a parent EOEditingContext. The receiving parent EOEditingContext incorporates all changes from the nested EOEditingContext into its own copies of the objects, but it doesn't immediately save those changes to the database. If the parent itself is later sent __saveChanges__ , it propagates any changes received from the child along with any other changes to its parent EOObjectStore. Throws an exception if an error occurs; the error message indicates the nature of the problem.

---

#### setDelegate

public void __setDelegate__ (java.lang.Object _anObject_)

Set the receiver's delegate to be _anObject_.

__See also:__ - __delegate__

---

#### setInvalidatesObjectsWhenFreed

public void __setInvalidatesObjectsWhenFreed__ (boolean _flag_)

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Sets according to _flag_ whether the receiver clears and "booby-traps" all of the objects registered with it when the receiver is finalized. If an editing context invalidates objects when it's finalized, it sends a [__clearProperties__](EOEnterpriseObject.md)message to all of its objects, thereby breaking any reference cycles between objects that would prevent them from being finalized. This method leaves the objects in a state in which sending them any message throws an exception.

The default is __true__ , and as a general rule, this setting must be __true__ for enterprise objects with cyclic references to be finalized when their EOEditingContext is finalized.

Note that the word "invalidate" in this method name has a different meaning than it does in the other `invalidate...` methods, which discard object values and refault them.

When you are using Java APIs to access Objective-C Enterprise Objects Framework classes, you have to take into consideration the way objects are deallocated on the Objective-C side of the Java Bridge. This means that you might still need to break reference cycles to help keep your application' the objects usage in check.

__See also:__ - __invalidatesObjectsWhenFreed__

---

#### setLocksObjectsBeforeFirstModification

public void __setLocksObjectsBeforeFirstModification__ (boolean _flag_)

Sets according to _flag_ whether the receiver locks _object_ in the external store (with __lockObject__ ) the first time _object_ is modified. The default is __false__ . If _flag_ is __true__ , an exception will be thrown raised if a lock can't be obtained when _object_ invokes [__willChange__](EOEnterpriseObject.md). There are two reasons a lock might fail: because the row is already locked in the server, or because your snapshot is out of date. If your snapshot is out of date, you can explicitly refetch the object using an EOFetchSpecification with [__setRefreshesRefetchedObjects__](EOFetchSpecification.md)set to __true__ . To handle the exception, you can implement the EODatabaseContext delegate method __databaseContextShouldRaiseExceptionForLockFailure__ .

You should avoid using this method or pessimistic locking in an interactive end-user application. For example, a user might make a change in a text field and neglect to save it, thereby leaving the data locked in the server indefinitely. Consider using optimistic locking or application level explicit check-in/check-out instead.

__See also:__ - __locksObjectsBeforeFirstModification__

---

#### setMessageHandler

public void __setMessageHandler__ (java.lang.Object _handler_)

Set the receiver's message handler to be _handler_.

__See also:__ - __messageHandler__

---

#### setPropagatesDeletesAtEndOfEvent

public void __setPropagatesDeletesAtEndOfEvent__ (boolean _flag_)

This method is only available on Yellow Box; it has no effect in Java Client.

Sets according to _flag_ whether the receiver propagates deletes at the end of the event in which a change was made, or only just before saving changes.

If _flag_ is __true__ , deleting an enterprise object triggers delete propagation at the end of the event in which the deletion occurred (this is the default behavior). If _flag_ is __false__ , delete propagation isn't performed until __saveChanges__ is invoked.

You can delete enterprise objects explicitly by using the __deleteObject__ method or implicitly by removing the enterprise object from an owning relationship. Delete propagation uses the delete rules in the EOClassDescription to determine whether objects related to the deleted object should also be deleted (for more information, see the [EOClassDescription](EOClassDescription.md) class specification and the [EOEnterpriseObject](EOEnterpriseObject.md) interface specification). If delete propagation fails (that is, if an enterprise object refuses to be deleted-possibly due to a deny rule), all changes made during the event are rolled back.

__See also:__ - __propagatesDeletesAtEndOfEvent__

---

#### setStopsValidationAfterFirstError

public void __setStopsValidationAfterFirstError__ (boolean _flag_)

Sets according to _flag_ whether the receiver stops validating after the first error is encountered, or continues for all objects (validation typically occurs during a save operation). The default is __true__ . Setting it to __false__ is useful if the delegate implements [__editingContextShouldPresentException__](EOEditingContext.Delegate.md)to handle the presentation of aggregate exceptions.

__See also:__ - __stopsValidationAfterFirstError__

---

#### setUndoManager

public void __setUndoManager__ (NSUndoManager _undoManager_)

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Sets the receiver's NSUndoManager to _undoManager_. You might invoke this method with __null__ if your application doesn't need undo and you want to avoid the overhead of an undo stack. For more information on editing context's undo support, see the section "[Undo and Redo](EOEditingContext-2.md)."

__See also:__ - __undoManager__

---

#### stopsValidationAfterFirstError

public boolean __stopsValidationAfterFirstError__ ()

()

Returns __true__ to indicate that the receiver should stop validating after it encounters the first error, or __false__ to indicate that it should continue for all objects.

__See also:__ - __setStopsValidationAfterFirstError__

---

#### undo

public void __undo__ ()

This method is available for Yellow Box applications only; there is no Java Client equivalent.

This method forwards an __undo__ message to the receiver's NSUndoManager, asking it to reverse the latest uncommitted changes applied to objects in the object graph. For more information on editing context's undo support, see the section "[Undo and Redo](EOEditingContext-2.md)."

__See also:__ __redo__

---

#### undoManager

public NSUndoManager __undoManager__ ()

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Returns the receiver's NSUndoManager.

__See also:__ - __setUndoManager__

---

#### unlock

public void __unlock__ ()

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Unlocks access to the receiver so that other threads may access it.

---

__Warning:__ This method creates an NSAutoreleasePool that is released when __unlock__ is called. Consequently, objects that have been autoreleased within the scope of a __lock__ /__unlock__ pair may not be valid after the __unlock__ .

---

__See also:__ - __lock__

---

#### updatedObjects

public NSArray __updatedObjects__ ()

Returns the objects in the receiver's object graph that have been updated.

__See also:__ `-` __deletedObjects__ , `-` __insertedObjects__

## Notification

The following notifications are declared (except where otherwise noted) and posted by EOEditingContext.

---

### EditingContextDidSaveChangesNotification

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

### InvalidatedAllObjectsInStoreNotification

This notification is defined by EOObjectStore. When posted by an EOEditingContext, it's the result of the editing context invalidating all its objects. When an EOEditingContext receives an [InvalidatedAllObjectsInStoreNotification](EOObjectStore.md) from its parent EOObjectStore, it clears its lists of inserted, updated, and deleted objects, and resets its undo stack. The notification contains:`| Notification Object | The EOEditingContext |
| userInfo Dictionary | None. |

|  |
| --- |
|  |`

An interface layer EODisplayGroup (not a WebObjects WODisplayGroup) listens for this notification to refetch its contents. See the EOObjectStore class specification for more information on this notification.

---

### ObjectsChangedInStoreNotification

This notification is defined by EOObjectStore. When posted by an EOEditingContext, it's the result of the editing context processing __objectWillChange__ observer notifications in __processRecentChanges__ , which is usually as the end of the event in which the changes occurred. See the EOObjectStore class specification for more information on [ObjectsChangedInStoreNotification](EOObjectStore.md).

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

### ObjectsChangedInEditingContextNotification

This notification is broadcast whenever changes are made in an EOEditingContext. It's similar to ObjectsChangedInStoreNotification, except that it contains objects rather than globalIDs. The notification contains:

| __Notification Object__ | The EOEditingContext |
| userInfo Dictionary | userInfo Dictionary |
| __Key__ | __Value__ |
| UpdatedKey | An NSArray containing the changed objects |
| DeletedKey | An NSArray containing the deleted objects |
| InsertedKey | An NSArray containing the inserted objects |
| InvalidatedKey | An NSArray containing invalidated objects. |

```
```

Interface layer EODisplayGroups (not WebObjects WODisplayGroups) listen for this notification to redisplay their contents.

---

[!](EODetailDataSource.md)
[!](EOEditingContext-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
