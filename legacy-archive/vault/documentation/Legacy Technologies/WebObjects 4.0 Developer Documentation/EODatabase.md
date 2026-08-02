---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EODatabase.html
archived_at: '2026-07-18T01:28:09.187102Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](SQL%20Statement%20Formats.md)
[!](EODatabase-2.md)

---

# EODatabase

__Inherits From:__

__Inherits From:__
com.apple.yellow.eoaccess

---

## Class Description

An EODatabase object represents a single database server. It contains an EOAdaptor which is capable of communicating with the server, a list of EOModels that describe the server's schema, a list of EODatabaseContexts that are connected to the server, and a set of snapshots representing the state of all objects stored in the server.

For more information, see ["More about EODatabase"](EODatabase-2.md).

---

## Method Types

**Constructors**

**[EODatabase](#apple-he4dsmq)**

**Adding and removing models**

**[addModel](#apple-gm2dimy)

**[addModelIfCompatible](#apple-gm2tsoi)

**[removeModel](#apple-gq3tc)

**[models](#apple-gi3dmmi)********

**Accessing entities**

**[entityForObject](#apple-gmydcoa)

**[entityNamed](#apple-gmydgmi)****

**Recording snapshots**

**[recordSnapshot:forGlobalID:](#apple-gq4tioi)

**[forgetSnapshotForGlobalID](#apple-gqztm)

**[forgetSnapshotsForGlobalIDs](#apple-gq2da)

**[recordSnapshots](#apple-gq2ts)

**[forgetAllSnapshots](#apple-gqzte)

**[snapshotForGlobalID](#apple-gq3tk)

**[snapshots](#apple-gi3danq)

**recordSnapshotForSourceGlobalIDpublic void
recordSnapshotForSourceGlobalID(NSArray globalIDs,
com.apple.yellow.eocontrol.EOGlobalID globalID,
java.lang.String name)

**void
recordToManySnapshots(NSDictionary snapshots)

**snapshotForSourceGlobalIDpublic NSArray
snapshotForSourceGlobalID(
com.apple.yellow.eocontrol.EOGlobalID globalID,
java.lang.String name)********************

**Registering database contexts**

**[registerContext](#apple-gq3dg)

**[unregisterContext](#apple-gq4de)

**[registeredContexts](#apple-gi3dgnq)******

**Accessing the adaptor**

**[adaptor](#apple-gqytg)**

**Managing the result cache**

**[invalidateResultCache](#apple-gm3tm)

**[invalidateResultCacheForEntityNamed](#apple-gq4tm)

**[resultCacheForEntityNamed](#apple-guyda)

**[setResultCacheForEntityWithName](#apple-ha4tqnq)********

---

## Constructors

---

### EODatabase

public `next.eo.EODatabase`(EOAdaptor _anAdaptor_)

public `next.eo.EODatabase`(EOModel _aModel_)

Creates and returns a new EODatabase object. If _anAdaptor_ is provided, it specifies the new EODatabase's adaptor. If _aModel_ is provided, the constructor creates an instance of the EOAdaptor named in _aModel_ and assigns that EOAdaptor object as the new EODatabase's adaptor.

Typically, you don't need to programmatically create EODatabase objects. Rather, they are created automatically by the control layer. See the class description for more information. If you do need to create an EODatabase programmatically, you should never associate more than one EODatabase with a given EOAdaptor. In general, provide _aModel_ instead of _anAdaptor_, which automatically selects the adaptor.

__See also:__
[`addModel`](#apple-gm2dimy), [`adaptor`](#apple-gqytg)
, [`adaptorName`](EOModel.md#apple-gqytc) (EOModel)

---

## Instance Methods

---

### adaptor

public EOAdaptor `adaptor`()

Returns the EOAdaptor used by the receiver for communication with the database server. Your application can interact directly with the EOAdaptor, but should avoid altering its state (for example, by starting a transaction with one of its adaptor contexts).

__See also:__
["Constructors"](#apple-he4dsma)

---

### addModel

public void `addModel`(EOModel _aModel_)

Adds _aModel_ to the receiver's list of EOModels. This allows EODatabases to load entities and their properties only as they're needed, by dividing them among separate EOModels. _aModel_ must use the same EOAdaptor as the receiver and use the same connection dictionary as the receiver's other EOModels.

__See also:__
[`addModelIfCompatible`](#apple-gm2tsoi), [`models`](#apple-gi3dmmi), [`removeModel`](#apple-gq3tc)

---

### addModelIfCompatible

public boolean `addModelIfCompatible`(EOModel _aModel_)

Adds _aModel_ to the receiver's list of EOModels, checking first to see whether it's compatible with those other EOModels. Returns `true` if _aModel_ is already in the list or if it's successfully added. Returns `false` if _aModel_'s adaptor name differs from that of the receivers or if the receiver's [`adaptor`](#apple-gqytg) returns `false` to a `canServiceModel:` message.

__See also:__
[`addModel`](#apple-gm2dimy), [`models`](#apple-gi3dmmi), [`removeModel`](#apple-gq3tc)

---

### entityForObject

public EOEntity `entityForObject`(java.lang.Object _anObject_)

Returns the EOEntity from one of the receiver's Models that's mapped to _anObject_, or `null` if there is no such EOEntity. This method works by sending `entityForObject:` messages to each of the receiver's EOModels and returning the first one found.

__See also:__
[`entityNamed`](#apple-gmydgmi)

---

### entityNamed

public EOEntity `entityNamed`(java.lang.String _entityName_)

Returns the EOEntity from one of the receiver's Models that's named _entityName_, or `null` if there is no such EOEntity. This method works by sending `entityNamed:` messages to each of the receiver's EOModels and returning the first one found.

__See also:__
[`entityForObject`](#apple-gmydcoa)

---

### forgetAllSnapshots

public void `forgetAllSnapshots`

Clears all of the receiver's snapshots and posts an ObjectsChangedInStoreNotification (defined in the EOControl framework's EOObjectStore class) describing the invalidated object. For a description of snapshots and their role in an application, see the class description.

__See also:__
[`forgetSnapshotForGlobalID`](#apple-gqztm), [`forgetSnapshotsForGlobalIDs`](#apple-gq2da), [`recordSnapshot:forGlobalID:`](#apple-gq4tioi),
[`recordSnapshots`](#apple-gq2ts), `recordSnapshotForSourceGlobalIDpublic void
recordSnapshotForSourceGlobalID(NSArray globalIDs,
com.apple.yellow.eocontrol.EOGlobalID globalID, java.lang.String name)`,
`recordToManySnapshotspublic void recordToManySnapshots(NSDictionary snapshots)`

---

### forgetSnapshotForGlobalID

public void `forgetSnapshotForGlobalID`(com.apple.yellow.eocontrol.EOGlobalID _globalID_)

Clears the snapshot made for the enterprise object identified by _globalID_ and posts an ObjectsChangedInStoreNotification (defined in the EOControl framework's EOObjectStore class) describing the invalidated object. For a description of snapshots and their role in an application, see the class description.

__See also:__
[`forgetSnapshotsForGlobalIDs`](#apple-gq2da), [`forgetAllSnapshots`](#apple-gqzte), [`recordSnapshot:forGlobalID:`](#apple-gq4tioi)

---

### forgetSnapshotsForGlobalIDs

public void `forgetSnapshotsForGlobalIDs`(NSArray _globalIDs_)

Clears the snapshots made for the enterprise objects identified by each of the EOGlobalIDs in _globalIDs_ and posts an ObjectsChangedInStoreNotification (defined in the EOControl framework's EOObjectStore class) describing the invalidated objects. For a description of snapshots and their role in an application, see the class description.

__See also:__
[`forgetSnapshotForGlobalID`](#apple-gqztm), [`forgetAllSnapshots`](#apple-gqzte), [`recordSnapshots`](#apple-gq2ts)

---

### invalidateResultCache

public void `invalidateResultCache`

Invalidates the receiver's result cache. See the class description for more discussion of this topic.

__See also:__
[`invalidateResultCacheForEntityNamed`](#apple-gq4tm), [`resultCacheForEntityNamed`](#apple-guyda)

---

### invalidateResultCacheForEntityNamed

public void `invalidateResultCacheForEntityNamed`(java.lang.String _entityName_)

Invalidates the result cache containing an array of globalIDs for the objects associated with the entity _entityName_. See the class description for more discussion of this topic.

__See also:__
[`invalidateResultCache`](#apple-gm3tm), [`resultCacheForEntityNamed`](#apple-guyda)

---

### models

public NSArray `models`()

Returns the receiver's EOModels.

__See also:__
["Constructors"](#apple-he4dsma), [`addModel`](#apple-gm2dimy), [`addModelIfCompatible`](#apple-gm2tsoi), [`removeModel`](#apple-gq3tc)

---

### recordSnapshot:forGlobalID:

public void `recordSnapshotForGlobalID`(NSDictionary _aSnapshot_, com.apple.yellow.eocontrol.EOGlobalID _globalID_)

Records _aSnapshot_ under _globalID_. For a description of snapshots and their role in an application, see the class description.

__See also:__
- `globalIDForRow:` (EOEntity), [`recordSnapshots`](#apple-gq2ts), [`forgetSnapshotForGlobalID`](#apple-gqztm)

__recordSnapshotForSourceGlobalID__ public void `recordSnapshotForSourceGlobalID`(NSArray _globalIDs_,
com.apple.yellow.eocontrol.EOGlobalID _globalID_,
java.lang.String _name_)

For the object identified by _globalID_, records an NSArray of _globalIDs_ for the to-many relationship named _name_. These _globalIDs_ identify the objects at the destination of the relationship. For a description of snapshots and their role in an application, see the class description.

__See also:__
[`recordSnapshot:forGlobalID:`](#apple-gq4tioi), [`recordSnapshots`](#apple-gq2ts), [`recordSnapshot:forGlobalID:`](#apple-gq4tioi),
`snapshotForSourceGlobalIDpublic NSArray snapshotForSourceGlobalID(
com.apple.yellow.eocontrol.EOGlobalID globalID, java.lang.String name)`

---

### recordSnapshots

public void `recordSnapshots`(NSDictionary _snapshots_)

Records the snapshots in _snapshots_. _snapshots_ is a dictionary whose keys are EOGlobalIDs and whose values are the snapshots for those global IDs. For a description of snapshots and their role in an application, see the class description.

__See also:__
[`recordSnapshot:forGlobalID:`](#apple-gq4tioi), [`forgetSnapshotsForGlobalIDs`](#apple-gq2da)

__recordToManySnapshots__ public void `recordToManySnapshots`(NSDictionary _snapshots_)

Records the objects in _snapshots_. _snapshots_ should be an NSDictionary of NSDictionaries, in which the top-level dictionary has as its key the globaID of the enterprise object for which to-many relationships are being recorded. The key's value is a dictionary whose keys are the names of the enterprise object's to-many relationships. Each of these keys in turn has as its value an array of globalIDs that identify the objects at the destination of the relationship. For a description of snapshots and their role in an application, see the class description.

__See also:__
`recordSnapshotForSourceGlobalIDpublic void
recordSnapshotForSourceGlobalID(NSArray globalIDs,
com.apple.yellow.eocontrol.EOGlobalID globalID, java.lang.String name)`, [`recordSnapshot:
forGlobalID:`](#apple-gq4tioi), `snapshotForSourceGlobalIDpublic NSArray snapshotForSourceGlobalID(
com.apple.yellow.eocontrol.EOGlobalID globalID, java.lang.String name)`

---

### registerContext

public void `registerContext`(EODatabaseContext _aContext_)

Records _aContext_ as one of the receiver's EODatabaseContexts. The receiver must have been specified as _aContext_'s EODatabase in the EODatabaseContext constructor (which invokes this method automatically). You should never need to invoke this method directly.

__See also:__
[`unregisterContext`](#apple-gq4de), [`registeredContexts`](#apple-gi3dgnq)

---

### registeredContexts

public NSArray `registeredContexts`()

Returns all the EODatabaseContexts that have been registered with the receiver, generally all the database contexts that were created with the receiver as their EODatabase object.

__See also:__
[`registerContext`](#apple-gq3dg), [`unregisterContext`](#apple-gq4de)

---

### removeModel

public void `removeModel`(EOModel _aModel_)

Removes _aModel_ from the receiver's list of EOModels. Throws an exception if _aModel_ isn't one of the receiver's models.

__See also:__
[`addModel`](#apple-gm2dimy), [`addModelIfCompatible`](#apple-gm2tsoi), [`models`](#apple-gi3dmmi)

---

### resultCacheForEntityNamed

public NSArray `resultCacheForEntityNamed`(java.lang.String _entityName_)

Returns an array containing the globalIDs of the objects associated with _entityName_. See the class description for more discussion of this topic.

__See also:__
[`invalidateResultCache`](#apple-gm3tm), [`invalidateResultCacheForEntityNamed`](#apple-gq4tm)

---

### setResultCacheForEntityWithName

public void `setResultCacheForEntityWithName`(NSArray _cache_, java.lang.String _entityName_)

Updates the receiver's cache for _entityName_ with _cache_, an array of EOGlobalID objects, for all the enterprise objects associated with the EOEntity named _entityName_. This method is invoked automatically, and you should never need to invoke it directly. For more information on this topic, see the class description.

__See also:__
[`invalidateResultCache`](#apple-gm3tm), [`invalidateResultCacheForEntityNamed`](#apple-gq4tm),
[`resultCacheForEntityNamed`](#apple-guyda)

---

### snapshotForGlobalID

public NSDictionary `snapshotForGlobalID`(com.apple.yellow.eocontrol.EOGlobalID _globalID_)

Returns the snapshot associated with _globalID_ if there is one; otherwise returns `null`. For a description of snapshots and their role in an application, see the class description.

__See also:__
[`recordSnapshot:forGlobalID:`](#apple-gq4tioi), [`forgetSnapshotForGlobalID`](#apple-gqztm)

__snapshotForSourceGlobalID__ public NSArray `snapshotForSourceGlobalID`(
com.apple.yellow.eocontrol.EOGlobalID _globalID_,
java.lang.String _name_)

Returns a snapshot that consists of an array of globalIDs. These globalIDs identify the objects at the destination of the to-many relationship named _name_, which is a property of the object identified by _globalID_. If there is no snapshot, returns `null`. For a description of snapshots and their role in an application, see the class description.

---

### snapshots

public NSDictionary `snapshots`()

Returns all of the receiver's snapshots, stored in a dictionary under their EOGlobalIDs.

__See also:__
`recordSnapshotForSourceGlobalIDpublic void
recordSnapshotForSourceGlobalID(NSArray globalIDs,
com.apple.yellow.eocontrol.EOGlobalID globalID, java.lang.String name)`,
`recordToManySnapshotspublic void recordToManySnapshots(NSDictionary snapshots)`

---

### unregisterContext

public void `unregisterContext`(EODatabaseContext _aContext_)

Removes _aContext_ as one of the receiver's EODatabaseContexts. An EODatabaseContext automatically invokes this method when it's finalized; you should never need to invoke it directly.

__See also:__
[`registerContext`](#apple-gq3dg), [`registeredContexts`](#apple-gi3dgnq)

---

### 

---

[!](SQL%20Statement%20Formats.md)
[!](EODatabase-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
