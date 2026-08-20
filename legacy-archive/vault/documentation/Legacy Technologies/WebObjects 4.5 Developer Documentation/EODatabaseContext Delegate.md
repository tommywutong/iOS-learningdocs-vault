---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Protocols/EODatabaseContextDelegate.html
archived_at: '2026-07-15T08:11:36.013743Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EODatabaseContext Delegate

> __(informal protocol)__

> __Declared in:__  EOAccess/EODatabaseContext.h

## Protocol Description

---

An EODatabaseContext shares its delegate with its EODatabaseChannels.
These delegate methods are actually sent from EODatabaseChannel,
but they're defined in EODatabaseContext for ease of access:

: [- databaseContext:didSelectObjectsWithFetchSpecification:databaseChannel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2mruwiu3fnrswg5cpmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4otemf2gcytbonsug2dbnzxgk3b2)
: [- databaseContext:shouldSelectObjectsWithFetchSpecification:databaseChannel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrjwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny5giylumfrgc43finugc3tomvwdu)
: [- databaseContext:shouldUpdateCurrentSnapshot:newSnapshot:globalID:databaseChannel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrkxazdborsug5lsojsw45ctnzqxa43in52du3tfo5jw4ylqonug65b2m5wg6ytbnreuiotemf2gcytbonsug2dbnzxgk3b2)
: - databaseContext:shouldUsePessimisticLockWithFetchSpecification: databaseChannel:

You can use the EODatabaseContext delegate methods to intervene
when objects are created and when they're fetched from the database.
This gives you more fine-grained control over such issues as how
an object's primary key is generated ( [databaseContext:newPrimaryKeyForObject:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2nzsxoudsnfwwc4tzjnsxsrtpojhwe2tfmn2duzlooruxi6j2)),
how and if objects are locked ( [databaseContext:shouldLockObjectWithGlobalID:snapshot:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrgg6y3lj5rguzldorlws5dii5wg6ytbnreuiottnzqxa43in52du)),
what fetch specification is used to fetch objects ( [databaseContext:shouldSelectObjectsWithFetchSpecification:databaseChannel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrjwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny5giylumfrgc43finugc3tomvwdu)),
how batch faulting is performed ( [databaseContext:shouldFetchArrayFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrdgk5ddnbaxe4tbpfdgc5lmoq5a) and [databaseContext:shouldFetchObjectFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrdgk5ddnbhwe2tfmn2emylvnr2du)),
and so on. For more information, see the individual delegate method
descriptions.

## Instance Methods

---

### databaseContext:didFetchObjects:fetchSpecification:editingContext:

`- (void)databaseContext:(EODatabaseContext
*)aDatabaseContext
didFetchObjects:(NSArray *)objects
fetchSpecification:(EOFetchSpecification
*)fetchSpecification
editingContext:(EOEditingContext
*)anEditingContext`

Invoked from [objectsWithFetchSpecification:editingContext:](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpn5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63r2mvsgs5djnztug33oorsxq5b2) after _aDatabaseContext_ fetches _objects_ using
the criteria defined in _fetchSpecification_ on
behalf of _anEditingContext_.

__See Also:__
[- databaseContext:shouldFetchObjectFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrdgk5ddnbhwe2tfmn2emylvnr2du)

---

### databaseContext:didSelectObjectsWithFetchSpecification:databaseChannel:

`- (void)databaseContext:(EODatabaseContext
*)aDatabaseContext
didSelectObjectsWithFetchSpecification:(EOFetchSpecification
*)fetchSpecification
databaseChannel:(EODatabaseChannel
*)channel`

Invoked from the EODatabaseChannel method [selectObjectsWithFetchSpecification:editingContext:](EODatabaseChannel-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponswyzldorhwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33ohjswi2lunfxgoq3pnz2gk6duhi) to
tell the delegate that _channel_ selected
the objects on behalf of _aDatabaseContext_ as specified
by _fetchSpecification_.

__See Also:__
[- databaseContext:shouldSelectObjectsWithFetchSpecification:databaseChannel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrjwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny5giylumfrgc43finugc3tomvwdu)

---

### databaseContext:failedToFetchObject:globalID:

`- (BOOL)databaseContext:(EODatabaseContext
*)aDatabaseContext
failedToFetchObject:(id)object
globalID:(EOGlobalID *)globalID`

