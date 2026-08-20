---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOObjectStoreCoordinator.html
archived_at: '2026-07-18T01:28:36.854613Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOObjectStore-2.md)
[!](EOObserverCenter-2.md)

---

# EOObjectStoreCoordinator

__Inherits From:__
EOObjectStore : NSObject

__Conforms To:__ NSObject (NSObject)

__Declared in:__ EOControl/EOObjectStoreCoordinator.h

EOObjectStoreCoordinator is a part of the control layer's object storage abstraction. An EOObjectStoreCoordinator object acts as a single object store by directing one or more EOCooperatingObjectStores in managing objects from distinct data repositories. For more general information on the object storage abstraction, see ["Object Storage Abstraction"](The%20EOControl%20Framework-2.md) in the introduction to the EOControl Framework.

---

### EOObjectStore Methods

EOObjectStoreCoordinator overrides the following EOObjectStore methods:

- [- objectsWithFetchSpecification:editingContext:](EOObjectStore-2.md)
- [- objectsForSourceGlobalID:relationshipName:editingContext:](EOObjectStore-2.md)
- [- faultForGlobalID:editingContext:](EOObjectStore-2.md)
- [- arrayFaultWithSourceGlobalID:relationshipName:editingContext:](EOObjectStore-2.md)
- [- refaultObject:withGlobalID:editingContext:](EOObjectStore-2.md)
- [- saveChangesInEditingContext:](EOObjectStore-2.md)
- [- invalidateAllObjects](EOObjectStore-2.md)
- [- invalidateObjectsWithGlobalIDs:](EOObjectStore-2.md)

With the exception of [__saveChangesInEditingContext:__](EOObjectStore-2.md), EOObjectStoreCoordinator's implementation of these methods simply forwards the message to an EOCooperatingObjectStore or stores. The message [__invalidateAllObjects__](EOObjectStore-2.md)is forwarded to all of a coordinator's cooperating stores. The rest of the messages are forwarded to the appropriate store based on which store responds YES to the messages [__ownsGlobalID:__](EOCooperatingObjectStore-2.md), [__ownsObject:__](EOCooperatingObjectStore-2.md), and [__handlesFetchSpecification:__](EOCooperatingObjectStore-2.md)(which message is used depends on the context). The EOObjectStore methods listed above aren't documented in this class specification (except for __saveChangesInEditingContext:__ )-for descriptions of them, see the [EOObjectStore](EOObjectStore-2.md) and EODatabaseContext (EOAccess) class specifications

For the method __saveChangesInEditingContext:__ , the coordinator guides its cooperating stores through a multi-pass save protocol in which each cooperating store saves its own changes and forwards remaining changes to the other of the coordinator's stores. For example, if in its [__recordChangesInEditingContext__](EOCooperatingObjectStore-2.md)method one cooperating store notices the removal of an object from an "owning" relationship but that object belongs to another cooperating store, it informs the other store by sending the coordinator a __forwardUpdateForObject:changes:__ message. For a more details, see the method description for __saveChangesInEditingContext:__ .

Although it manages objects from multiple repositories, EOObjectStoreCoordinator doesn't absolutely guarantee consistent updates when saving changes across object stores. If your application requires guaranteed distributed transactions, you can either provide your own solution by creating a subclass of EOObjectStoreCoordinator that integrates with a TP monitor, use a database server with built-in distributed transaction support, or design your application to write to only one object store per save operation (though it may read from multiple object stores). For more discussion of this subject, see the method description for __saveChangesInEditingContext:__ .

**Initializing instances**

**- init**

**Setting the default coordinator**

**+ setDefaultCoordinator:

**+ defaultCoordinator****

**Managing EOCooperatingObjectStores**

**- addCooperatingObjectStore:

**- removeCooperatingObjectStore:

**- cooperatingObjectStores******

**Saving changes**

**- saveChangesInEditingContext:**

**Communication between EOCooperatingObjectStores**

**- forwardUpdateForObject:changes:

**- valuesForKeys:object:****

**Returning EOCooperatingObjectStores**

**- objectStoreForGlobalID:

**- objectStoreForFetchSpecification:

**- objectStoreForObject:******

**Getting the userInfo dictionary**

**- userInfo

**- setUserInfo:****

---

#### defaultCoordinator

+ (id)`defaultCoordinator`

Returns a shared instance of EOObjectStoreCoordinator.

---

#### setDefaultCoordinator:

+ (void)`setDefaultCoordinator:`(EOObjectStoreCoordinator \*)_coordinator_

