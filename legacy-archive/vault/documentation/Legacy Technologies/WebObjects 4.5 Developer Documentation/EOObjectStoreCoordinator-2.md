---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStoreCoordinator.html
archived_at: '2026-07-15T08:11:39.908322Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOObjectStoreCoordinator

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

EOObjectStoreCoordinator is a part of the
control layer's object storage abstraction. An EOObjectStoreCoordinator
object acts as a single object store by directing one or more EOCooperatingObjectStores
in managing objects from distinct data repositories.

For more general information on the object storage abstraction,
see ["Object Storage Abstraction"](The%20EOControl%20Framework-2.md#apple-ijeucq2bjffek) in the introduction to the EOControl
Framework.

## EOObjectStore Methods

EOObjectStoreCoordinator overrides the following EOObjectStore
methods:

- [- objectsWithFetchSpecification:editingContext:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#//apple_ref/occ/instm/EOObjectStore/objectsWithFetchSpecification:editingContext:)
- [- objectsForSourceGlobalID:relationshipName:editingContext:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#//apple_ref/occ/instm/EOObjectStore/objectsForSourceGlobalID:relationshipName:editingContext:)
- [- faultForGlobalID:editingContext:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#//apple_ref/occ/instm/EOObjectStore/faultForGlobalID:editingContext:)
- [- arrayFaultWithSourceGlobalID:relationshipName:editingContext:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#//apple_ref/occ/instm/EOObjectStore/arrayFaultWithSourceGlobalID:relationshipName:editingContext:)
- [- refaultObject:withGlobalID:editingContext:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#//apple_ref/occ/instm/EOObjectStore/refaultObject:withGlobalID:editingContext:)
- [- saveChangesInEditingContext:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#//apple_ref/occ/instm/EOObjectStore/saveChangesInEditingContext:)
- [- invalidateAllObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#//apple_ref/occ/instm/EOObjectStore/invalidateAllObjects)
- [- invalidateObjectsWithGlobalIDs:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#//apple_ref/occ/instm/EOObjectStore/invalidateObjectsWithGlobalIDs:)

With the exception of __saveChangesInEditingContext:__,
EOObjectStoreCoordinator's implementation of these methods simply
forwards the message to an EOCooperatingObjectStore or stores. The
message __invalidateAllObjects__ is forwarded
to all of a coordinator's cooperating stores. The rest of the
messages are forwarded to the appropriate store based on which store
responds YES to the messages [ownsGlobalID:](EOCooperatingObjectStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxazlsmzxxe3kdnbqw4z3fom), [ownsObject:](EOCooperatingObjectStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxw653oonhwe2tfmn2du), and [handlesFetchSpecification:](EOCooperatingObjectStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxwqylomrwgk42gmv2gg2ctobswg2lgnfrwc5djn5xdu) (which
message is used depends on the context). The EOObjectStore methods
listed above aren't documented in this class specification (except for __saveChangesInEditingContext:__)-for
descriptions of them, see the [EOObjectStore](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#EOObjectStore) and EODatabaseContext
(EOAccess) class specifications

For the method [saveChangesInEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixxgylwmvbwqylom5sxgsloivsgs5djnztug33oorsxq5b2),
the coordinator guides its cooperating stores through a multi-pass
save protocol in which each cooperating store saves its own changes
and forwards remaining changes to the other of the coordinator's
stores. For example, if in its [recordChangesInEditingContext](EOCooperatingObjectStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxezldn5zgiq3imfxgozltjfxekzdjoruw4z2dn5xhizlyoq) method
one cooperating store notices the removal of an object from an "owning"
relationship but that object belongs to another cooperating store,
it informs the other store by sending the coordinator a [forwardUpdateForObject:changes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixwm33so5qxezcvobsgc5dfizxxet3cnjswg5b2mnugc3thmvztu) message.
For a more details, see the method description for [saveChangesInEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixxgylwmvbwqylom5sxgsloivsgs5djnztug33oorsxq5b2).

Although it manages objects from multiple repositories, EOObjectStoreCoordinator
doesn't absolutely guarantee consistent updates when saving changes
across object stores. If your application requires guaranteed distributed
transactions, you can either provide your own solution by creating
a subclass of EOObjectStoreCoordinator that integrates with a TP
monitor, use a database server with built-in distributed transaction
support, or design your application to write to only one object
store per save operation (though it may read from multiple object
stores). For more discussion of this subject, see the method description
for __saveChangesInEditingContext:__.

## Constants

---

In EOObjectStoreCoordinator.h, EOControl defines NSString
constants for the notifications it posts. For more information,
see the section ["Notifications"](#apple-ijeugrcdivduk).

## Method Types

---

> **Initializing instances**
> : [- init](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixws3tjoq)
>
> **Setting the default coordinator**
> : [+ setDefaultCoordinator:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6ytkmvrxiu3un5zgkq3pn5zgi2lomf2g64rponsxirdfmzqxk3duinxw64tenfxgc5dpoi5a)
> : [+ defaultCoordinator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6ytkmvrxiu3un5zgkq3pn5zgi2lomf2g64rpmrswmylvnr2eg33pojsgs3tborxxe)
>
> **Managing EOCooperatingObjectStores**
> : [- addCooperatingObjectStore:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixwczdeinxw64dfojqxi2lom5hwe2tfmn2fg5dpojstu)
> : [- removeCooperatingObjectStore:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixxezlnn53gkq3pn5ygk4tboruw4z2pmjvgky3ukn2g64tfhi)
> : [- cooperatingObjectStores](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixwg33pobsxeylunfxgot3cnjswg5ctorxxezlt)
>
> **Saving changes**
> : [- saveChangesInEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixxgylwmvbwqylom5sxgsloivsgs5djnztug33oorsxq5b2)
>
> **Communication between
> EOCooperatingObjectStores**
> : [- forwardUpdateForObject:changes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixwm33so5qxezcvobsgc5dfizxxet3cnjswg5b2mnugc3thmvztu)
> : [- valuesForKeys:object:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixxmylmovsxgrtpojfwk6lthjxwe2tfmn2du)
>
> **Returning EOCooperatingObjectStores**
> : [- objectStoreForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixw6ytkmvrxiu3un5zgkrtpojdwy33cmfwesrb2)
> : [- objectStoreForFetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixw6ytkmvrxiu3un5zgkrtpojdgk5ddnbjxazldnftgsy3boruw63r2)
> : [- objectStoreForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixw6ytkmvrxiu3un5zgkrtpojhwe2tfmn2du)
>
> **Getting the userInfo
> dictionary**
> : [- userInfo](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixxk43fojew4ztp)
> : [- setUserInfo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixxgzlukvzwk4sjnztg6oq)

## Class Methods

---

### defaultCoordinator

`+ (id)defaultCoordinator`

Returns a shared instance of EOObjectStoreCoordinator.

---

### setDefaultCoordinator:

`+ (void)setDefaultCoordinator:(EOObjectStoreCoordinator
*)coordinator`

Sets a shared instance EOObjectStoreCoordinator.

---

## Instance Methods

---

### addCooperatingObjectStore:

`- (void)addCooperatingObjectStore:(EOCooperatingObjectStore
*)store`

Adds _store_ to
the list of EOCooperatingObjectStores that need to be queried and
notified about changes to enterprise objects. The receiver reuses
its stores: they don't go away until the EOObjectStoreCoordinator
is destroyed or until the stores are explicitly removed. Posts the
notification [EOCooperatingObjectStoreWasAdded](#apple-ijeugqsjivauo).

__See
Also:__  [- removeCooperatingObjectStore:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixxezlnn53gkq3pn5ygk4tboruw4z2pmjvgky3ukn2g64tfhi), [- cooperatingObjectStores](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixwg33pobsxeylunfxgot3cnjswg5ctorxxezlt)

---

### cooperatingObjectStores

`- (NSArray *)cooperatingObjectStores`

Returns the receiver's EOCooperatingObjectStores.

__See
Also:__  [- addCooperatingObjectStore:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixwczdeinxw64dfojqxi2lom5hwe2tfmn2fg5dpojstu), [- removeCooperatingObjectStore:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixxezlnn53gkq3pn5ygk4tboruw4z2pmjvgky3ukn2g64tfhi)

---

### forwardUpdateForObject:changes:

`- (void)forwardUpdateForObject:(id)object
changes:(NSDictionary *)changes`

Tells the receiver to forward a message from
an EOCooperatingObjectStore to another store, informing it that _changes_ need
to be made to _object_. For example,
inserting an object in a relationship property of one EOCooperatingObjectStore
might require changing a foreign key property in an object owned
by another EOCooperatingObjectStore.

This method first locates
the EOCooperatingObjectStore that's responsible for applying _changes_,
and then it sends the store the message [recordUpdateForObject:changes:](EOCooperatingObjectStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxezldn5zgivlqmrqxizkgn5ze6ytkmvrxiotdnbqw4z3fom5a).

---

### init

`- init`

Initializes a newly allocated EOObjectStoreCoordinator
and returns self_._ This is the designated initializer
for the EOObjectStoreCoordinator class.

---

### objectStoreForFetchSpecification:

`- (EOCooperatingObjectStore *)objectStoreForFetchSpecification:(EOFetchSpecification
*)fetchSpecification`

Returns the EOCooperatingObjectStore responsible
for fetching objects with _fetchSpecification_. Returns nil if
no EOCooperatingObjectStore can be found that responds YES to [handlesFetchSpecification:](EOCooperatingObjectStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxwqylomrwgk42gmv2gg2ctobswg2lgnfrwc5djn5xdu).

__See
Also:__  [- objectStoreForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixw6ytkmvrxiu3un5zgkrtpojdwy33cmfwesrb2), [- objectStoreForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixw6ytkmvrxiu3un5zgkrtpojhwe2tfmn2du)

---

### objectStoreForGlobalID:

`- (EOCooperatingObjectStore *)objectStoreForGlobalID:(EOGlobalID
*)globalID`

Returns the EOCooperatingObjectStore for the
object identified by _globalID_. Returns nil if
no EOCooperatingObjectStore can be found that responds YES to [ownsGlobalID:](EOCooperatingObjectStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxazlsmzxxe3kdnbqw4z3fom).

__See
Also:__  [- objectStoreForFetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixw6ytkmvrxiu3un5zgkrtpojdgk5ddnbjxazldnftgsy3boruw63r2), [- objectStoreForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixw6ytkmvrxiu3un5zgkrtpojhwe2tfmn2du)

---

### objectStoreForObject:

`- (EOCooperatingObjectStore *)objectStoreForObject:(id)object`

Returns the EOCooperatingObjectStore that owns _object_.
Returns nil if no EOCooperatingObjectStore can be found that responds YES to [ownsObject:](EOCooperatingObjectStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxw653oonhwe2tfmn2du).

__See
Also:__  [- objectStoreForFetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixw6ytkmvrxiu3un5zgkrtpojdgk5ddnbjxazldnftgsy3boruw63r2), [- objectStoreForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixw6ytkmvrxiu3un5zgkrtpojdwy33cmfwesrb2)

---

### removeCooperatingObjectStore:

`- (void)removeCooperatingObjectStore:(EOCooperatingObjectStore
*)store`

Removes _store_ from
the list of EOCooperatingObjectStores that need to be queried and
notified about changes to enterprise objects. Posts the notification [EOCooperatingObjectStoreWasRemoved](#apple-ijeugqsbjjauu).

__See
Also:__  [- addCooperatingObjectStore:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixwczdeinxw64dfojqxi2lom5hwe2tfmn2fg5dpojstu), [- cooperatingObjectStores](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixwg33pobsxeylunfxgot3cnjswg5ctorxxezlt)

---

### saveChangesInEditingContext:

`- (void)saveChangesInEditingContext:(EOEditingContext
*)anEditingContext`

Overrides the EOObjectStore implementation to
save the changes made in _anEditingContext_.
This message is sent by an EOEditingContext to an EOObjectStoreCoordinator
to commit changes. When an EOObjectStoreCoordinator receives this
message, it guides its EOCooperatingObjectStores through a multi-pass
save protocol in which each EOCooperatingObjectStore saves its own
changes and forwards remaining changes to other EOCooperatingObjectStores.
When this method is invoked, the following sequence of events occurs:

1. The receiver sends each of its EOCooperatingObjectStores the
   message [prepareForSaveWithCoordinator:editingContext:](EOCooperatingObjectStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxa4tfobqxezkgn5zfgylwmvlws5diinxw64tenfxgc5dpoi5gkzdjoruw4z2dn5xhizlyoq5a),
   which informs them that a multi-pass save operation is beginning.
   When the EOCooperatingObjectStore is an EODatabaseContext (EOAccess), it
   takes this opportunity to generate primary keys for any new objects
   in the EOEditingContext.
2. The receiver sends each of its EOCooperatingObjectStores the
   message [recordChangesInEditingContext](EOCooperatingObjectStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxezldn5zgiq3imfxgozltjfxekzdjoruw4z2dn5xhizlyoq),
   which prompts them to examine the changed objects in the editing context,
   record operations that need to be performed, and notify the receiver
   of any changes that need to be forwarded to other stores. For example,
   if in its __recordChangesInEditingContext__ method one
   EOCooperatingObjectStore notices the removal of an object from an
   "owning" relationship but that object belongs to another EOCooperatingObjectStore,
   it informs the other store by sending the coordinator a [forwardUpdateForObject:changes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixwm33so5qxezcvobsgc5dfizxxet3cnjswg5b2mnugc3thmvztu) message.
3. The receiver sends each of its EOCooperatingObjectStores the
   message [ownsGlobalID:](EOCooperatingObjectStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxazlsmzxxe3kdnbqw4z3fom). This tells the stores
   to transmit their changes to their underlying databases. When the
   EOCooperatingObjectStore is an EODatabaseContext, it responds to
   this message by taking the EODatabaseOperations (EOAccess) that
   were constructed in the previous step, constructing EOAdaptorOperations (EOAccess)
   from them, and giving the EOAdaptorOperations to an available EOAdaptorChannel (EOAccess)
   for execution.
4. If __ownsGlobalID:__ fails for any of
   the EOCooperatingObjectStores, all stores are sent the message [rollbackChanges](EOCooperatingObjectStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxe33mnrrgcy3linugc3thmvzq).
5. If __ownsGlobalID:__ succeeds for all
   EOCooperatingObjectStores, the receiver sends them the message [commitChanges](EOCooperatingObjectStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxwg33nnvuxiq3imfxgozlt), which has the effect
   of telling the adaptor to commit the changes.
6. If __commitChanges__ fails for a particular
   EOCooperatingObjectStore, that store and all subsequent ones are
   sent the message [rollbackChanges](EOCooperatingObjectStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5xxazlsmf2gs3thj5rguzldorjxi33smuxxe33mnrrgcy3linugc3thmvzq). However, the stores
   that have already committed their changes do not roll back. In other
   words, the coordinator doesn't perform the two-phase commit protocol
   necessary to guarantee consistent distributed update.

This
method raises an exception if an error occurs.

---

### setUserInfo:

`- (void)setUserInfo:(NSDictionary
*)dictionary`

Sets the _dictionary_ of
auxiliary data, which your application can use for whatever it needs.

__See
Also:__  [- userInfo](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixxk43fojew4ztp)

---

### userInfo

`- (NSDictionary *)userInfo`

Returns a dictionary of user data. Your application
can use this to store any auxiliary information it needs.

__See
Also:__  [- setUserInfo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixxgzlukvzwk4sjnztg6oq)

---

### valuesForKeys:object:

`- (NSDictionary *)valuesForKeys:(NSArray
*)keys
object:(id)object`

Communicates with the appropriate EOCooperatingObjectStore
to get the values identified by _keys_ for _object_,
so that it can then forward them on to another EOCooperatingObjectStore. EOCooperatingObjectStores
can hold values for an object that augment the properties in the
object. For instance, an EODatabaseContext (EOAccess) stores foreign
key information for the objects it owns. These foreign keys may
well not be defined as properties of the object. Other EODatabaseContexts
can find out the object's foreign keys by sending the EODatabaseContext
that owns the object a __valuesForKeys:object:__ message(through
the coordinator).

---

## Notifications

---

The following notifications are declared and posted by EOObjectStoreCoordinator.

### EOCooperatingObjectStoreWasAdded

`EOCONTROL_EXTERN NSString *EOCooperatingObjectStoreWasAdded`

When an EOObjectStoreCoordinator
receives an [addCooperatingObjectStore:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixwczdeinxw64dfojqxi2lom5hwe2tfmn2fg5dpojstu) message
and adds an EOCooperatingObjectStore to its list, it posts `EOCooperatingObjectStoreWasAdded` to
notify observers.

|  |  |
| --- | --- |
| Notification Object | The EOObjectStoreCoordinator |
| userInfo Dictionary | None |

### EOCooperatingObjectStoreWasRemoved

`EOCONTROL_EXTERN NSString *EOCooperatingObjectStoreWasRemoved`

When an EOObjectStoreCoordinator receives
a [removeCooperatingObjectStore:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjvgky3ukn2g64tfinxw64tenfxgc5dpoixxezlnn53gkq3pn5ygk4tboruw4z2pmjvgky3ukn2g64tfhi) message
and removes an EOCooperatingObjectStore from its list, it posts `EOCooperatingObjectStoreWasRemoved` to
notify observers.

|  |  |
| --- | --- |
| Notification Object | The EOObjectStoreCoordinator |
| userInfo Dictionary | None |

### EOCooperatingObjectStoreNeeded

`EOCONTROL_EXTERN NSString *EOCooperatingObjectStoreNeeded`

Posted when an EOObjectStoreCoordinator
receives a request that it can't service with any of its currently
registered EOCooperatingObjectStores. The observer can call back
to the coordinator to register an appropriate EOCooperatingObjectStore
based on the information in the userInfo dictionary.

**Notification Object**
: The EOObjectStoreCoordinator

**userInfo Dictionary**
: Contains the following keys and values:

|  |  |
| --- | --- |
| __Key__ | __Value__ |
| globalID | globalID for the operation |
| fetchSpecification | fetch specification for the operation |
| object | object for the operation |

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
