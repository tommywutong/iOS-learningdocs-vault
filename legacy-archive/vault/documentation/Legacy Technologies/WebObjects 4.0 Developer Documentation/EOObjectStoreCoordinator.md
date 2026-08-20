---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOObjectStoreCoordinator.html
archived_at: '2026-07-18T01:28:26.865996Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOObjectStore.md)
[!](EOObserverCenter.md)

---

# EOObjectStoreCoordinator

__Inherits From:__
EOObjectStore : NSObject

__Package:__
com.apple.yellow.eocontrol (Yellow Box)

## Class Description

EOObjectStoreCoordinator is a part of the control layer's object storage abstraction. An EOObjectStoreCoordinator object acts as a single object store by directing one or more EOCooperatingObjectStores in managing objects from distinct data repositories. It is for use in WebObjects and Yellow Box applications only; there is no equivalent class for Java Client applications. For more general information on the object storage abstraction, see ["Object Storage Abstraction"](The%20EOControl%20Framework.md) in the introduction to the EOControl Framework.

---

### EOObjectStore Methods

EOObjectStoreCoordinator overrides the following EOObjectStore methods:

- [- objectsWithFetchSpecification](EOObjectStore.md)
- [- objectsForSourceGlobalID](EOObjectStore.md)
- [- faultForGlobalID](EOObjectStore.md)
- [- arrayFaultWithSourceGlobalID](EOObjectStore.md)
- [- refaultObject](EOObjectStore.md)
- [- saveChangesInEditingContext](EOObjectStore.md)
- [- invalidateAllObjects](EOObjectStore.md)
- [- invalidateObjectsWithGlobalIDs](EOObjectStore.md)

With the exception of [__saveChangesInEditingContext__](EOObjectStore.md), EOObjectStoreCoordinator's implementation of these methods simply forwards the message to an EOCooperatingObjectStore or stores. The message [__invalidateAllObjects__](EOObjectStore.md)is forwarded to all of a coordinator's cooperating stores. The rest of the messages are forwarded to the appropriate store based on which store responds __true__ to the messages [__ownsGlobalID__](EOCooperatingObjectStore.md), [__ownsObject__](EOCooperatingObjectStore.md), and [__handlesFetchSpecification__](EOCooperatingObjectStore.md)(which message is used depends on the context). The EOObjectStore methods listed above aren't documented in this class specification (except for __saveChangesInEditingContext__ )-for descriptions of them, see the [EOObjectStore](EOObjectStore.md) and EODatabaseContext (EOAccess) class specifications

For the method __saveChangesInEditingContext__ , the coordinator guides its cooperating stores through a multi-pass save protocol in which each cooperating store saves its own changes and forwards remaining changes to the other of the coordinator's stores. For example, if in its [__recordChangesInEditingContext__](EOCooperatingObjectStore.md)method one cooperating store notices the removal of an object from an "owning" relationship but that object belongs to another cooperating store, it informs the other store by sending the coordinator a __forwardUpdateForObject__ message. For a more details, see the method description for __saveChangesInEditingContext__ .

Although it manages objects from multiple repositories, EOObjectStoreCoordinator doesn't absolutely guarantee consistent updates when saving changes across object stores. If your application requires guaranteed distributed transactions, you can either provide your own solution by creating a subclass of EOObjectStoreCoordinator that integrates with a TP monitor, use a database server with built-in distributed transaction support, or design your application to write to only one object store per save operation (though it may read from multiple object stores). For more discussion of this subject, see the method description for __saveChangesInEditingContext__ .

## Constants

The following string constants define the names of EOObjectStoreCoordinator's notifications:

- CooperatingObjectStoreWasAdded
- CooperatingObjectStoreWasRemoved
- CooperatingObjectStoreNeeded

For more information, see the section "Notifications" below.

## Method Types

**Constructors**

**EOObjectStoreCoordinator**

**Setting the default coordinator**

**+ setDefaultCoordinator

**+ defaultCoordinator****

**Managing EOCooperatingObjectStores**

**- addCooperatingObjectStore

**- removeCooperatingObjectStore

**- cooperatingObjectStores******

**Saving changes**

**- saveChangesInEditingContext**

**Communication between EOCooperatingObjectStores**

**- forwardUpdateForObject

**- valuesForKeys****

