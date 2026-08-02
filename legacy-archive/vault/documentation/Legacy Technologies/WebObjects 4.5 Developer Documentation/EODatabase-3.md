---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EODatabase.html
archived_at: '2026-07-15T08:11:33.461765Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EODatabase

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  EOAccess/EODatabase.h

---

## Class Description

---

An EODatabase object represents a single database server.
It contains an EOAdaptor which is capable of communicating with
the server, a list of EOModels that describe the server's schema,
a list of EODatabaseContexts that are connected to the server, and
a set of snapshots representing the state of all objects stored
in the server.

Each of an EODatabase's EODatabaseContexts forms a separate
transaction scope, and is in effect a separate logical user to the
server. An EODatabaseContext uses one or more pairs of EODatabaseChannel
and EOAdaptorChannel objects to manage data operations (insert,
update, delete, and fetch). Adaptors may support a limited number
of contexts per database or channels per context, but an application
is guaranteed at least one of each.

For more information on the EODatabase class, see the sections:

- ["The Database Level"](EODatabase-4.md#apple-iraukrceizcum)
- ["Snapshots"](EODatabase-4.md#apple-iraukrckinbue)

## Constants

---

EOAccess declares the following constants in EODatabase.h.

|  |  |  |
| --- | --- | --- |
| __Constant__ | __Type__ | __Description__ |
| EODistantPastTimeInterval | NSTimeInterval | The lower bound on timestamps. |
| EOGeneralDatabaseException | NSString | The name of exceptions raised by the database sublayer when errors occur during interactions with a database server. |

## Method Types

---

> **Creating instances**
> : [- initWithModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62lonf2fo2lunbgw6zdfnq5a)
> : [- initWithAdaptor:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62lonf2fo2lunbawiylqorxxeoq)
>
> **Adding and removing models**
> : [- addModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ylemrgw6zdfnq5a)
> : [- addModelIfCompatible:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ylemrgw6zdfnrewmq3pnvygc5djmjwgkoq)
> : [- removeModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfnvxxmzknn5sgk3b2)
> : [- models](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss63lpmrswy4y)
>
> **Accessing entities**
> : [- entityForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6zlooruxi6kgn5ze6ytkmvrxioq)
> : [- entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6zlooruxi6komfwwkzb2)
>
> **Recording snapshots**
> : [- recordSnapshot:forGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52duztpojdwy33cmfwesrb2)
> : [- recordSnapshot:forSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52duztpojjw65lsmnsuo3dpmjqwyskehjzgk3dboruw63ttnbuxattbnvstu)
> : [- recordSnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52hgoq)
> : [- recordToManySnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezcun5gwc3tzknxgc4dtnbxxi4z2)
>
> **Forgetting snapshots**
> : [- forgetSnapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ztpojtwk5ctnzqxa43in52em33si5wg6ytbnreuioq)
> : [- forgetSnapshotsForGlobalIDs:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ztpojtwk5ctnzqxa43in52hgrtpojdwy33cmfwesrdthi)
> : [- forgetAllSnapshots](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ztpojtwk5cbnrwfg3tbobzwq33uom)
>
> **Accessing snapshots and
> snapshot timestamps**
> : [- snapshotForGlobalID:after:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss643omfyhg2dpordg64shnrxweylmjfcduylgorsxeoq)
> : [- snapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss643omfyhg2dpordg64shnrxweylmjfcdu)
> : [- snapshotForSourceGlobalID:relationshipName:after:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss643omfyhg2dpordg64stn52xey3fi5wg6ytbnreuiotsmvwgc5djn5xhg2djobhgc3lfhjqwm5dfoi5a)
> : [- snapshotForSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss643omfyhg2dpordg64stn52xey3fi5wg6ytbnreuiotsmvwgc5djn5xhg2djobhgc3lfhi)
> : [- snapshots](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss643omfyhg2dporzq)
> : [- timestampForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss65djnvsxg5dbnvyem33si5wg6ytbnreuioq)
> : [- timestampForSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss65djnvsxg5dbnvyem33sknxxk4tdmvdwy33cmfwesrb2ojswyylunfxw443infye4ylnmu5a)
>
> **Snapshot reference counting**
> : [- incrementSnapshotCountForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62lomnzgk3lfnz2fg3tbobzwq33uinxxk3tuizxxer3mn5rgc3cjiq5a)
> : [- decrementSnapshotCountForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6zdfmnzgk3lfnz2fg3tbobzwq33uinxxk3tuizxxer3mn5rgc3cjiq5a)
> : [+ disableSnapshotRefcounting](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuiylumfrgc43ff5sgs43bmjwgku3omfyhg2dporjgkztdn52w45djnztq)
>
> **Registering database
> contexts**
> : [- registerContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfm5uxg5dfojbw63tumv4hioq)
> : [- unregisterContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss65loojswo2ltorsxeq3pnz2gk6duhi)
> : [- registeredContexts](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfm5uxg5dfojswiq3pnz2gk6duom)
>
> **Accessing the adaptor**
> : [- adaptor](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ylemfyhi33s)
>
> **Managing the database
> connection**
> : [- handleDroppedConnection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62dbnzsgyzkeojxxa4dfmrbw63tomvrxi2lpny)
>
> **Managing the result cache**
> : [- invalidateResultCache](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62loozqwy2lemf2gkutfon2wy5cdmfrwqzi)
> : [- invalidateResultCacheForEntityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62loozqwy2lemf2gkutfon2wy5cdmfrwqzkgn5zek3tunf2hsttbnvswioq)
> : [- resultCacheForEntityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfon2wy5cdmfrwqzkgn5zek3tunf2hsttbnvswioq)
> : [- setResultCache:forEntityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss643forjgk43vnr2egyldnbstuztpojcw45djor4u4ylnmvsdu)

## Class Methods

---

### disableSnapshotRefcounting

`+ (void)disableSnapshotRefcounting`

Configures EODatabase instances not to release
unreferenced snapshots.

---

## Instance Methods

---

### adaptor

`- (EOAdaptor *)adaptor`

Returns the EOAdaptor used by the receiver for
communication with the database server. Your application can interact
directly with the EOAdaptor, but should avoid altering its state
(for example, by starting a transaction with one of its adaptor
contexts).

__See Also:__  [- initWithAdaptor:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62lonf2fo2lunbawiylqorxxeoq), [- initWithModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62lonf2fo2lunbgw6zdfnq5a)

---

### addModel:

`- (void)addModel:(EOModel
*)aModel`

Adds _aModel_ to
the receiver's list of EOModels. This allows EODatabases to load
entities and their properties only as they're needed, by dividing
them among separate EOModels. _aModel_ must
use the same EOAdaptor as the receiver and use the same connection
dictionary as the receiver's other EOModels.

__See
Also:__  [- addModelIfCompatible:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ylemrgw6zdfnrewmq3pnvygc5djmjwgkoq), [- models](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss63lpmrswy4y), [- removeModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfnvxxmzknn5sgk3b2)

---

### addModelIfCompatible:

`- (BOOL)addModelIfCompatible:(EOModel
*)aModel`

Adds _aModel_ to
the receiver's list of EOModels, checking first to see whether
it's compatible with those other EOModels. Returns YES if _aModel_ is
already in the list or if it's successfully added. Returns NO if _aModel_'s
adaptor name differs from that of the receivers or if the receiver's [adaptor](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ylemfyhi33s) returns NO to
a __canServiceModel:__ message.

__See
Also:__  [- addModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ylemrgw6zdfnq5a), [- models](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss63lpmrswy4y), [- removeModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfnvxxmzknn5sgk3b2)

---

### decrementSnapshotCountForGlobalID:

`- (void)decrementSnapshotCountForGlobalID:(EOGlobalID
*)globalId`

If the receiver releases unreferenced snapshots,
decrements the reference count for the shared snapshot associated
with _globalID_; and if no more objects
refer to the snapshot, removes it from the snapshot table. (If the
receiver doesn't release snapshots, this method does nothing.)

---

### entityForObject:

`- (EOEntity *)entityForObject:(id)anObject`

Returns the EOEntity from one of the receiver's
Models that's mapped to _anObject_,
or nil if there is no such EOEntity. This method works by sending __entityForObject:__ messages
to each of the receiver's EOModels and returning the first one
found.

__See Also:__  [- entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6zlooruxi6komfwwkzb2)

---

### entityNamed:

`- (EOEntity *)entityNamed:(NSString
*)entityName`

Returns the EOEntity from one of the receiver's
Models that's named _entityName_,
or nil if there is no such EOEntity. This method works by sending __entityNamed:__ messages
to each of the receiver's EOModels and returning the first one
found.

__See Also:__  [- entityForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6zlooruxi6kgn5ze6ytkmvrxioq)

---

### forgetAllSnapshots

`- (void)forgetAllSnapshots`

Clears all of the receiver's snapshots and
posts an `EOObjectsChangedInStoreNotification` (defined
in the EOControl framework's EOObjectStore class) describing the
invalidated object. For a description of snapshots and their role
in an application, see the class description.

__See
Also:__  [- forgetSnapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ztpojtwk5ctnzqxa43in52em33si5wg6ytbnreuioq), [- forgetSnapshotsForGlobalIDs:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ztpojtwk5ctnzqxa43in52hgrtpojdwy33cmfwesrdthi), [- recordSnapshot:forGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52duztpojdwy33cmfwesrb2), [- recordSnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52hgoq), [- recordSnapshot:forSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52duztpojjw65lsmnsuo3dpmjqwyskehjzgk3dboruw63ttnbuxattbnvstu), [- recordToManySnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezcun5gwc3tzknxgc4dtnbxxi4z2)

---

### forgetSnapshotForGlobalID:

`- (void)forgetSnapshotForGlobalID:(EOGlobalID
*)globalID`

Clears the snapshot made for the enterprise
object identified by _globalID_ and
posts an `EOObjectsChangedInStoreNotification` (defined
in the EOControl framework's EOObjectStore class) describing the
invalidated object. For a description of snapshots and their role
in an application, see the class description.

__See
Also:__  [- forgetSnapshotsForGlobalIDs:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ztpojtwk5ctnzqxa43in52hgrtpojdwy33cmfwesrdthi), [- forgetAllSnapshots](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ztpojtwk5cbnrwfg3tbobzwq33uom), [- recordSnapshot:forGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52duztpojdwy33cmfwesrb2)

---

### forgetSnapshotsForGlobalIDs:

`- (void)forgetSnapshotsForGlobalIDs:(NSArray
*)globalIDs`

Clears the snapshots made for the enterprise
objects identified by each of the EOGlobalIDs in _globalIDs_ and
posts an EOObjectsChangedInStoreNotification (defined in the EOControl
framework's EOObjectStore class) describing the invalidated objects.
For a description of snapshots and their role in an application,
see the class description.

__See Also:__  [- forgetSnapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ztpojtwk5ctnzqxa43in52em33si5wg6ytbnreuioq), [- forgetAllSnapshots](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ztpojtwk5cbnrwfg3tbobzwq33uom), [- recordSnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52hgoq)

---

### handleDroppedConnection

`- (void)handleDroppedConnection`

Invoked to initiate clean up when the Framework
detects a dropped database connection. The receiver cleans up by
sending [handleDroppedConnection](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwqylomrwgkrdsn5yhazleinxw43tfmn2gs33o) to its adaptor,
and then sending [handleDroppedConnection](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnbqw4zdmmvche33qobswiq3pnzxgky3unfxw4) to all of
its registered database contexts. When the cleanup procedure is complete,
the Framework can automatically reconnect to the database.

You
should never invoke this method; it's invoked automatically by
the Framework.

---

### incrementSnapshotCountForGlobalID:

`- (void)incrementSnapshotCountForGlobalID:(EOGlobalID
*)globalId`

Increments the reference count for the shared
snapshot associated with _globalID_ if
the receiver releases unreferenced snapshots. (Does nothing if the
receiver doesn't release snapshots.)

---

### initWithAdaptor:

`- initWithAdaptor:(EOAdaptor
*)anAdaptor`

The designated initializer, this method initializes
a newly allocated EODatabase with _anAdaptor_ as
its adaptor and returns __self__.

Typically,
you don't need to programmatically create EODatabase objects.
Rather, they are created automatically by the control layer. See
the class description for more information. If you do need to create
an EODatabase programmatically, you should never associate more
than one EODatabase with a given EOAdaptor. In general, use [initWithModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62lonf2fo2lunbgw6zdfnq5a),
which automatically selects the adaptor.

---

### initWithModel:

`- initWithModel:(EOModel
*)aModel`

Initializes a newly allocated EODatabase by
creating an instance of EOAdaptor named in _aModel_ and invoking [initWithAdaptor:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62lonf2fo2lunbawiylqorxxeoq).
Returns __self__. Typically, you don't need
to programmatically create EODatabase objects. Rather, they are
created automatically by the control layer. See the class description
for more information.

__See Also:__  [+ adaptorWithModel:](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64rpmfsgc4dun5zfo2lunbgw6zdfnq5a) ( [EOAdaptor](EOAdaptor-3.md#apple-ivhuczdbob2g64q)), [- adaptorName](EOModel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmfsgc4dun5ze4ylnmu) ( [EOModel](EOModel-3.md#apple-ineeoq2iizduk))

---

### invalidateResultCache

`- (void)invalidateResultCache`

Invalidates the receiver's result cache. See
the class description for more discussion of this topic.

__See
Also:__  [- invalidateResultCacheForEntityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62loozqwy2lemf2gkutfon2wy5cdmfrwqzkgn5zek3tunf2hsttbnvswioq), [- resultCacheForEntityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfon2wy5cdmfrwqzkgn5zek3tunf2hsttbnvswioq)

---

### invalidateResultCacheForEntityNamed:

`- (void)invalidateResultCacheForEntityNamed:(NSString
*)entityName`

Invalidates the result cache containing an array
of globalIDs for the objects associated with the entity _entityName_.
See the class description for more discussion of this topic.

__See
Also:__  [- invalidateResultCache](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62loozqwy2lemf2gkutfon2wy5cdmfrwqzi), [- resultCacheForEntityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfon2wy5cdmfrwqzkgn5zek3tunf2hsttbnvswioq)

---

### models

`- (NSArray *)models`

Returns the receiver's EOModels.

__See
Also:__  [- initWithModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62lonf2fo2lunbgw6zdfnq5a), [- addModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ylemrgw6zdfnq5a), [- addModelIfCompatible:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ylemrgw6zdfnrewmq3pnvygc5djmjwgkoq), [- removeModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfnvxxmzknn5sgk3b2)

---

### recordSnapshot:forGlobalID:

`- (void)recordSnapshot:(NSDictionary
*)aSnapshot
forGlobalID:(EOGlobalID *)globalID`

Records _aSnapshot_ under _globalID_.
For a description of snapshots and their role in an application,
see the class description.

__See Also:__  [- globalIDForRow:](EOEntity-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5twy33cmfwesrcgn5zfe33xhi) ( [EOEntity](EOEntity-3.md#apple-irauuq2ginduu)), [- recordSnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52hgoq), [- forgetSnapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ztpojtwk5ctnzqxa43in52em33si5wg6ytbnreuioq)

---

### recordSnapshot:forSourceGlobalID:relationshipName:

`- (void)recordSnapshot:(NSArray
*)globalIDs
forSourceGlobalID:(EOGlobalID
*)globalID
relationshipName:(NSString *)name`

For the object identified by _globalID_,
records an NSArray of _globalIDs_ for
the to-many relationship named _name_.
These _globalIDs_ identify the objects
at the destination of the relationship. For a description of snapshots
and their role in an application, see the class description.

__See
Also:__  [- recordSnapshot:forGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52duztpojdwy33cmfwesrb2), [- recordSnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52hgoq), [- recordSnapshot:forGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52duztpojdwy33cmfwesrb2), [- snapshotForSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss643omfyhg2dpordg64stn52xey3fi5wg6ytbnreuiotsmvwgc5djn5xhg2djobhgc3lfhi)

---

### recordSnapshots:

`- (void)recordSnapshots:(NSDictionary
*)snapshots`

Records the snapshots in _snapshots_. _snapshots_ is
a dictionary whose keys are EOGlobalIDs and whose values are the
snapshots for those global IDs. For a description of snapshots and
their role in an application, see the class description.

__See
Also:__  [- recordSnapshot:forGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52duztpojdwy33cmfwesrb2), [- forgetSnapshotsForGlobalIDs:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ztpojtwk5ctnzqxa43in52hgrtpojdwy33cmfwesrdthi)

---

### recordToManySnapshots:

`- (void)recordToManySnapshots:(NSDictionary
*)snapshots`

Records the objects in _snapshots_. _snapshots_ should
be an NSDictionary of NSDictionaries, in which the top-level dictionary
has as its key the globaID of the enterprise object for which to-many
relationships are being recorded. The key's value is a dictionary
whose keys are the names of the enterprise object's to-many relationships.
Each of these keys in turn has as its value an array of globalIDs
that identify the objects at the destination of the relationship.
For a description of snapshots and their role in an application,
see the class description.

__See Also:__  [- recordSnapshot:forSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52duztpojjw65lsmnsuo3dpmjqwyskehjzgk3dboruw63ttnbuxattbnvstu), [- recordSnapshot:forGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52duztpojdwy33cmfwesrb2), [- snapshotForSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss643omfyhg2dpordg64stn52xey3fi5wg6ytbnreuiotsmvwgc5djn5xhg2djobhgc3lfhi)

---

### registerContext:

`- (void)registerContext:(EODatabaseContext
*)aContext`

Records _aContext_ as
one of the receiver's EODatabaseContexts, without retaining it. _aContext_ must have
been created with the receiver using EODatabaseContext's [initWithDatabase:](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfxgs5cxnf2gqrdborqweyltmu5a) method,
which invokes this method automatically. You should never need to
invoke this method directly.

__See Also:__  [- unregisterContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss65loojswo2ltorsxeq3pnz2gk6duhi), [- registeredContexts](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfm5uxg5dfojswiq3pnz2gk6duom)

---

### registeredContexts

`- (NSArray *)registeredContexts`

Returns all the EODatabaseContexts that have
been registered with the receiver, generally all the database contexts
that were created with the receiver as their EODatabase object.

__See
Also:__  [- registerContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfm5uxg5dfojbw63tumv4hioq), [- unregisterContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss65loojswo2ltorsxeq3pnz2gk6duhi)

---

### removeModel:

`- (void)removeModel:(EOModel
*)aModel`

Removes _aModel_ from
the receiver's list of EOModels. Raises an exception if _aModel_ isn't
one of the receiver's models.

__See Also:__  [- addModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ylemrgw6zdfnq5a), [- addModelIfCompatible:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ylemrgw6zdfnrewmq3pnvygc5djmjwgkoq), [- models](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss63lpmrswy4y)

---

### resultCacheForEntityNamed:

`- (NSArray *)resultCacheForEntityNamed:(NSString
*)entityName`

Returns an array containing the globalIDs of
the objects associated with _entityName_.
See the class description for more discussion of this topic.

__See
Also:__  [- invalidateResultCache](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62loozqwy2lemf2gkutfon2wy5cdmfrwqzi), [- invalidateResultCacheForEntityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62loozqwy2lemf2gkutfon2wy5cdmfrwqzkgn5zek3tunf2hsttbnvswioq)

---

### setResultCache:forEntityNamed:

`- (void)setResultCache:(NSArray
*)cache
forEntityNamed:(NSString *)entityName`

Updates the receiver's cache for _entityName_ with _cache_,
an array of EOGlobalID objects, for all the enterprise objects associated
with the EOEntity named _entityName_.
This method is invoked automatically, and you should never need
to invoke it directly. For more information on this topic, see the
class description.

__See Also:__  [- invalidateResultCache](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62loozqwy2lemf2gkutfon2wy5cdmfrwqzi), [- invalidateResultCacheForEntityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss62loozqwy2lemf2gkutfon2wy5cdmfrwqzkgn5zek3tunf2hsttbnvswioq), [- resultCacheForEntityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfon2wy5cdmfrwqzkgn5zek3tunf2hsttbnvswioq)

---

### setTimestampToNow

`- (void)setTimestampToNow`

Sets the internal timestamp to the value returned
by NSDate's __timeIntervalSinceReferenceDate__ method.
Used for recording subsequent snapshots.

---

### snapshotForGlobalID:

`- (NSDictionary *)snapshotForGlobalID:(EOGlobalID
*)globalID`

Equivalent to invoking [snapshotForGlobalID:after:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss643omfyhg2dpordg64shnrxweylmjfcduylgorsxeoq) with [EODistantPastTimeInterval](#apple-iraukq2jjjdeq) as
the time interval, this method returns the snapshot associated with _globalID_.

---

### snapshotForGlobalID:after:

`- (NSDictionary *)snapshotForGlobalID:(EOGlobalID
*)globalId
after:(NSTimeInterval)timestamp`

Returns the snapshot associated with _globalID_.
Returns `nil` if there
isn't a snapshot for the globalID or if the corresponding timestamp
is less than timestamp. For a description of snapshots and their
role in an application, see the class description.

__See
Also:__  [- recordSnapshot:forGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52duztpojdwy33cmfwesrb2), [- forgetSnapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss6ztpojtwk5ctnzqxa43in52em33si5wg6ytbnreuioq)

---

### snapshotForSourceGlobalID:relationshipName:

`- (NSArray *)snapshotForSourceGlobalID:(EOGlobalID
*)globalID
relationshipName:(NSString *)name`

Equivalent to invoking [snapshotForSourceGlobalID:relationshipName:after:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss643omfyhg2dpordg64stn52xey3fi5wg6ytbnreuiotsmvwgc5djn5xhg2djobhgc3lfhjqwm5dfoi5a) with [EODistantPastTimeInterval](#apple-iraukq2jjjdeq) as
the time interval, this method returns the to-many snapshot for _globalId_ and _name_.

---

### snapshotForSourceGlobalID:relationshipName:after:

`- (NSArray *)snapshotForSourceGlobalID:(EOGlobalID
*)globalID
relationshipName:(NSString *)name
after:(NSTimeInterval)timestamp`

Returns the to-many snapshot for _globalId_ and _name_.
A to-many snapshot is an array of globalIDs. These globalIDs identify
the objects at the destination of the to-many relationship named _name_,
which is a property of the object identified by _globalID._ Returns `nil` if
there isn't a to-many snapshot for _globalId_ or
if the timestamp is less than timestamp. For a description of snapshots
and their role in an application, see the class description.

---

### snapshots

`- (NSDictionary *)snapshots`

Returns all of the receiver's snapshots, stored
in a dictionary under their EOGlobalIDs.

__See
Also:__  [- recordSnapshot:forSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52duztpojjw65lsmnsuo3dpmjqwyskehjzgk3dboruw63ttnbuxattbnvstu), [- recordToManySnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezcun5gwc3tzknxgc4dtnbxxi4z2)

---

### timestampForGlobalID:

`- (NSTimeInterval)timestampForGlobalID:(EOGlobalID
*)globalId`

Returns the timestamp of the snapshot for _globalID_.
Returns `EODistantPastTimeInterval` if
there isn't a snapshot.

---

### timestampForSourceGlobalID:relationshipName:

`- (NSTimeInterval)timestampForSourceGlobalID:(EOGlobalID
*)globalId
relationshipName:(NSString *)relationshipName`

Returns the timestamp of the to-many snapshot
for the relationship specified by _relationshipName_ and the
object specified by _globalID_. Returns `EODistantPastTimeInterval` if
there isn't a snapshot.

---

### unregisterContext:

`- (void)unregisterContext:(EODatabaseContext
*)aContext`

Removes _aContext_ as
one of the receiver's EODatabaseContexts, without releasing it.
An EODatabaseContext automatically invokes this method when it's deallocated;
you should never need to invoke it directly.

__See
Also:__  [- registerContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfm5uxg5dfojbw63tumv4hioq), [- registeredContexts](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfm5uxg5dfojswiq3pnz2gk6duom)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