Sets a shared instance EOObjectStoreCoordinator.

---

#### addCooperatingObjectStore:

- (void)`addCooperatingObjectStore:`(EOCooperatingObjectStore \*)_store_

Adds _store_ to the list of EOCooperatingObjectStores that need to be queried and notified about changes to enterprise objects. Posts the notification EOCooperatingObjectStoreWasAdded.

__See also:__ - __removeCooperatingObjectStore:__ , - __cooperatingObjectStores__

---

#### cooperatingObjectStores

- (NSArray \*)`cooperatingObjectStores`

Returns the receiver's EOCooperatingObjectStores.

__See also:__ - __addCooperatingObjectStore:__ , - __removeCooperatingObjectStore:__

---

#### forwardUpdateForObject:changes:

- (void)`forwardUpdateForObject:`(id)_object_`changes:`(NSDictionary \*)_changes_

Tells the receiver to forward a message from an EOCooperatingObjectStore to another store, informing it that _changes_ need to be made to _object_. For example, inserting an object in a relationship property of one EOCooperatingObjectStore might require changing a foreign key property in an object owned by another EOCooperatingObjectStore.

This method first locates the EOCooperatingObjectStore that's responsible for applying _changes_, and then it sends the store the message [__recordUpdateForObject:changes:__](EOCooperatingObjectStore-2.md).

---

#### init

- `init`

Initializes a newly allocated EOObjectStoreCoordinator and returns `self`_._ This is the designated initializer for the EOObjectStoreCoordinator class.

---

#### objectStoreForFetchSpecification:

- (EOCooperatingObjectStore \*)`objectStoreForFetchSpecification:`(EOFetchSpecification \*)_fetchSpecification_

Returns the EOCooperatingObjectStore responsible for fetching objects with _fetchSpecification_. Returns `nil` if no EOCooperatingObjectStore can be found that responds YES to [__handlesFetchSpecification:__](EOCooperatingObjectStore-2.md).

__See also:__ - __objectStoreForGlobalID:__ , - __objectStoreForObject:__

---

#### objectStoreForGlobalID:

- (EOCooperatingObjectStore \*)`objectStoreForGlobalID:`(EOGlobalID \*)_globalID_

Returns the EOCooperatingObjectStore for the object identified by _globalID_. Returns `nil` if no EOCooperatingObjectStore can be found that responds YES to [__ownsGlobalID:__](EOCooperatingObjectStore-2.md).

__See also:__ - __objectStoreForFetchSpecification:__ , - __objectStoreForObject:__

---

#### objectStoreForObject:

- (EOCooperatingObjectStore \*)`objectStoreForObject:`(id)_object_

Returns the EOCooperatingObjectStore that owns _object_. Returns `nil` if no EOCooperatingObjectStore can be found that responds YES to [__ownsObject:__](EOCooperatingObjectStore-2.md).

__See also:__ - __objectStoreForFetchSpecification:__ , - __objectStoreForGlobalID:__

---

#### removeCooperatingObjectStore:

- (void)`removeCooperatingObjectStore:`(EOCooperatingObjectStore \*)_store_

Removes _store_ from the list of EOCooperatingObjectStores that need to be queried and notified about changes to enterprise objects. Posts the notification EOCooperatingObjectStoreWasRemoved.

__See also:__ - __addCooperatingObjectStore:__ , - __cooperatingObjectStores__

---

#### saveChangesInEditingContext:

- (void)__saveChangesInEditingContext:__ (EOEditingContext \*)_anEditingContext_

Overrides the EOObjectStore implementation to save the changes made in _anEditingContext_. This message is sent by an EOEditingContext to an EOObjectStoreCoordinator to commit changes. When an EOObjectStoreCoordinator receives this message, it guides its EOCooperatingObjectStores through a multi-pass save protocol in which each EOCooperatingObjectStore saves its own changes and forwards remaining changes to other EOCooperatingObjectStores. When this method is invoked, the following sequence of events occurs:

