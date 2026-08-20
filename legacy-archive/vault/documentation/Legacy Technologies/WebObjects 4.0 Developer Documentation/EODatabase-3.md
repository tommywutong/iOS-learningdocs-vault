---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EODatabase.html
archived_at: '2026-07-18T01:28:15.902134Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](SQL%20Statement%20Formats-2.md)
[!](More%20about%20EODatabase.md)

---

# EODatabase

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
EOAccess/EODatabase.h

---

## Class Description

An EODatabase object represents a single database server. It contains an EOAdaptor which is capable of communicating with the server, a list of EOModels that describe the server's schema, a list of EODatabaseContexts that are connected to the server, and a set of snapshots representing the state of all objects stored in the server.

For more information, see ["More about EODatabase"](More%20about%20EODatabase.md).

---

## Method Types

**Creating instances [- initWithModel:](#apple-ha3dqmy)**

**[- initWithAdaptor:](#apple-ha3domy)**

**Adding and removing models**

**[- addModel:](#apple-gm2dimy)

**[- addModelIfCompatible:](#apple-gm2tsoi)

**[- removeModel:](#apple-gq3tc)

**[- models](#apple-gi3dmmi)********

**Accessing entities**

**[- entityForObject:](#apple-gmydcoa)

**[- entityNamed:](#apple-gmydgmi)****

**Recording snapshots**

**[- recordSnapshot:forGlobalID:](#apple-gq4tioi)

**[- forgetSnapshotForGlobalID:](#apple-gqztm)

**[- forgetSnapshotsForGlobalIDs:](#apple-gq2da)

**[- recordSnapshots:](#apple-gq2ts)

**[- forgetAllSnapshots](#apple-gqzte)

**[- snapshotForGlobalID:](#apple-gq3tk)

**[- snapshots](#apple-gi3danq)

**[- recordSnapshot:forSourceGlobalID:relationshipName:](#apple-ha3tsnq)

**[- recordToManySnapshots:](#apple-ha4dima)

**[- snapshotForSourceGlobalID:relationshipName:](#apple-heydmni)********************

**Registering database contexts**

**[- registerContext:](#apple-gq3dg)

**[- unregisterContext:](#apple-gq4de)

**[- registeredContexts](#apple-gi3dgnq)******

**Accessing the adaptor**

**[- adaptor](#apple-gqytg)**

**Managing the result cache**

**[- invalidateResultCache](#apple-gm3tm)

**[- invalidateResultCacheForEntityNamed:](#apple-gq4tm)

**[- resultCacheForEntityNamed:](#apple-guyda)

**[- setResultCache:forEntityNamed:](#apple-ha4tqnq)********

---

## Instance Methods

---

### adaptor

- (EOAdaptor \*)`adaptor`

Returns the EOAdaptor used by the receiver for communication with the database server. Your application can interact directly with the EOAdaptor, but should avoid altering its state (for example, by starting a transaction with one of its adaptor contexts).

---

### addModel:

- (void)`addModel:`(EOModel \*)_aModel_

Adds _aModel_ to the receiver's list of EOModels. This allows EODatabases to load entities and their properties only as they're needed, by dividing them among separate EOModels. _aModel_ must use the same EOAdaptor as the receiver and use the same connection dictionary as the receiver's other EOModels.

__See also:__
[- `addModelIfCompatible:`](#apple-gm2tsoi), [- `models`](#apple-gi3dmmi), [- `removeModel:`](#apple-gq3tc)

---

### addModelIfCompatible:

- (BOOL)`addModelIfCompatible:`(EOModel \*)_aModel_

Adds _aModel_ to the receiver's list of EOModels, checking first to see whether it's compatible with those other EOModels. Returns YES if _aModel_ is already in the list or if it's successfully added. Returns NO if _aModel_'s adaptor name differs from that of the receivers or if the receiver's [`adaptor`](#apple-gqytg) returns NO to a `canServiceModel:` message.

__See also:__
[- `addModel:`](#apple-gm2dimy), [- `models`](#apple-gi3dmmi), [- `removeModel:`](#apple-gq3tc)

---

### entityForObject:

- (EOEntity \*)`entityForObject:`(id)_anObject_

Returns the EOEntity from one of the receiver's Models that's mapped to _anObject_, or `nil` if there is no such EOEntity. This method works by sending `entityForObject:` messages to each of the receiver's EOModels and returning the first one found.

__See also:__
[- `entityNamed:`](#apple-gmydgmi)

---

### entityNamed:

- (EOEntity \*)`entityNamed:`(NSString \*)_entityName_

Returns the EOEntity from one of the receiver's Models that's named _entityName_, or `nil` if there is no such EOEntity. This method works by sending `entityNamed:` messages to each of the receiver's EOModels and returning the first one found.

__See also:__
[- `entityForObject:`](#apple-gmydcoa)

---

### forgetAllSnapshots

- (void)`forgetAllSnapshots`

Clears all of the receiver's snapshots and posts an EOObjectsChangedInStoreNotification (defined in the EOControl framework's EOObjectStore class) describing the invalidated object. For a description of snapshots and their role in an application, see the class description.

__See also:__
[- `forgetSnapshotForGlobalID:`](#apple-gqztm), [- `forgetSnapshotsForGlobalIDs:`](#apple-gq2da), [- `recordSnapshot:
forGlobalID:`](#apple-gq4tioi), [- `recordSnapshots:`](#apple-gq2ts), [- `recordSnapshot:forSourceGlobalID:relationshipName:`](#apple-ha3tsnq)
, [- `recordToManySnapshots:`](#apple-ha4dima)

---

### forgetSnapshotForGlobalID:

- (void)`forgetSnapshotForGlobalID:`(EOGlobalID \*)_globalID_

Clears the snapshot made for the enterprise object identified by _globalID_ and posts an EOObjectsChangedInStoreNotification (defined in the EOControl framework's EOObjectStore class) describing the invalidated object. For a description of snapshots and their role in an application, see the class description.

__See also:__
[- `forgetSnapshotsForGlobalIDs:`](#apple-gq2da), [- `forgetAllSnapshots`](#apple-gqzte), [- `recordSnapshot:forGlobalID:`](#apple-gq4tioi)

---

### forgetSnapshotsForGlobalIDs:

- (void)`forgetSnapshotsForGlobalIDs:`(NSArray \*)_globalIDs_

Clears the snapshots made for the enterprise objects identified by each of the EOGlobalIDs in _globalIDs_ and posts an EOObjectsChangedInStoreNotification (defined in the EOControl framework's EOObjectStore class) describing the invalidated objects. For a description of snapshots and their role in an application, see the class description.

__See also:__
[- `forgetSnapshotForGlobalID:`](#apple-gqztm), [- `forgetAllSnapshots`](#apple-gqzte), [- `recordSnapshots:`](#apple-gq2ts)

---

### initWithAdaptor:

- `initWithAdaptor:`(EOAdaptor \*)_anAdaptor_

The designated initializer, this method initializes a newly allocated EODatabase with _anAdaptor_ as its adaptor and returns `self`.

Typically, you don't need to programmatically create EODatabase objects. Rather, they are created automatically by the control layer. See the class description for more information. If you do need to create an EODatabase programmatically, you should never associate more than one EODatabase with a given EOAdaptor. In general, use `[initWithModel:](#apple-ha3dqmy)`, which automatically selects the adaptor.

---

### initWithModel:

- `initWithModel:`(EOModel \*)_aModel_

Initializes a newly allocated EODatabase by creating an instance of EOAdaptor named in _aModel_ and invoking `[initWithAdaptor:](#apple-ha3domy)`. Returns `self`. Typically, you don't need to programmatically create EODatabase objects. Rather, they are created automatically by the control layer. See the class description for more information.

__See also:__
+ `adaptorWithModel:` (EOAdaptor), - `adaptorName` (EOModel)

---

### invalidateResultCache

- (void)`invalidateResultCache`

Invalidates the receiver's result cache. See the class description for more discussion of this topic.

__See also:__
[- `invalidateResultCacheForEntityNamed:`](#apple-gq4tm), [- `resultCacheForEntityNamed:`](#apple-guyda)

---

### invalidateResultCacheForEntityNamed:

- (void)`invalidateResultCacheForEntityNamed:`(NSString \*)_entityName_

Invalidates the result cache containing an array of globalIDs for the objects associated with the entity _entityName_. See the class description for more discussion of this topic.

__See also:__
[- `invalidateResultCache`](#apple-gm3tm), [- `resultCacheForEntityNamed:`](#apple-guyda)

---

### models

- (NSArray \*)`models`

Returns the receiver's EOModels.

__See also:__
[- `initWithModel:`](#apple-ha3dqmy), [- `addModel:`](#apple-gm2dimy), [- `addModelIfCompatible:`](#apple-gm2tsoi), [- `removeModel:`](#apple-gq3tc)

---

### recordSnapshot:forGlobalID:

- (void)`recordSnapshot:`(NSDictionary \*)_aSnapshot_ `forGlobalID:`(EOGlobalID \*)_globalID_

Records _aSnapshot_ under _globalID_. For a description of snapshots and their role in an application, see the class description.

__See also:__
- `globalIDForRow:` (EOEntity), [- `recordSnapshots:`](#apple-gq2ts), [- `forgetSnapshotForGlobalID:`](#apple-gqztm)

---

### recordSnapshot:forSourceGlobalID:relationshipName:

- (void)`recordSnapshot:`(NSArray \*)_globalIDs_
`forSourceGlobalID:`(EOGlobalID \*)_globalID_
`relationshipName:`(NSString \*)_name_

For the object identified by _globalID_, records an NSArray of _globalIDs_ for the to-many relationship named _name_. These _globalIDs_ identify the objects at the destination of the relationship. For a description of snapshots and their role in an application, see the class description.

__See also:__
[- `recordSnapshot:forGlobalID:`](#apple-gq4tioi), [- `recordSnapshots:`](#apple-gq2ts), [- `recordSnapshot:forGlobalID:`](#apple-gq4tioi),
[- `snapshotForSourceGlobalID:relationshipName:`](#apple-heydmni)

---

### recordSnapshots:

- (void)`recordSnapshots:`(NSDictionary \*)_snapshots_

Records the snapshots in _snapshots_. _snapshots_ is a dictionary whose keys are EOGlobalIDs and whose values are the snapshots for those global IDs. For a description of snapshots and their role in an application, see the class description.

__See also:__
[- `recordSnapshot:forGlobalID:`](#apple-gq4tioi), [- `forgetSnapshotsForGlobalIDs:`](#apple-gq2da)

---

### recordToManySnapshots:

- (void)`recordToManySnapshots:`(NSDictionary \*)_snapshots_

Records the objects in _snapshots_. _snapshots_ should be an NSDictionary of NSDictionaries, in which the top-level dictionary has as its key the globaID of the enterprise object for which to-many relationships are being recorded. The key's value is a dictionary whose keys are the names of the enterprise object's to-many relationships. Each of these keys in turn has as its value an array of globalIDs that identify the objects at the destination of the relationship. For a description of snapshots and their role in an application, see the class description.

__See also:__
[- `recordSnapshot:forSourceGlobalID:relationshipName:`](#apple-ha3tsnq), [- `recordSnapshot:forGlobalID:`](#apple-gq4tioi),
[- `snapshotForSourceGlobalID:relationshipName:`](#apple-heydmni)

---

### registerContext:

- (void)`registerContext:`(EODatabaseContext \*)_aContext_

Records _aContext_ as one of the receiver's EODatabaseContexts, without retaining it. . _aContext_ must have been created with the receiver using EODatabaseContext's `initWithDatabase:` method, which invokes this method automatically. You should never need to invoke this method directly.

__See also:__
[- `unregisterContext:`](#apple-gq4de), [- `registeredContexts`](#apple-gi3dgnq)

---

### registeredContexts

- (NSArray \*)`registeredContexts`

Returns all the EODatabaseContexts that have been registered with the receiver, generally all the database contexts that were created with the receiver as their EODatabase object.

__See also:__
[- `registerContext:`](#apple-gq3dg), [- `unregisterContext:`](#apple-gq4de)

---

### removeModel:

- (void)`removeModel:`(EOModel \*)_aModel_

Removes _aModel_ from the receiver's list of EOModels. Raises an exception if _aModel_ isn't one of the receiver's models.

__See also:__
[- `addModel:`](#apple-gm2dimy), [- `addModelIfCompatible:`](#apple-gm2tsoi), [- `models`](#apple-gi3dmmi)

---

### resultCacheForEntityNamed:

- (NSArray \*)`resultCacheForEntityNamed:`(NSString \*)_entityName_

Returns an array containing the globalIDs of the objects associated with _entityName_. See the class description for more discussion of this topic.

__See also:__
[- `invalidateResultCache`](#apple-gm3tm), [- `invalidateResultCacheForEntityNamed:`](#apple-gq4tm)

---

### setResultCache:forEntityNamed:

- (void)`setResultCache:`(NSArray \*)_cache_ `forEntityNamed:`(NSString \*)_entityName_

Updates the receiver's cache for _entityName_ with _cache_, an array of EOGlobalID objects, for all the enterprise objects associated with the EOEntity named _entityName_. This method is invoked automatically, and you should never need to invoke it directly. For more information on this topic, see the class description.

__See also:__
[- `invalidateResultCache`](#apple-gm3tm), [- `invalidateResultCacheForEntityNamed:`](#apple-gq4tm),
[- `resultCacheForEntityNamed:`](#apple-guyda)

---

### snapshotForGlobalID:

- (NSDictionary \*)`snapshotForGlobalID:`(EOGlobalID \*)_globalID_

Returns the snapshot associated with _globalID_ if there is one; otherwise returns `nil`. For a description of snapshots and their role in an application, see the class description.

__See also:__
[- `recordSnapshot:forGlobalID:`](#apple-gq4tioi), [- `forgetSnapshotForGlobalID:`](#apple-gqztm)

---

### snapshotForSourceGlobalID:relationshipName:

- (NSArray \*)`snapshotForSourceGlobalID:`(EOGlobalID \*)_globalID_
`relationshipName:`(NSString \*)_name_

Returns a snapshot that consists of an array of globalIDs. These globalIDs identify the objects at the destination of the to-many relationship named _name_, which is a property of the object identified by _globalID_. If there is no snapshot, returns `nil`. For a description of snapshots and their role in an application, see the class description.

---

### snapshots

- (NSDictionary \*)`snapshots`

Returns all of the receiver's snapshots, stored in a dictionary under their EOGlobalIDs.

__See also:__
[- `recordSnapshot:forSourceGlobalID:relationshipName:`](#apple-ha3tsnq), [- `recordToManySnapshots:`](#apple-ha4dima)

---

### unregisterContext:

- (void)`unregisterContext:`(EODatabaseContext \*)_aContext_

Removes _aContext_ as one of the receiver's EODatabaseContexts, without releasing it. An EODatabaseContext automatically invokes this method when deallocated; you should never need to invoke it directly.

__See also:__
[- `registerContext:`](#apple-gq3dg), [- `registeredContexts`](#apple-gi3dgnq)

---

### 

---

[!](SQL%20Statement%20Formats-2.md)
[!](More%20about%20EODatabase.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