**Returning EOCooperatingObjectStores**

**- objectStoreForGlobalID

**- objectStoreForFetchSpecification

**- objectStoreForObject******

**Getting the userInfo dictionary**

**- userInfo

**- setUserInfo****

## Constructors

---

#### EOObjectStoreCoordinator

public __EOObjectStoreCoordinator__ ()

Creates and returns an EOObjectStoreCoordinator.

## Static Methods

---

#### defaultCoordinator

public static java.lang.Object __defaultCoordinator__ ()

Returns a shared instance of EOObjectStoreCoordinator.

---

#### setDefaultCoordinator

public static void __setDefaultCoordinator__ (EOObjectStoreCoordinator _c__oordinator_)

Sets a shared instance EOObjectStoreCoordinator.

## Instance Methods

---

#### addCooperatingObjectStore

public void __addCooperatingObjectStore__ (EOCooperatingObjectStore _store_)

Adds _store_ to the list of EOCooperatingObjectStores that need to be queried and notified about changes to enterprise objects. Posts the notification CooperatingObjectStoreWasAdded.

__See also:__ - __removeCooperatingObjectStore__ , - __cooperatingObjectStores__

---

#### cooperatingObjectStores

public NSArray __cooperatingObjectStores__ ()

Returns the receiver's EOCooperatingObjectStores.

__See also:__ - __addCooperatingObjectStore__ , - __removeCooperatingObjectStore__

---

#### forwardUpdateForObject

public void __forwardUpdateForObject__ (
java.lang.Object _object_,
NSDictionary _changes_)

Tells the receiver to forward a message from an EOCooperatingObjectStore to another store, informing it that _changes_ need to be made to _object_. For example, inserting an object in a relationship property of one EOCooperatingObjectStore might require changing a foreign key property in an object owned by another EOCooperatingObjectStore.

This method first locates the EOCooperatingObjectStore that's responsible for applying _changes_, and then it sends the store the message [__recordUpdateForObject__](EOCooperatingObjectStore.md).

---

#### objectStoreForFetchSpecification

public EOCooperatingObjectStore __objectStoreForFetchSpecification__ (
EOFetchSpecification _fetchSpecification_)

Returns the EOCooperatingObjectStore responsible for fetching objects with _fetchSpecification_. Returns `null` if no EOCooperatingObjectStore can be found that responds __true__ to [__handlesFetchSpecification__](EOCooperatingObjectStore.md).

__See also:__ - __objectStoreForGlobalID__ , - __objectStoreForObject__

---

#### objectStoreForGlobalID

public EOCooperatingObjectStore __objectStoreForGlobalID__ (EOGlobalID _globalID_)

Returns the EOCooperatingObjectStore for the object identified by _globalID_. Returns `null` if no EOCooperatingObjectStore can be found that responds __true__ to [__ownsGlobalID__](EOCooperatingObjectStore.md).

__See also:__ - __objectStoreForFetchSpecification__ , - __objectStoreForObject__

---

#### objectStoreForObject

public EOCooperatingObjectStore __objectStoreForObject__ (java.lang.Object _object_)

Returns the EOCooperatingObjectStore that owns _object_. Returns `null` if no EOCooperatingObjectStore can be found that responds __true__ to [__ownsObject__](EOCooperatingObjectStore.md).

__See also:__ - __objectStoreForFetchSpecification__ , - __objectStoreForGlobalID__

---

#### removeCooperatingObjectStore

public void __removeCooperatingObjectStore__ (EOCooperatingObjectStore _store_)

Removes _store_ from the list of EOCooperatingObjectStores that need to be queried and notified about changes to enterprise objects. Posts the notification CooperatingObjectStoreWasRemoved.

__See also:__ - __addCooperatingObjectStore__ , - __cooperatingObjectStores__

---

#### saveChangesInEditingContext

public void __saveChangesInEditingContext__ (EOEditingContext _anEditingContext_)

Overrides the EOObjectStore implementation to save the changes made in _anEditingContext_. This message is sent by an EOEditingContext to an EOObjectStoreCoordinator to commit changes. When an EOObjectStoreCoordinator receives this message, it guides its EOCooperatingObjectStores through a multi-pass save protocol in which each EOCooperatingObjectStore saves its own changes and forwards remaining changes to other EOCooperatingObjectStores. When this method is invoked, the following sequence of events occurs:

