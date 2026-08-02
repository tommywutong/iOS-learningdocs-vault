---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOCooperatingObjectStore.html
archived_at: '2026-07-18T01:28:24.622927Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOClassDescription-2.md)
[!](EOCustomObject.md)

---

# EOCooperatingObjectStore

__Inherits From:__
EOObjectStore : NSObject

__Package:__
com.apple.yellow.eocontrol (Yellow Box)

## Class Description

EOCooperatingObjectStore is a part of the control layer's object storage abstraction. It is an abstract class that defines the basic API for object stores that work together to manage data from several distinct data repositories. It is for use in WebObjects and Yellow Box applications only; there is no equivalent class for Java Client applications. For more general information on the object storage abstraction, see ["Object Storage Abstraction"](The%20EOControl%20Framework.md) in the introduction to the EOControl Framework.

The interaction between EOCooperatingObjectStores is managed by another class, EOObjectStoreCoordinator. The EOObjectStoreCoordinator communicates changes to its EOCooperatingObjectStores by passing them an EOEditingContext. Each cooperating store examines the modified objects in the editing context and determines if it's responsible for handling the changes. When a cooperating store has changes that need to be handled by another store, it communicates the changes to the other store back through the coordinator.

For relational databases, Enterprise Objects Framework provides a concrete subclass of EOCooperatingObjectStore, EODatabaseContext (EOAccess). A database context represents a single connection to a database server, fetching and saving objects on behalf of one or more editing contexts. However, a database context and an editing context don't interact with each other directly-a coordinator acts as a mediator between them.

!

## Method Types

**Committing or discarding changes**

**- commitChanges

**- performChanges

**- rollbackChanges

**- prepareForSaveWithCoordinator

**- recordChangesInEditingContext

**- recordUpdateForObject************

**Returning information about objects**

**- valuesForKeys**

**Determining if the EOCooperatingObjectStore is responsible for an operation**

**- ownsObject

**- ownsGlobalID

**- handlesFetchSpecification******

## Instance Methods

---

#### commitChanges

public abstract void __commitChanges__ ()

Overridden by subclasses to commit the transaction. Throws an exception if an error occurs; the error message indicates the nature of the problem.

__See also:__ - __performChanges__ , - __commitChanges__ , [- __saveChangesInEditingContext__](EOObjectStoreCoordinator.md)(EOObjectStoreCoordinator)

---

#### handlesFetchSpecification

public abstract boolean __handlesFetchSpecification__ (EOFetchSpecification _fetchSpecification_)

Overridden by subclasses to return __true__ if the receiver is responsible for fetching the objects described by _fetchSpecification_. For example, EODatabaseContext (EOAccess) determines whether it's responsible based on _fetchSpecification_'s entity name.

__See also:__ - __ownsGlobalID__ , - __ownsObject__

---

#### ownsGlobalID

public abstract boolean __ownsGlobalID__ (EOGlobalID _globalID_)

Overridden by subclasses to return __true__ if the receiver is responsible for fetching and saving the object identified by _globalID_. For example, EODatabaseContext (EOAccess) determines whether it's responsible based on the entity associated with _globalID_.

__See also:__ - __handlesFetchSpecification__ , - __ownsObject__

---

#### ownsObject

public abstract boolean __ownsObject__ (java.lang.Object _object_)

Overridden by subclasses to return __true__ if the receiver is responsible for fetching and saving _object_. For example, EODatabaseContext (EOAccess) determines whether it's responsible based on the entity associated with _object_.

__See also:__ - __ownsGlobalID__ , - __handlesFetchSpecification__

---

#### performChanges

public abstract void __performChanges__ ()

()

Overridden by subclasses to transmit changes to the receiver's underlying database. Raises an exception if an error occurs; the error message indicates the nature of the problem.

__See also:__ - __commitChanges__ , - __rollbackChanges__ , [- __saveChangesInEditingContext__](EOObjectStoreCoordinator.md)(EOObjectStoreCoordinator)

---

#### prepareForSaveWithCoordinator

public abstract void __prepareForSaveWithCoordinator__ (
EOObjectStoreCoordinator _coordinator_,
EOEditingContext _anEditingContext_)

Overridden by subclasses to notify the receiver that a multi-store save operation overseen by _coordinator_ is beginning for _anEditingContext_. For example, the receiver might prepare primary keys for newly inserted objects so that they can be handed out to other EOCooperatingObjectStores upon request. The receiver should be prepared to receive the messages __recordChangesInEditingContext__ and __recordUpdateForObject__ .

After performing these methods, the receiver should be prepared to receive the possible messages __performChanges__ and then __commitChanges__ or __rollbackChanges__ .

---

#### recordChangesInEditingContext

public abstract void __recordChangesInEditingContext__ ()

()

Overridden by subclasses to instruct the receiver to examine the changed objects in the receiver's EOEditingContext, record any operations that need to be performed, and notify the receiver's EOObjectStoreCoordinator of any changes that need to be forwarded to other EOCooperatingObjectStores.

__See also:__ - __prepareForSaveWithCoordinator__ , - __recordUpdateForObject__

---

#### recordUpdateForObject

public abstract void __recordUpdateForObject__ (
java.lang.Object _object_,
NSDictionary _changes_)

Overridden by subclasses to communicate from one EOCooperatingObjectStore to another (through the EOObjectStoreCoordinator) that _changes_ need to be made to an _object_. For example, an insert of an object in a relationship property might require changing a foreign key property in an object owned by another EOCooperatingObjectStore. This method is primarily used to manipulate relationships.

__See also:__ - __prepareForSaveWithCoordinator__ , - __recordChangesInEditingContext__

---

#### rollbackChanges

public abstract void __rollbackChanges__ ()

()

Overridden by subclasses to roll back changes to the underlying database. Raises one of several possible exceptions if an error occurs; the error message should indicate the nature of the problem.

__See also:__ - __commitChanges__ , - __performChanges__ , [- __saveChangesInEditingContext__](EOObjectStoreCoordinator.md)(EOObjectStoreCoordinator)

---

#### valuesForKeys

public abstract NSDictionary __valuesForKeys__ (
NSArray _keys_,
java.lang.Object _object_)

Overridden by subclasses to return values (as identified by _keys_) held by the receiver that augment properties in _object_. For instance, an EODatabaseContext (EOAccess) stores foreign keys for the objects it owns (and primary keys for new objects). These foreign and primary keys may well not be defined as properties of the object. Other database contexts can find out these keys by sending the database context that owns the object a __valuesForKeys__ message. Note that you use this for properties that are _not_ stored in the object, so using key-value coding directly on the object won't always work.

---

[!](EOClassDescription-2.md)
[!](EOCustomObject.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