Sent when a to-one fault cannot find its data
in the database. The _object_ is a
cleared fault identified by _globalID_.
If this method returns YES, _aDatabaseContext_ assumes
that the delegate has handled the situation to its satisfaction,
in whatever way it deemed appropriate (for example, by displaying
an alert panel or initializing a fault object with new values).
If it returns NO or if the delegate method is not implemented, _aDatabaseContext_ tracks
the globalID of the offending object. If the tracked globalID is
in the list of updated objects when [prepareForSaveWithCoordinator:editingContext:](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpobzgk4dbojsum33sknqxmzkxnf2gqq3pn5zgi2lomf2g64r2mvsgs5djnztug33oorsxq5b2) is
invoked, _aDatabaseContext_ raises an
exception.

To get a list of the objects that failed to fetch, see the
method [missingObjectGlobalIDs](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnvuxg43jnztu6ytkmvrxir3mn5rgc3cjirzq).

---

### databaseContext:newPrimaryKeyForObject:entity:

`- (NSDictionary *)databaseContext:(EODatabaseContext
*)aDatabaseContext
newPrimaryKeyForObject:(id)object
entity:(EOEntity *)entity`

Sent when a newly inserted enterprise _object_ doesn't
already have a primary key set. This delegate method can be used
to implement custom primary key generation. If the delegate is not
implemented or returns nil, then _aDatabaseContext_ will
send an EOAdaptorChannel a [primaryKeyForNewRowWithEntity:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qojuw2ylspffwk6kgn5ze4zlxkjxxov3joruek3tunf2hsoq) message
in an attempt to generate the key.

The dictionary you return from this delegate method contains
the attribute or attributes (if _object_ has a
compound primary key) that make up _object_'s
primary key.

---

### databaseContext:shouldFetchArrayFault:

`- (BOOL)databaseContext:(EODatabaseContext
*)databaseContext
shouldFetchArrayFault:(id)fault`

Invoked when a fault is fired, this delegate
method lets you fine-tune the behavior of batch faulting. Delegates
can fetch the array themselves (for example, by using the EODatabaseContext
method [batchFetchRelationship:forSourceObjects:editingContext:](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmjqxiy3iizsxiy3ikjswyylunfxw443infyduztpojjw65lsmnsu6ytkmvrxi4z2mvsgs5djnztug33oorsxq5b2))
and return NO, or return YES to allow the _databaseContext_ to
do the fetch itself. If _databaseContext_ performs
the fetch it will batch fault according to the batch count on the
relationship being fetched.

__See Also:__
[- databaseContext:shouldFetchObjectFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrdgk5ddnbhwe2tfmn2emylvnr2du)

---

### databaseContext:shouldFetchObjectFault:

`- (BOOL)databaseContext:(EODatabaseContext
*)databaseContext
shouldFetchObjectFault:(id)fault`

Invoked when a fault is fired, this delegate
method lets you fine-tune the behavior of batch faulting. Delegates
can fetch the fault themselves (for example, by using the EODatabaseContext
method [objectsWithFetchSpecification:editingContext:](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpn5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63r2mvsgs5djnztug33oorsxq5b2))
and return NO, or return YES to allow _databaseContext_ to
perform the fetch. If _databaseContext_ performs
the fetch, it will batch fault according to the batch count on the
entity being fetched.

__See Also:__
[- databaseContext:shouldFetchArrayFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrdgk5ddnbaxe4tbpfdgc5lmoq5a)

---

### databaseContext:shouldFetchObjectsWithFetchSpecification:editingContext:

`- (NSArray *)databaseContext:(EODatabaseContext
*)aDatabaseContext
shouldFetchObjectsWithFetchSpecification:(EOFetchSpecification
*)fetchSpecification
editingContext:(EOEditingContext
*)anEditingContext`

Invoked from [objectsWithFetchSpecification:editingContext:](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpn5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63r2mvsgs5djnztug33oorsxq5b2) to
give the delegate the opportunity to satisfy _anEditingContext_'s
fetch request (using the criteria specified in _fetchSpecification_)
from a local cache. If the delegate returns nil, _aDatabaseContext_ performs
the fetch. Otherwise, the returned array is returned as the fetch
result.

__See Also:__
[databaseContext:didFetchObjects:fetchSpecification:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2mruwirtforrwqt3cnjswg5dthjtgk5ddnbjxazldnftgsy3boruw63r2mvsgs5djnztug33oorsxq5b2)

---

### databaseContext:shouldInvalidateObjectWithGlobalID:snapshot:

`- (BOOL)databaseContext:(EODatabaseContext
*)aDatabaseContext
shouldInvalidateObjectWithGlobalID:(EOGlobalID
*)globalId
snapshot:(NSDictionary *)snapshot`

