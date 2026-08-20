---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOCooperatingObjStr.html
archived_at: '2026-07-15T08:11:39.196104Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOCooperatingObjectStore

> **__Inherits
> from:__**
> : [EOObjectStore](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#//apple_ref/occ/cl/EOObjectStore) : NSObject

> **__Conforms to:__**
> : NSObject
> : (NSObject)

> __Declared in:__ : EOControl/EOObjectStoreCoordinator.h

---

## Class Description

---

EOCooperatingObjectStore is a part of the
control layer's object storage abstraction. It is an abstract class
that defines the basic API for object stores that work together
to manage data from several distinct data repositories.

For more general information on the object storage abstraction,
see ["Object Storage Abstraction"](The%20EOControl%20Framework-2.md#apple-ijeucq2bjffek) in the introduction to the EOControl
Framework.

The interaction between EOCooperatingObjectStores is managed
by another class, EOObjectStoreCoordinator. The EOObjectStoreCoordinator
communicates changes to its EOCooperatingObjectStores by passing
them an EOEditingContext. Each cooperating store examines the modified
objects in the editing context and determines if it's responsible
for handling the changes. When a cooperating store has changes that
need to be handled by another store, it communicates the changes
to the other store back through the coordinator.

For relational databases, Enterprise Objects Framework provides
a concrete subclass of EOCooperatingObjectStore, EODatabaseContext
(EOAccess). A database context represents a single connection to
a database server, fetching and saving objects on behalf of one
or more editing contexts. However, a database context and an editing
context don't interact with each other directly-a coordinator
acts as a mediator between them.

![[image: Art/DBasic2.GIF]](Art/DBasic2.GIF)

## Method Types

---

> **Committing or discarding
> changes**
> : [- commitChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxwg33nnvuxiq3imfxgozlt)
> : [- ownsGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxazlsmzxxe3kdnbqw4z3fom)
> : [- rollbackChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxe33mnrrgcy3linugc3thmvzq)
> : [- prepareForSaveWithCoordinator:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxa4tfobqxezkgn5zfgylwmvlws5diinxw64tenfxgc5dpoi5gkzdjoruw4z2dn5xhizlyoq5a)
> : [- recordChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxezldn5zgiq3imfxgozltjfxekzdjoruw4z2dn5xhizlyoq)
> : [- recordUpdateForObject:changes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxezldn5zgivlqmrqxizkgn5ze6ytkmvrxiotdnbqw4z3fom5a)
>
> **Returning information
> about objects**
> : [- valuesForKeys:object:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxmylmovsxgrtpojfwk6lthjxwe2tfmn2du)
>
> **Determining if the EOCooperatingObjectStore
> is responsible for an operation**
> : [- ownsObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxw653oonhwe2tfmn2du)
> : [- ownsGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxazlsmzxxe3kdnbqw4z3fom)
> : [- handlesFetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxwqylomrwgk42gmv2gg2ctobswg2lgnfrwc5djn5xdu)

## Instance Methods

---

### commitChanges

`- (void)commitChanges`

Overridden by subclasses to commit the transaction. Raises an
exception if an error occurs; the error message indicates the nature
of the problem.

__See Also:__  [- ownsGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxazlsmzxxe3kdnbqw4z3fom), [- commitChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxwg33nnvuxiq3imfxgozlt), [- saveChangesInEditingContext:](EOObjectStoreCoordinator-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixxgylwmvbwqylom5sxgsloivsgs5djnztug33oorsxq5b2) ( [EOObjectStoreCoordinator](EOObjectStoreCoordinator-2.md#apple-ivhu6ytkmvrxiu3un5zgkq3pn5zgi2lomf2g64q))

---

### handlesFetchSpecification:

`- (BOOL)handlesFetchSpecification:(EOFetchSpecification
*)fetchSpecification`

Overridden by subclasses to return YES if the
receiver is responsible for fetching the objects described by _fetchSpecification_.
For example, EODatabaseContext (EOAccess) determines whether it's responsible
based on _fetchSpecification_'s entity
name.

__See Also:__  [- ownsGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxazlsmzxxe3kdnbqw4z3fom), [- ownsObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxw653oonhwe2tfmn2du)

---

### ownsGlobalID:

`- (BOOL)ownsGlobalID:(EOGlobalID
*)globalID`

Overridden by subclasses to return YES if the
receiver is responsible for fetching and saving the object identified
by _globalID_. For example, EODatabaseContext
(EOAccess) determines whether it's responsible based on the entity
associated with _globalID_.

__See
Also:__  [- handlesFetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxwqylomrwgk42gmv2gg2ctobswg2lgnfrwc5djn5xdu), [- ownsObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxw653oonhwe2tfmn2du)

---

### ownsObject:

`- (BOOL)ownsObject:(id)object`

Overridden by subclasses to return YES if the
receiver is responsible for fetching and saving _object_.
For example, EODatabaseContext (EOAccess) determines whether it's
responsible based on the entity associated with _object_.

__See
Also:__  [- ownsGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxazlsmzxxe3kdnbqw4z3fom), [- handlesFetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxwqylomrwgk42gmv2gg2ctobswg2lgnfrwc5djn5xdu)

---

### performChanges

`- (void)performChanges`

Overridden by subclasses to transmit changes
to the receiver's underlying database. Raises an exception if
an error occurs; the error message indicates the nature of the problem.

__See
Also:__  [- commitChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxwg33nnvuxiq3imfxgozlt), [- rollbackChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxe33mnrrgcy3linugc3thmvzq), [- saveChangesInEditingContext:](EOObjectStoreCoordinator-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixxgylwmvbwqylom5sxgsloivsgs5djnztug33oorsxq5b2) ( [EOObjectStoreCoordinator](EOObjectStoreCoordinator-2.md#apple-ivhu6ytkmvrxiu3un5zgkq3pn5zgi2lomf2g64q))

---

### prepareForSaveWithCoordinator:editingContext:

`- (void)prepareForSaveWithCoordinator:(EOObjectStoreCoordinator
*)coordinator
editingContext:(EOEditingContext
*)anEditingContext`

Overridden by subclasses to notify the receiver
that a multi-store save operation overseen by _coordinator_ is
beginning for _anEditingContext_. For
example, the receiver might prepare primary keys for newly inserted
objects so that they can be handed out to other EOCooperatingObjectStores
upon request. The receiver should be prepared to receive the messages [recordChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxezldn5zgiq3imfxgozltjfxekzdjoruw4z2dn5xhizlyoq) and [recordUpdateForObject:changes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxezldn5zgivlqmrqxizkgn5ze6ytkmvrxiotdnbqw4z3fom5a).

After
performing these methods, the receiver should be prepared to receive
the possible messages [ownsGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxazlsmzxxe3kdnbqw4z3fom) and then [commitChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxwg33nnvuxiq3imfxgozlt) or [rollbackChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxe33mnrrgcy3linugc3thmvzq).

---

### recordChangesInEditingContext

`- (void)recordChangesInEditingContext`

Overridden by subclasses to instruct the receiver
to examine the changed objects in the receiver's EOEditingContext,
record any operations that need to be performed, and notify the
receiver's EOObjectStoreCoordinator of any changes that need to
be forwarded to other EOCooperatingObjectStores.

__See
Also:__  [- prepareForSaveWithCoordinator:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxa4tfobqxezkgn5zfgylwmvlws5diinxw64tenfxgc5dpoi5gkzdjoruw4z2dn5xhizlyoq5a), [- recordUpdateForObject:changes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxezldn5zgivlqmrqxizkgn5ze6ytkmvrxiotdnbqw4z3fom5a)

---

### recordUpdateForObject:changes:

`- (void)recordUpdateForObject:(id)object
changes:(NSDictionary *)changes`

Overridden by subclasses to communicate from
one EOCooperatingObjectStore to another (through the EOObjectStoreCoordinator)
that _changes_ need to be made to an _object_.
For example, an insert of an object in a relationship property might
require changing a foreign key property in an object owned by another
EOCooperatingObjectStore. This method is primarily used to manipulate
relationships.

__See Also:__  [- prepareForSaveWithCoordinator:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxa4tfobqxezkgn5zfgylwmvlws5diinxw64tenfxgc5dpoi5gkzdjoruw4z2dn5xhizlyoq5a), [- recordChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxezldn5zgiq3imfxgozltjfxekzdjoruw4z2dn5xhizlyoq)

---

### rollbackChanges

`- (void)rollbackChanges`

Overridden by subclasses to roll back changes
to the underlying database. Raises one of several possible exceptions
if an error occurs; the error message should indicate the nature
of the problem.

__See Also:__  [- commitChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxwg33nnvuxiq3imfxgozlt), [- ownsGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxazlsmzxxe3kdnbqw4z3fom), [- saveChangesInEditingContext:](EOObjectStoreCoordinator-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixxgylwmvbwqylom5sxgsloivsgs5djnztug33oorsxq5b2) (EOObjectStoreCoordinator)

---

### valuesForKeys:object:

`- (NSDictionary *)valuesForKeys:(NSArray
*)keys
object:(id)object`

Overridden by subclasses to return values (as
identified by _keys_) held by the receiver
that augment properties in _object_.
For instance, an EODatabaseContext (EOAccess) stores foreign keys
for the objects it owns (and primary keys for new objects). These
foreign and primary keys may well not be defined as properties of
the object. Other database contexts can find out these keys by sending
the database context that owns the object a __valuesForKeys:object:__ message.
Note that you use this for properties that are _not_ stored
in the object, so using key-value coding directly on the object
won't always work.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