- The receiver sends each of its EOCooperatingObjectStores the message [__prepareForSaveWithCoordinator__](EOCooperatingObjectStore.md), which informs them that a multi-pass save operation is beginning. When the EOCooperatingObjectStore is an EODatabaseContext (EOAccess), it takes this opportunity to generate primary keys for any new objects in the EOEditingContext.
- The receiver sends each of its EOCooperatingObjectStores the message [__recordChangesInEditingContext__](EOCooperatingObjectStore.md), which prompts them to examine the changed objects in the editing context, record operations that need to be performed, and notify the receiver of any changes that need to be forwarded to other stores. For example, if in its [__recordChangesInEditingContext__](EOCooperatingObjectStore.md)method one EOCooperatingObjectStore notices the removal of an object from an "owning" relationship but that object belongs to another EOCooperatingObjectStore, it informs the other store by sending the coordinator a __forwardUpdateForObject__
message. - The receiver sends each of its EOCooperatingObjectStores the message [__performChanges__](EOCooperatingObjectStore.md). This tells the stores to transmit their changes to their underlying databases. When the EOCooperatingObjectStore is an EODatabaseContext, it responds to this message by taking the EODatabaseOperations (EOAccess) that were constructed in the previous step, constructing EOAdaptorOperations (EOAccess) from them, and giving the EOAdaptorOperations to an available EOAdaptorChannel(EOAccess) for execution.
- If [__performChanges__](EOCooperatingObjectStore.md)fails for any of the EOCooperatingObjectStores, all stores are sent the message [__rollbackChanges__](EOCooperatingObjectStore.md).
- If [__performChanges__](EOCooperatingObjectStore.md)succeeds for all EOCooperatingObjectStores, the receiver sends them the message [__commitChanges__](EOCooperatingObjectStore.md), which has the effect of telling the adaptor to commit the changes.
- If [__commitChanges__](EOCooperatingObjectStore.md)fails for a particular EOCooperatingObjectStore, that store and all subsequent ones are sent the message [__rollbackChanges__](EOCooperatingObjectStore.md). However, the stores that have already committed their changes do not roll back. In other words, the coordinator doesn't perform the two-phase commit protocol necessary to guarantee consistent distributed update.

This method raises an exception if an error occurs.

---

#### setUserInfo

public void __setUserInfo__ (NSDictionary _dictionary_)

Sets the _dictionary_ of auxiliary data, which your application can use for whatever it needs.

__See also:__ - __userInfo__

---

#### userInfo

public NSDictionary __userInfo__ ()

Returns a dictionary of user data. Your application can use this to store any auxiliary information it needs.

__See also:__ - __setUserInfo__

---

#### valuesForKeys

public NSDictionary __valuesForKeys__ (
NSArray _keys_,
java.lang.Object _object_)

Communicates with the appropriate EOCooperatingObjectStore to get the values identified by _keys_ for _object_, so that it can then forward them on to another EOCooperatingObjectStore. EOCooperatingObjectStores can hold values for an object that augment the properties in the object. For instance, an EODatabaseContext (EOAccess) stores foreign key information for the objects it owns. These foreign keys may well not be defined as properties of the object. Other EODatabaseContexts can find out the object's foreign keys by sending the EODatabaseContext that owns the object a __valuesForKeys__ message(through the coordinator).

## Notification

**The following notifications are declared and posted by EOObjectStoreCoordinator.**

---

### CooperatingObjectStoreWasAdded

When an EOObjectStoreCoordinator receives an __addCooperatingObjectStore__ message and adds an EOCooperatingObjectStore to its list, it posts CooperatingObjectStoreWasAdded to notify observers.

| __Notification Object__ | The EOObjectStoreCoordinator |
| __userInfo Dictionary__ | None |

```
```


---

### CooperatingObjectStoreWasRemoved

When an EOObjectStoreCoordinator receives a __removeCooperatingObjectStore__ message and removes an EOCooperatingObjectStore from its list, it posts CooperatingObjectStoreWasRemoved to notify observers.

| __Notification Object__ | The EOObjectStoreCoordinator |
| __userInfo Dictionary__ | None |

```
```


---

### CooperatingObjectStoreNeeded

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

[!](EOObjectStore.md)
[!](EOObserverCenter.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