Invoked from [invalidateObjectsWithGlobalIDs:](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfxhmylmnfsgc5dfj5rguzldorzvo2lunbdwy33cmfwesrdthi).
Delegate can cause _aDatabaseContext_'s
object as identified by _globalID_ to
not be invalidated and that object's _snapshot_ to
not be cleared by returning NO.

---

### databaseContext:shouldLockObjectWithGlobalID:snapshot:

`- (BOOL)databaseContext:(EODatabaseContext
*)aDatabaseContext
shouldLockObjectWithGlobalID:(EOGlobalID
*)globalID
snapshot:(NSDictionary *)snapshot`

Invoked from [lockObjectWithGlobalID:editingContext:](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwg22pmjvgky3uk5uxi2chnrxweylmjfcduzlenf2gs3thinxw45dfpb2du).
The delegate should return YES if it wants the operation to proceed
or NO if it doesn't. Values from _snapshot_ are
used to create a qualifier from the attributes used for locking
specified for the object's entity (that is, the object identified
by _globalID_). Delegates can override
the locking mechanism by implementing their own locking procedure
and returning NO. Methods that override the locking mechanism should raise an
exception on the failure to lock exactly one object.

---

### databaseContext:shouldRaiseExceptionForLockFailure:

`- (BOOL)databaseContext:(EODatabaseContext
*)aDatabaseContext
shouldRaiseExceptionForLockFailure:(NSException
*)exception`

Invoked from [lockObjectWithGlobalID:editingContext:](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwg22pmjvgky3uk5uxi2chnrxweylmjfcduzlenf2gs3thinxw45dfpb2du).
This method allows the delegate to suppress an _exception_ that
has occurred during _aDatabaseContext_'s
attempt to lock the object.

---

### databaseContext:shouldSelectObjectsWithFetchSpecification:databaseChannel:

`- (BOOL)databaseContext:(EODatabaseContext
*)aDatabaseContext
shouldSelectObjectsWithFetchSpecification:(EOFetchSpecification
*)fetchSpecification
databaseChannel:(EODatabaseChannel
*)channel`

Invoked from the EODatabaseChannel method [selectObjectsWithFetchSpecification:editingContext:](EODatabaseChannel-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponswyzldorhwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33ohjswi2lunfxgoq3pnz2gk6duhi) to
tell the delegate that _channel_ will
select objects on behalf of _aDatabaseContext_ as specified
by _fetchSpecification_. The delegate
should not modify _fetchSpecification_'s
qualifier or fetch order. If the delegate returns YES the channel
will go ahead and select the object; if the delegate returns NO (possibly
after issuing custom SQL against the adaptor) the _channel_ will
skip the select and return.

---

### databaseContext:shouldUpdateCurrentSnapshot:newSnapshot:globalID:databaseChannel:

`- (NSDictionary *)databaseContext:(EODatabaseContext
*)aDatabaseContext
shouldUpdateCurrentSnapshot:(NSDictionary
*)currentSnapshot
newSnapshot:(NSDictionary *)newSnapshot
globalID:(EOGlobalID *)globalID
databaseChannel:(EODatabaseChannel
*)channel`

Invoked from the EODatabaseChannel method [fetchObject](EODatabaseChannel-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpmzsxiy3ij5rguzldoq) when _aDatabaseContext_ already
has a snapshot (_currentSnapshot_)
for a row fetched from the database. This method is invoked without
first checking whether the snapshots are equivalent (the check would
be too expensive to do in the common case), so the receiver may
be passed equivalent snapshots. The default behavior is to not update
an older snapshot with _newSnapshot_.
The delegate can override this behavior by returning a dictionary (possibly _newSnapshot_)
that will be recorded as the updated snapshot. This results in _aDatabaseContext_ broadcasting
an `EOObjectsChangedInStoreNotification`,
causing the object store hierarchy to invalidate existing objects
(as identified by _globalID_) built
from the obsolete snapshot. You can use this method to achieve the
same effect as using a EOFetchSpecification with __setRefreshesRefetchedObjects:__ set
to YES-that is, it allows you to overwrite in-memory object values
with values from the database that may have been changed by someone
else.

Returning _currentSnapshot_ (or nil)
causes the _aDatabaseContext_ to perform
the default behavior (that is, not updating the older snapshot).

---

### databaseContext:shouldUsePessimisticLockWithFetchSpecification: databaseChannel:

