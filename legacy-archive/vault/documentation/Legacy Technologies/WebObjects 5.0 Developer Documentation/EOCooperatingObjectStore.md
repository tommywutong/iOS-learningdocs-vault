---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOCooperatingObjectStore.html
archived_at: '2026-07-15T08:13:46.172300Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOCooperatingObjectStore

> **__Inherits from:__**
> : [EOObjectStore](EOObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhu6ytkmvrxiu3un5zgk)

> **__Implements:__**
> : NSLocking

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

EOCooperatingObjectStore is a part of the control layer's object storage abstraction. It is an abstract class that defines the basic API for object stores that work together to manage data from several distinct data repositories.

For more general information on the object storage abstraction, see "Object Storage Abstraction" (page 23) in the introduction to the EOControl Framework.

The interaction between EOCooperatingObjectStores is managed by another class, EOObjectStoreCoordinator. The EOObjectStoreCoordinator communicates changes to its EOCooperatingObjectStores by passing them an EOEditingContext. Each cooperating store examines the modified objects in the editing context and determines if it's responsible for handling the changes. When a cooperating store has changes that need to be handled by another store, it communicates the changes to the other store back through the coordinator.

For relational databases, Enterprise Objects Framework provides a concrete subclass of EOCooperatingObjectStore, EODatabaseContext (EOAccess). A database context represents a single connection to a database server, fetching and saving objects on behalf of one or more editing contexts. However, a database context and an editing context don't interact with each other directly-a coordinator acts as a mediator between them.

![[image: Art/DBasic2.GIF]](Art/DBasic2.GIF)

## Interfaces Implemented

---

> : NSLocking: [lock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss63dpmnvq): [unlock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss65lonrxwg2y):

## Method Types

---

> **Committing or discarding changes**
> : [commitChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss6y3pnvwws5cdnbqw4z3fom): [ownsGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64dfojtg64tninugc3thmvzq): [rollbackChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64tpnrwgeyldnnbwqylom5sxg): [prepareForSaveWithCoordinator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64dsmvygc4tfizxxeu3bozsvo2lunbbw633smruw4ylun5za): [recordChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64tfmnxxezcdnbqw4z3fonew4rlenf2gs3thinxw45dfpb2a): [recordUpdateForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64tfmnxxezcvobsgc5dfizxxet3cnjswg5a)
>
> **Returning information about objects**
> : [valuesForKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss65tbnr2wk42gn5zewzlzom)
>
> **Determining if the EOCooperatingObjectStore is responsible for an operation**
> : [ownsObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss633xnzzu6ytkmvrxi): [ownsGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64dfojtg64tninugc3thmvzq): [handlesFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss62dbnzsgyzltizsxiy3iknygky3jmzuwgylunfxw4)

## Constructors

---

### EOCooperatingObjectStore

`public EOCooperatingObjectStore()`

Description forthcoming.

---

## Instance Methods

---

### commitChanges

`public abstract void commitChanges()`

Overridden by subclasses to commit the transaction. Throws an exception if an error occurs; the error message indicates the nature of the problem.

__See Also:__ [ownsGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64dfojtg64tninugc3thmvzq), [commitChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss6y3pnvwws5cdnbqw4z3fom), saveChangesInEditingContext (EOObjectStoreCoordinator)

---

### handlesFetchSpecification

`public abstract boolean handlesFetchSpecification(EOFetchSpecification fetchSpecification)`

Overridden by subclasses to return `true` if the receiver is responsible for fetching the objects described by _fetchSpecification_. For example, EODatabaseContext (EOAccess) determines whether it's responsible based on _fetchSpecification_'s entity name.

__See Also:__ [ownsGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64dfojtg64tninugc3thmvzq), [ownsObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss633xnzzu6ytkmvrxi)

---

### lock

`public abstract void lock()`

Conformance to NSLocking.

---

### ownsGlobalID

`public abstract boolean ownsGlobalID(EOGlobalID globalID)`

Overridden by subclasses to return `true` if the receiver is responsible for fetching and saving the object identified by _globalID_. For example, EODatabaseContext (EOAccess) determines whether it's responsible based on the entity associated with _globalID_.

__See Also:__ [handlesFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss62dbnzsgyzltizsxiy3iknygky3jmzuwgylunfxw4), [ownsObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss633xnzzu6ytkmvrxi)

