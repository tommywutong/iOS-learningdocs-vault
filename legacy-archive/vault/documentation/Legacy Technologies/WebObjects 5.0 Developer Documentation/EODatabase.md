---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EODatabase.html
archived_at: '2026-07-15T08:13:41.388184Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EODatabase

> __Inherits from:__ Object

> __Implements:__ NSDisposable

> __Package:__ com.webobjects.eoaccess

---

## Class Description

---

An EODatabase object represents a single database server. It contains an EOAdaptor which is capable of communicating with the server, a list of EOModels that describe the server's schema, a list of EODatabaseContexts that are connected to the server, and a set of snapshots representing the state of all objects stored in the server.

Each of an EODatabase's EODatabaseContexts forms a separate transaction scope, and is in effect a separate logical user to the server. An EODatabaseContext uses one or more pairs of EODatabaseChannel and EOAdaptorChannel objects to manage data operations (insert, update, delete, and fetch). Adaptors may support a limited number of contexts per database or channels per context, but an application is guaranteed at least one of each.

For more information on the EODatabase class, see the sections:

- ["The Database Level" (page 123)](EODatabase.Concepts.md#apple-iraukrceizcum)
- ["Snapshots" (page 125)](EODatabase.Concepts.md#apple-iraukrckinbue)

## Method Types

---

> Constructors
> [EODatabase](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl2fj5cgc5dbmjqxgzi)
>
> Adding and removing models
> [addModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3bmrse233emvwa)
> [addModelIfCompatible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3bmrse233emvweszsdn5wxaylunfrgyzi)
> [removeModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvww65tfjvxwizlm)
> [models](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3nn5sgk3dt)
>
> Accessing entities
> [entityForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3fnz2gs5dzizxxet3cnjswg5a)
> [entityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3fnz2gs5dzjzqw2zle)
>
> Recording snapshots
> [recordSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxirtpojdwy33cmfwesra)
> [recordSnapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyske)
> [recordSnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxi4y)
> [recordToManySnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64tekrxu2ylopfjw4ylqonug65dt)
>
> Forgetting snapshots
> [forgetSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3gn5zgozluknxgc4dtnbxxirtpojdwy33cmfwesra)
> [forgetSnapshotsForGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3gn5zgozluknxgc4dtnbxxi42gn5zeo3dpmjqwyskeom)
> [forgetAllSnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3gn5zgozluifwgyu3omfyhg2dporzq)
>
> Accessing snapshots and snapshot timestamps
> [snapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3tnzqxa43in52em33si5wg6ytbnreui)
> [snapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3tnzqxa43in52em33sknxxk4tdmvdwy33cmfwesra)
> [snapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3tnzqxa43in52hg)
> [timestampForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3unfwwk43umfwxartpojdwy33cmfwesra)
> [timestampForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3unfwwk43umfwxartpojjw65lsmnsuo3dpmjqwyske)
>
> Snapshot reference counting
> [incrementSnapshotCountForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3jnzrxezlnmvxhiu3omfyhg2dporbw65loordg64shnrxweylmjfca)
> [decrementSnapshotCountForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3emvrxezlnmvxhiu3omfyhg2dporbw65loordg64shnrxweylmjfca)
> [disableSnapshotRefcounting](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdborqweyltmuxwi2ltmfrgyzktnzqxa43in52fezlgmnxxk3tunfxgo)
>
> Registering database contexts
> [registerContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvtws43umvzeg33oorsxq5a)
> [unregisterContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3vnzzgkz3jon2gk4sdn5xhizlyoq)
> [registeredContexts](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvtws43umvzgkzcdn5xhizlyorzq)
>
> Accessing the adaptor
> [adaptor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3bmrqxa5dpoi)
>
> Managing the database connection
> [handleDroppedConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3imfxgi3dfirzg64dqmvseg33onzswg5djn5xa)
>
> Managing the result cache
> [invalidateResultCache](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3jnz3gc3djmrqxizksmvzxk3duinqwg2df)
> [invalidateResultCacheForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3jnz3gc3djmrqxizksmvzxk3duinqwg2dfizxxerlooruxi6komfwwkza)
> [resultCacheForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvzxk3duinqwg2dfizxxerlooruxi6komfwwkza)
> [setResultCache](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3tmv2fezltovwhiq3bmnugk)

## Constructors

---

### EODatabase

`public EODatabase(EOAdaptor anAdaptor)`

Creates and returns a new EODatabase object, specifying _anAdaptor_ as the new EODatabase's adaptor. Typically, you don't need to programmatically create EODatabase objects. Rather, they are created automatically by the control layer. See the class description for more information. If you do need to create an EODatabase programmatically, you should never associate more than one EODatabase with a given EOAdaptor. In general, create an EODatabase with an EOModel instead of an EOAdaptor.

`public EODatabase(EOModel aModel)`

Creates and returns a new EODatabase object, also creating an instance of the EOAdaptor named in _aModel_ and assigning that EOAdaptor object as the new EODatabase's adaptor.

Typically, you don't need to programmatically create EODatabase objects. Rather, they are created automatically by the control layer. See the class description for more information.

__See Also:__ [addModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3bmrse233emvwa), [adaptor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3bmrqxa5dpoi), adaptorName (EOModel)

---

## Static Methods

---

### disableSnapshotRefcounting

`public static void disableSnapshotRefCounting()`

Configures EODatabase instances not to release unreferenced snapshots.

---

## Instance Methods

---

### adaptor

`public EOAdaptor adaptor()`

Returns the EOAdaptor used by the receiver for communication with the database server. Your application can interact directly with the EOAdaptor, but should avoid altering its state (for example, by starting a transaction with one of its adaptor contexts).

__See Also:__ [EODatabase](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl2fj5cgc5dbmjqxgzi) constructors

---

### addModel

`public void addModel(EOModel aModel)`

Adds _aModel_ to the receiver's list of EOModels. This allows EODatabases to load entities and their properties only as they're needed, by dividing them among separate EOModels. _aModel_ must use the same EOAdaptor as the receiver and use the same connection dictionary as the receiver's other EOModels.

__See Also:__ [addModelIfCompatible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3bmrse233emvweszsdn5wxaylunfrgyzi), [models](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3nn5sgk3dt), [removeModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvww65tfjvxwizlm)

---

### addModelIfCompatible

`public boolean addModelIfCompatible(EOModel aModel)`

Adds _aModel_ to the receiver's list of EOModels, checking first to see whether it's compatible with those other EOModels. Returns `true` if _aModel_ is already in the list or if it's successfully added. Returns `false` if _aModel_'s adaptor name differs from that of the receivers or if the receiver's [adaptor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3bmrqxa5dpoi) returns `false` to a __canServiceModel__ message.

__See Also:__ [addModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3bmrse233emvwa), [models](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3nn5sgk3dt), [removeModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvww65tfjvxwizlm)

---

### decrementSnapshotCountForGlobalID

`public void decrementSnapshotCountForGlobalID(com.webobjects.eocontrol.EOGlobalID globalId)`

If the receiver releases unreferenced snapshots, decrements the reference count for the shared snapshot associated with _globalID_; and if no more objects refer to the snapshot, removes it from the snapshot table. (If the receiver doesn't release snapshots, this method does nothing.)

---

### dispose

`public void dispose()`

Conformance to NSDisposable.

---

### entityForObject

`public EOEntity entityForObject(EOEnterpriseObject anObject)`

Returns the EOEntity from one of the receiver's Models that's mapped to _anObject_, or `null` if there is no such EOEntity. This method works by sending __entityForObject:__ messages to each of the receiver's EOModels and returning the first one found.

__See Also:__ [entityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3fnz2gs5dzjzqw2zle)

---

### entityNamed

`public EOEntity entityNamed(String entityName)`

Returns the EOEntity from one of the receiver's Models that's named _entityName_, or `null` if there is no such EOEntity. This method works by sending __entityNamed:__ messages to each of the receiver's EOModels and returning the first one found.

__See Also:__ [entityForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3fnz2gs5dzizxxet3cnjswg5a)

---

### forgetAllSnapshots

`public void forgetAllSnapshots()`

Clears all of the receiver's snapshots and posts an `ObjectsChangedInStoreNotification` (defined in the EOControl framework's EOObjectStore class) describing the invalidated object. For a description of snapshots and their role in an application, see the class description.

__See Also:__ [forgetSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3gn5zgozluknxgc4dtnbxxirtpojdwy33cmfwesra), [forgetSnapshotsForGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3gn5zgozluknxgc4dtnbxxi42gn5zeo3dpmjqwyskeom), [recordSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxirtpojdwy33cmfwesra), [recordSnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxi4y), [recordSnapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyske), [recordToManySnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64tekrxu2ylopfjw4ylqonug65dt)

---

### forgetSnapshotForGlobalID

`public void forgetSnapshotForGlobalID(com.webobjects.eocontrol.EOGlobalID globalID)`

Clears the snapshot made for the enterprise object identified by _globalID_ and posts an `ObjectsChangedInStoreNotification` (defined in the EOControl framework's EOObjectStore class) describing the invalidated object. For a description of snapshots and their role in an application, see the class description.

__See Also:__ [forgetSnapshotsForGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3gn5zgozluknxgc4dtnbxxi42gn5zeo3dpmjqwyskeom), [forgetAllSnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3gn5zgozluifwgyu3omfyhg2dporzq), [recordSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxirtpojdwy33cmfwesra)

---

### forgetSnapshotsForGlobalIDs

`public void forgetSnapshotsForGlobalIDs(NSArray globalIDs)`

Clears the snapshots made for the enterprise objects identified by each of the EOGlobalIDs in _globalIDs_ and posts an ObjectsChangedInStoreNotification (defined in the EOControl framework's EOObjectStore class) describing the invalidated objects. For a description of snapshots and their role in an application, see the class description.

__See Also:__ [forgetSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3gn5zgozluknxgc4dtnbxxirtpojdwy33cmfwesra), [forgetAllSnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3gn5zgozluifwgyu3omfyhg2dporzq), [recordSnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxi4y)

---

### handleDroppedConnection

`public void handleDroppedConnection()`

Invoked to initiate clean up when the Framework detects a dropped database connection. The receiver cleans up by sending handleDroppedConnection to its adaptor, and then sending handleDroppedConnection to all of its registered database contexts. When the cleanup procedure is complete, the Framework can automatically reconnect to the database.

You should never invoke this method; it's invoked automatically by the Framework.

---

### incrementSnapshotCountForGlobalID

`public void incrementSnapshotCountForGlobalID(com.webobjects.eocontrol.EOGlobalID globalID)`

Increments the reference count for the shared snapshot associated with _globalID_ if the receiver releases unreferenced snapshots. (Does nothing if the receiver doesn't release snapshots.)

---

### invalidateResultCache

`public void invalidateResultCache()`

Invalidates the receiver's result cache. See the class description for more discussion of this topic.

__See Also:__ [invalidateResultCacheForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3jnz3gc3djmrqxizksmvzxk3duinqwg2dfizxxerlooruxi6komfwwkza), [resultCacheForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvzxk3duinqwg2dfizxxerlooruxi6komfwwkza)

---

### invalidateResultCacheForEntityNamed

`public void invalidateResultCacheForEntityNamed(String entityName)`

Invalidates the result cache containing an array of globalIDs for the objects associated with the entity _entityName_. See the class description for more discussion of this topic.

__See Also:__ [invalidateResultCache](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3jnz3gc3djmrqxizksmvzxk3duinqwg2df), [resultCacheForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvzxk3duinqwg2dfizxxerlooruxi6komfwwkza)

---

### models

`public NSArray models()`

Returns the receiver's EOModels.

__See Also:__ [EODatabase](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl2fj5cgc5dbmjqxgzi) constructor, [addModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3bmrse233emvwa), [addModelIfCompatible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3bmrse233emvweszsdn5wxaylunfrgyzi), [removeModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvww65tfjvxwizlm)

---

### recordSnapshotForGlobalID

`public void recordSnapshotForGlobalID( NSDictionary aSnapshot, com.webobjects.eocontrol.EOGlobalID globalID)`

Records _aSnapshot_ under _globalID_. For a description of snapshots and their role in an application, see the class description.

__See Also:__ globalIDForRow (EOEntity), [recordSnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxi4y), [forgetSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3gn5zgozluknxgc4dtnbxxirtpojdwy33cmfwesra)

---

### recordSnapshotForSourceGlobalID

`public void recordSnapshotForSourceGlobalID( NSArray globalIDs, com.webobjects.eocontrol.EOGlobalID globalID, String name)`

For the object identified by _globalID_, records an NSArray of _globalIDs_ for the to-many relationship named _name_. These _globalIDs_ identify the objects at the destination of the relationship. For a description of snapshots and their role in an application, see the class description.

__See Also:__ [recordSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxirtpojdwy33cmfwesra), [recordSnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxi4y), [recordSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxirtpojdwy33cmfwesra), [snapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3tnzqxa43in52em33sknxxk4tdmvdwy33cmfwesra)

---

### recordSnapshots

`public void recordSnapshots(NSDictionary snapshots)`

Records the snapshots in _snapshots_. _snapshots_ is a dictionary whose keys are EOGlobalIDs and whose values are the snapshots for those global IDs. For a description of snapshots and their role in an application, see the class description.

__See Also:__ [recordSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxirtpojdwy33cmfwesra), [forgetSnapshotsForGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3gn5zgozluknxgc4dtnbxxi42gn5zeo3dpmjqwyskeom)

---

### recordToManySnapshots

`public void recordToManySnapshots(NSDictionary snapshots)`

Records the objects in _snapshots_. _snapshots_ should be an NSDictionary of NSDictionaries, in which the top-level dictionary has as its key the globaID of the enterprise object for which to-many relationships are being recorded. The key's value is a dictionary whose keys are the names of the enterprise object's to-many relationships. Each of these keys in turn has as its value an array of globalIDs that identify the objects at the destination of the relationship. For a description of snapshots and their role in an application, see the class description.

__See Also:__ [recordSnapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyske), [recordSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxirtpojdwy33cmfwesra), [snapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3tnzqxa43in52em33sknxxk4tdmvdwy33cmfwesra)

---

### registerContext

`public void registerContext(EODatabaseContext aContext)`

Records _aContext_ as one of the receiver's EODatabaseContexts. The receiver must have been specified as aContext's EODatabase in the EODatabaseContext constructor (which invokes this method automatically). You should never need to invoke this method directly.

__See Also:__ [unregisterContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3vnzzgkz3jon2gk4sdn5xhizlyoq), [registeredContexts](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvtws43umvzgkzcdn5xhizlyorzq)

---

### registeredContexts

`public NSArray registeredContexts()`

Returns all the EODatabaseContexts that have been registered with the receiver, generally all the database contexts that were created with the receiver as their EODatabase object.

__See Also:__ [registerContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvtws43umvzeg33oorsxq5a), [unregisterContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3vnzzgkz3jon2gk4sdn5xhizlyoq)

---

### removeModel

`public void removeModel(EOModel aModel)`

Removes _aModel_ from the receiver's list of EOModels. Throws an exception if _aModel_ isn't one of the receiver's models.

__See Also:__ [addModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3bmrse233emvwa), [addModelIfCompatible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3bmrse233emvweszsdn5wxaylunfrgyzi), [models](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3nn5sgk3dt)

---

### resultCacheForEntityNamed

`public NSArray resultCacheForEntityNamed(String entityName)`

Returns an array containing the globalIDs of the objects associated with _entityName_. See the class description for more discussion of this topic.

__See Also:__ [invalidateResultCache](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3jnz3gc3djmrqxizksmvzxk3duinqwg2df), [invalidateResultCacheForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3jnz3gc3djmrqxizksmvzxk3duinqwg2dfizxxerlooruxi6komfwwkza)

---

### setResultCache

`public void setResultCache( NSArray cache, String entityName)`

Updates the receiver's cache for _entityName_ with _cache_, an array of EOGlobalID objects, for all the enterprise objects associated with the EOEntity named _entityName_. This method is invoked automatically, and you should never need to invoke it directly. For more information on this topic, see the class description.

__See Also:__ [invalidateResultCache](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3jnz3gc3djmrqxizksmvzxk3duinqwg2df), [invalidateResultCacheForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3jnz3gc3djmrqxizksmvzxk3duinqwg2dfizxxerlooruxi6komfwwkza), [resultCacheForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvzxk3duinqwg2dfizxxerlooruxi6komfwwkza)

---

### setTimestampToNow

`public void setTimestampToNow()`

Sets the internal timestamp to the value returned by NSDate's __timeIntervalSinceReferenceDate__ method. Used for recording subsequent snapshots.

---

### snapshotForGlobalID

`public NSDictionary snapshotForGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, long timestamp)`

`public NSDictionary snapshotForGlobalID(com.webobjects.eocontrol.EOGlobalID globalID)`

Returns the snapshot associated with _globalID_. Returns `null` if there isn't a snapshot for the globalID or if the corresponding timestamp is less than timestamp. For a description of snapshots and their role in an application, see the class description.

__See Also:__ [recordSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxirtpojdwy33cmfwesra), [forgetSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3gn5zgozluknxgc4dtnbxxirtpojdwy33cmfwesra)

---

### snapshotForSourceGlobalID

`public NSArray snapshotForSourceGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, String name, long timestamp)`

`public NSArray snapshotForSourceGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, String name)`

Returns the to-many snapshot for _globalId_ and _name_. A to-many snapshot is an array of globalIDs. These globalIDs identify the objects at the destination of the to-many relationship named _name_, which is a property of the object identified by _globalID._ Returns `null` if there isn't a to-many snapshot for _globalId_ or if the timestamp is less than timestamp. For a description of snapshots and their role in an application, see the class description.

---

### snapshots

`public NSDictionary snapshots()`

Returns all of the receiver's snapshots, stored in a dictionary under their EOGlobalIDs.

__See Also:__ [recordSnapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64teknxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyske), [recordToManySnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvrw64tekrxu2ylopfjw4ylqonug65dt)

---

### timestampForGlobalID

`public long timestampForGlobalID(com.webobjects.eocontrol.EOGlobalID globalId)`

Returns the timestamp of the snapshot for _globalID_. Returns `EODistantPastTimeInterval` if there isn't a snapshot.

---

### timestampForSourceGlobalID

`public long timestampForSourceGlobalID( com.webobjects.eocontrol.EOGlobalID globalId, String relationshipName)`

Returns the timestamp of the to-many snapshot for the relationship specified by _relationshipName_ and the object specified by _globalID_. Returns `EODistantPastTimeInterval` if there isn't a snapshot.

---

### unregisterContext

`public void unregisterContext(EODatabaseContext aContext)`

Removes _aContext_ as one of the receiver's EODatabaseContexts. An EODatabaseContext automatically invokes this method when it's finalized; you should never need to invoke it directly.

__See Also:__ [registerContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvtws43umvzeg33oorsxq5a), [registeredContexts](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkl3smvtws43umvzgkzcdn5xhizlyorzq)

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