- The receiver sends each of its EOCooperatingObjectStores the message [__prepareForSaveWithCoordinator:editingContext:__](EOCooperatingObjectStore-2.md), which informs them that a multi-pass save operation is beginning. When the EOCooperatingObjectStore is an EODatabaseContext (EOAccess), it takes this opportunity to generate primary keys for any new objects in the EOEditingContext.
- The receiver sends each of its EOCooperatingObjectStores the message [__recordChangesInEditingContext__](EOCooperatingObjectStore-2.md), which prompts them to examine the changed objects in the editing context, record operations that need to be performed, and notify the receiver of any changes that need to be forwarded to other stores. For example, if in its [__recordChangesInEditingContext__](EOCooperatingObjectStore-2.md)method one EOCooperatingObjectStore notices the removal of an object from an "owning" relationship but that object belongs to another EOCooperatingObjectStore, it informs the other store by sending the coordinator a __forwardUpdateForObject:changes:__
message. - The receiver sends each of its EOCooperatingObjectStores the message [__performChanges__](EOCooperatingObjectStore-2.md). This tells the stores to transmit their changes to their underlying databases. When the EOCooperatingObjectStore is an EODatabaseContext, it responds to this message by taking the EODatabaseOperations (EOAccess) that were constructed in the previous step, constructing EOAdaptorOperations (EOAccess) from them, and giving the EOAdaptorOperations to an available EOAdaptorChannel(EOAccess) for execution.
- If [__performChanges__](EOCooperatingObjectStore-2.md)fails for any of the EOCooperatingObjectStores, all stores are sent the message [__rollbackChanges__](EOCooperatingObjectStore-2.md).
- If [__performChanges__](EOCooperatingObjectStore-2.md)succeeds for all EOCooperatingObjectStores, the receiver sends them the message [__commitChanges__](EOCooperatingObjectStore-2.md), which has the effect of telling the adaptor to commit the changes.
- If [__commitChanges__](EOCooperatingObjectStore-2.md)fails for a particular EOCooperatingObjectStore, that store and all subsequent ones are sent the message [__rollbackChanges__](EOCooperatingObjectStore-2.md). However, the stores that have already committed their changes do not roll back. In other words, the coordinator doesn't perform the two-phase commit protocol necessary to guarantee consistent distributed update.

This method raises an exception if an error occurs.

---

#### setUserInfo:

- (void)`setUserInfo`:(NSDictionary \*)_dictionary_

Sets the _dictionary_ of auxiliary data, which your application can use for whatever it needs.

__See also:__ - __userInfo__

---

#### userInfo

- (NSDictionary \*)`userInfo`

Returns a dictionary of user data. Your application can use this to store any auxiliary information it needs.

__See also:__ - __setUserInfo:__

---

#### valuesForKeys:object:

- (NSDictionary \*)`valuesForKeys:`(NSArray \*)_keys_`object:`(id)_object_

Communicates with the appropriate EOCooperatingObjectStore to get the values identified by _keys_ for _object_, so that it can then forward them on to another EOCooperatingObjectStore. EOCooperatingObjectStores can hold values for an object that augment the properties in the object. For instance, an EODatabaseContext (EOAccess) stores foreign key information for the objects it owns. These foreign keys may well not be defined as properties of the object. Other EODatabaseContexts can find out the object's foreign keys by sending the EODatabaseContext that owns the object a __valuesForKeys:object:__ message(through the coordinator).

## Notification

**The following notifications are declared and posted by EOObjectStoreCoordinator.**

---

### EOCooperatingObjectStoreWasAdded

When an EOObjectStoreCoordinator receives an __addCooperatingObjectStore:__ message and adds an EOCooperatingObjectStore to its list, it posts EOCooperatingObjectStoreWasAdded to notify observers.

| __Notification Object__ | The EOObjectStoreCoordinator |
| __userInfo Dictionary__ | None |

```
```


---

### EOCooperatingObjectStoreWasRemoved

When an EOObjectStoreCoordinator receives a __removeCooperatingObjectStore:__ message and removes an EOCooperatingObjectStore from its list, it posts EOCooperatingObjectStoreWasRemoved to notify observers.

| __Notification Object__ | The EOObjectStoreCoordinator |
| __userInfo Dictionary__ | None |

```
```


---

### EOCooperatingObjectStoreNeeded

Posted when an EOObjectStoreCoordinator receives a request that it can't service with any of its currently registered EOCooperatingObjectStores. The observer can call back to the coordinator to register an appropriate EOCooperatingObjectStore based on the information in the userInfo dictionary.

| __`Notification Object`__ | The EOObjectStoreCoordinator |
| userInfo Dictionary | One of the following key-value pairs |
| __Key__ | __Value__ |
| globalID | globalID for the operation |
| fetchSpecification | fetch specification for the operation |
| object | object for the operation |

```
```

---

[!](EOObjectStore-2.md)
[!](EOObserverCenter-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