---

### ownsObject

`public abstract boolean ownsObject(EOEnterpriseObject anEO)`

Overridden by subclasses to return `true` if the receiver is responsible for fetching and saving _anEO_. For example, EODatabaseContext (EOAccess) determines whether it's responsible based on the entity associated with _anEO_.

__See Also:__ [ownsGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64dfojtg64tninugc3thmvzq), [handlesFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss62dbnzsgyzltizsxiy3iknygky3jmzuwgylunfxw4)

---

### performChanges

`public abstract void performChanges()`

Overridden by subclasses to transmit changes to the receiver's underlying database. Raises an exception if an error occurs; the error message indicates the nature of the problem.

__See Also:__ [commitChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss6y3pnvwws5cdnbqw4z3fom), [rollbackChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64tpnrwgeyldnnbwqylom5sxg), saveChangesInEditingContext (EOObjectStoreCoordinator)

---

### prepareForSaveWithCoordinator

`public abstract void prepareForSaveWithCoordinator( EOObjectStoreCoordinator coordinator, EOEditingContext anEditingContext)`

Overridden by subclasses to notify the receiver that a multi-store save operation overseen by _coordinator_ is beginning for _anEditingContext_. For example, the receiver might prepare primary keys for newly inserted objects so that they can be handed out to other EOCooperatingObjectStores upon request. The receiver should be prepared to receive the messages [recordChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64tfmnxxezcdnbqw4z3fonew4rlenf2gs3thinxw45dfpb2a) and [recordUpdateForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64tfmnxxezcvobsgc5dfizxxet3cnjswg5a).

After performing these methods, the receiver should be prepared to receive the possible messages [ownsGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64dfojtg64tninugc3thmvzq) and then [commitChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss6y3pnvwws5cdnbqw4z3fom) or [rollbackChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64tpnrwgeyldnnbwqylom5sxg).

---

### recordChangesInEditingContext

`public abstract void recordChangesInEditingContext()`

Overridden by subclasses to instruct the receiver to examine the changed objects in the receiver's EOEditingContext, record any operations that need to be performed, and notify the receiver's EOObjectStoreCoordinator of any changes that need to be forwarded to other EOCooperatingObjectStores.

__See Also:__ [prepareForSaveWithCoordinator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64dsmvygc4tfizxxeu3bozsvo2lunbbw633smruw4ylun5za), [recordUpdateForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64tfmnxxezcvobsgc5dfizxxet3cnjswg5a)

---

### recordUpdateForObject

`public abstract void recordUpdateForObject( EOEnterpriseObject anEO, NSDictionary changes)`

Overridden by subclasses to communicate from one EOCooperatingObjectStore to another (through the EOObjectStoreCoordinator) that _changes_ need to be made to an _anEO_. For example, an insert of an object in a relationship property might require changing a foreign key property in an object owned by another EOCooperatingObjectStore. This method is primarily used to manipulate relationships.

__See Also:__ [prepareForSaveWithCoordinator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64dsmvygc4tfizxxeu3bozsvo2lunbbw633smruw4ylun5za), [recordChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64tfmnxxezcdnbqw4z3fonew4rlenf2gs3thinxw45dfpb2a)

---

### rollbackChanges

`public abstract void rollbackChanges()`

Overridden by subclasses to roll back changes to the underlying database. Raises one of several possible exceptions if an error occurs; the error message should indicate the nature of the problem.

__See Also:__ [commitChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss6y3pnvwws5cdnbqw4z3fom), [ownsGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64dfojtg64tninugc3thmvzq), saveChangesInEditingContext (EOObjectStoreCoordinator)

---

### unlock

`public abstract void unlock()`

Conformance to NSLocking.

---

### valuesForKeys

`public abstract NSDictionary valuesForKeys( NSArray keys, EOEnterpriseObject anEO)`

Overridden by subclasses to return values (as identified by _keys_) held by the receiver that augment properties in _anEO_. For instance, an EODatabaseContext (EOAccess) stores foreign keys for the objects it owns (and primary keys for new objects). These foreign and primary keys may well not be defined as properties of the object. Other database contexts can find out these keys by sending the database context that owns the object a __valuesForKeys__ message. Note that you use this for properties that are _not_ stored in the object, so using key-value coding directly on the object won't always work.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