`- (BOOL)databaseContext:(EODatabaseContext
*)databaseContext
shouldUsePessimisticLockWithFetchSpecification:(EOFetchSpecification
*)fetchSpecification
databaseChannel:(EODatabaseChannel
*)channel`

Invoked from the EODatabaseChannel method [selectObjectsWithFetchSpecification:editingContext:](EODatabaseChannel-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponswyzldorhwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33ohjswi2lunfxgoq3pnz2gk6duhi) regardless
of the update strategy specified on _channel_'s _databaseContext_.
The delegate should not modify the qualifier or fetch order contained
in _fetchSpecification_. If the delegate
returns YES the channel locks the rows being selected; if the delegate
returns NO the channel selects the rows without locking.

---

### databaseContext:willFireArrayFaultForGlobalID:relationship:withFetchSpecification:editingContext:

`- (void)databaseContext:(EODatabaseContext
*)dbContext
willFireArrayFaultForGlobalID:(EOGlobalID
*)globalID
relationship:(EORelationship *)relationship
withFetchSpecification:(EOFetchSpecification
*)fetchSpec
editingContext:(EOEditingContext
*)edContext`

Invoked just before the Framework-generated
fetch specification, _fetchSpec_, is
used to clear the fault for the specified globalID and relationship.

|  |  |
| --- | --- |
| It is very dangerous to modify the fetch specification. |

---

### databaseContext:willFireObjectFaultForGlobalID:withFetchSpecification:editingContext:

`- (void)databaseContext:(EODatabaseContext
*)dbContext
willFireObjectFaultForGlobalID:(EOGlobalID
*)globalID
withFetchSpecification:(EOFetchSpecification
*)fetchSpec
editingContext:(EOEditingContext
*)edContext`

Invoked just before the Framework-generated
fetch specification, _fetchSpec_, is
used to clear the fault for the specified globalID.

|  |
| --- |
| It is very dangerous to modify the fetch specification. |

---

### databaseContext:willOrderAdaptorOperationsFromDatabaseOperations:

`- (NSArray *)databaseContext:(EODatabaseContext
*)aDatabaseContext
willOrderAdaptorOperationsFromDatabaseOperations:(NSArray
*)databaseOperations`

Sent from [ownsGlobalID:](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpobsxeztpojwug2dbnztwk4y). If the delegate responds
to this message, it must return an array of EOAdaptorOperations
that _aDatabaseContext_ can then submit
to an EOAdaptorChannel for execution. The delegate can fabricate
its own array by asking each of the _databaseOperations_ for
its list of EOAdaptorOperations, and adding them to the array which
will eventually be returned by this method. The delegate is free
to optimize, order, or transform the list in whatever way it deems necessary.
This method is useful for applications that need a special ordering
of the EOAdaptorOperations so as not to violate any database referential
integrity constraints.

---

### databaseContext:willPerformAdaptorOperations:adaptorChannel:

`- (NSArray *)databaseContext:(EODatabaseContext
*)aDatabaseContext
willPerformAdaptorOperations:(NSArray
*)adaptorOperations
adaptorChannel:(EOAdaptorChannel
*)adaptorChannel`

Sent from [ownsGlobalID:](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpobsxeztpojwug2dbnztwk4y). The delegate can return
a new _adaptorOperations_ array which _aDatabaseContext_ will
hand to _adaptorChannel_ for execution
in place of the old array of EOAdaptorOperations. This method is
useful for applications that need a special ordering of the EOAdaptorOperations
so as not to violate any database referential integrity constraints.

---

### databaseContext:willRunLoginPanelToOpenDatabaseChannel:

`- (BOOL)databaseContext:(EODatabaseContext
*)aDatabaseContext
willRunLoginPanelToOpenDatabaseChannel:(EODatabaseChannel
*)channel`

When _aDatabaseContext_ is
about to use a _channel_, it checks
to see if the _channel_'s corresponding EOAdaptorChannel
is open. If it isn't, it attempts to open the EOAdaptorChannel
by sending it an [openChannel](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3pobsw4q3imfxg4zlm) message. If that doesn't
succeed, _aDatabaseContext_ asks the
EOAdaptorChannel's adaptor to run the login panel and open the
channel. _aDatabaseContext_ gives the
delegate a chance to intervene in this by invoking this delegate
method. The delegate can return NO to stop _aDatabaseContext_ from running
the login panel. In this case, the delegate is responsible for opening
the channel. If the delegate returns YES, _aDatabaseContext_ runs
the login panel.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
