---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Protocols/EODatabaseContextDelegate.html
archived_at: '2026-07-15T08:11:33.228387Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EODatabaseContext.Delegate

> __(informal interface)__

> __Package:__
> com.apple.yellow.eoaccess

## Interface Description

---

An EODatabaseContext shares its delegate with its EODatabaseChannels.
These delegate methods are actually sent from EODatabaseChannel,
but they're defined in EODatabaseContext for ease of access:

: [databaseContextDidSelectObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirqxiylcmfzwkq3pnz2gk6dufzcgk3dfm5qxizjpmrqxiylcmfzwkq3pnz2gk6duiruwiu3fnrswg5cpmjvgky3uom)
: [databaseContextShouldSelectObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirqxiylcmfzwkq3pnz2gk6dufzcgk3dfm5qxizjpmrqxiylcmfzwkq3pnz2gk6duknug65lmmrjwk3dfmn2e6ytkmvrxi4y)
: [databaseContextShouldUpdateCurrentSnapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirqxiylcmfzwkq3pnz2gk6dufzcgk3dfm5qxizjpmrqxiylcmfzwkq3pnz2gk6duknug65lmmrkxazdborsug5lsojsw45ctnzqxa43in52a)
: [databaseContextShouldUsePessimisticLock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirqxiylcmfzwkq3pnz2gk6dufzcgk3dfm5qxizjpmrqxiylcmfzwkq3pnz2gk6duknug65lmmrkxgzkqmvzxg2lnnfzxi2ldjrxwg2y)

You can use the EODatabaseContext delegate methods to intervene
when objects are created and when they're fetched from the database.
This gives you more fine-grained control over such issues as how
an object's primary key is generated ( [databaseContextNewPrimaryKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirqxiylcmfzwkq3pnz2gk6dufzcgk3dfm5qxizjpmrqxiylcmfzwkq3pnz2gk6dujzsxoudsnfwwc4tzjnsxs)),
how and if objects are locked ( [databaseContextShouldLockObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirqxiylcmfzwkq3pnz2gk6dufzcgk3dfm5qxizjpmrqxiylcmfzwkq3pnz2gk6duknug65lmmrgg6y3lj5rguzldorlws5dii5wg6ytbnreui)),
what fetch specification is used to fetch objects ( [databaseContextShouldSelectObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirqxiylcmfzwkq3pnz2gk6dufzcgk3dfm5qxizjpmrqxiylcmfzwkq3pnz2gk6duknug65lmmrjwk3dfmn2e6ytkmvrxi4y)),
how batch faulting is performed ( [databaseContextShouldFetchArrayFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirqxiylcmfzwkq3pnz2gk6dufzcgk3dfm5qxizjpmrqxiylcmfzwkq3pnz2gk6duknug65lmmrdgk5ddnbaxe4tbpfdgc5lmoq) and [databaseContextShouldFetchObjectFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirqxiylcmfzwkq3pnz2gk6dufzcgk3dfm5qxizjpmrqxiylcmfzwkq3pnz2gk6duknug65lmmrdgk5ddnbhwe2tfmn2emylvnr2a)),
and so on. For more information, see the individual delegate method
descriptions.

## Instance Methods

---

### databaseContextDidFetchObjects

`public abstract void databaseContextDidFetchObjects(
EODatabaseContext aDatabaseContext,
NSArray objects,
com.apple.yellow.eocontrol.EOFetchSpecification fetchSpecification,
com.apple.yellow.eocontrol.EOEditingContext anEditingContext)`

Invoked from [objectsWithFetchSpecification](EODatabaseContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5xwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33o) after _aDatabaseContext_ fetches _objects_ using
the criteria defined in _fetchSpecification_ on
behalf of _anEditingContext_.

__See Also:__
[databaseContextShouldFetchObjectFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirqxiylcmfzwkq3pnz2gk6dufzcgk3dfm5qxizjpmrqxiylcmfzwkq3pnz2gk6duknug65lmmrdgk5ddnbhwe2tfmn2emylvnr2a)

---

### databaseContextDidSelectObjects

`public abstract void databaseContextDidSelectObjects(
EODatabaseContext aDatabaseContext,
com.apple.yellow.eocontrol.EOFetchSpecification fetchSpecification,
EODatabaseChannel channel)`

Invoked from the EODatabaseChannel method [selectObjectsWithFetchSpecification](EODatabaseChannel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny) to
tell the delegate that _channel_ selected
the objects on behalf of _aDatabaseContext_ as
specified by _fetchSpecification_.

__See Also:__
[databaseContextShouldSelectObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirqxiylcmfzwkq3pnz2gk6dufzcgk3dfm5qxizjpmrqxiylcmfzwkq3pnz2gk6duknug65lmmrjwk3dfmn2e6ytkmvrxi4y)

---

### databaseContextFailedToFetchObject

`public abstract boolean databaseContextFailedToFetchObject(
EODatabaseContext aDatabaseContext,
Object object,
com.apple.yellow.eocontrol.EOGlobalID globalID)`

Sent when a to-one fault cannot find its data
in the database. The _object_ is a
cleared fault identified by _globalID_.
If this method returns true, _aDatabaseContext_ assumes
that the delegate has handled the situation to its satisfaction,
in whatever way it deemed appropriate (for example, by displaying
an alert panel or initializing a fault object with new values).
If it returns false or if the delegate method is not implemented, _aDatabaseContext_ tracks
the globalID of the offending object. If the tracked globalID is
in the list of updated objects when [prepareForSaveWithCoordinator](EODatabaseContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5yhezlqmfzgkrtpojjwc5tfk5uxi2cdn5xxezdjnzqxi33s) is
invoked, _aDatabaseContext_ throws an
exception.

To get a list of the objects that failed to fetch, see the
method [missingObjectGlobalIDs](EODatabaseContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wws43tnfxgot3cnjswg5chnrxweylmjfchg).

---

### databaseContextNewPrimaryKey

`public abstract NSDictionary databaseContextNewPrimaryKey(
EODatabaseContext aDatabaseContext,
Object object,
EOEntity anEntity)`

Sent when a newly inserted enterprise _object_ doesn't
already have a primary key set. This delegate method can be used
to implement custom primary key generation. If the delegate is not
implemented or returns null, then _aDatabaseContext_ will
send an EOAdaptorChannel a [primaryKeyForNewRowWithEntity](EOAdaptorChannel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpobzgs3lboj4uwzlzizxxettfo5jg652xnf2gqrlooruxi6i) message
in an attempt to generate the key.

The dictionary you return from this delegate method contains
the attribute or attributes (if _object_ has a
compound primary key) that make up _object_'s
primary key.

---

### databaseContextShouldFetchArrayFault

`public abstract boolean databaseContextShouldFetchArrayFault(
EODatabaseContext databaseContext,
Object fault)`

Invoked when a fault is fired, this delegate
method lets you fine-tune the behavior of batch faulting. Delegates
can fetch the array themselves (for example, by using the EODatabaseContext
method [batchFetchRelationship](EODatabaseContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5rgc5ddnbdgk5ddnbjgk3dboruw63ttnbuxa))
and return false, or return true to allow the _databaseContext_ to
do the fetch itself. If _databaseContext_ performs
the fetch it will batch fault according to the batch count on the relationship
being fetched.

__See Also:__
[databaseContextShouldFetchObjectFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirqxiylcmfzwkq3pnz2gk6dufzcgk3dfm5qxizjpmrqxiylcmfzwkq3pnz2gk6duknug65lmmrdgk5ddnbhwe2tfmn2emylvnr2a)

---

### databaseContextShouldFetchObjectFault

`public abstract boolean databaseContextShouldFetchObjectFault(
EODatabaseContext databaseContext,
Object fault)`

Invoked when a fault is fired, this delegate
method lets you fine-tune the behavior of batch faulting. Delegates
can fetch the fault themselves (for example, by using the EODatabaseContext
method [objectsWithFetchSpecification](EODatabaseContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5xwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33o))
and return false, or return true to allow _databaseContext_ to
perform the fetch. If _databaseContext_ performs
the fetch, it will batch fault according to the batch count on the entity
being fetched.

__See Also:__
[databaseContextShouldFetchArrayFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirqxiylcmfzwkq3pnz2gk6dufzcgk3dfm5qxizjpmrqxiylcmfzwkq3pnz2gk6duknug65lmmrdgk5ddnbaxe4tbpfdgc5lmoq)

---

### databaseContextShouldFetchObjects

`public abstract NSArray databaseContextShouldFetchObjects(
EODatabaseContext aDatabaseContext,
com.apple.yellow.eocontrol.EOFetchSpecification fetchSpecification,
com.apple.yellow.eocontrol.EOEditingContext anEditingContext)`

Invoked from [objectsWithFetchSpecification](EODatabaseContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5xwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33o) to
give the delegate the opportunity to satisfy _anEditingContext_'s
fetch request (using the criteria specified in _fetchSpecification_)
from a local cache. If the delegate returns null, _aDatabaseContext_ performs
the fetch. Otherwise, the returned array is returned as the fetch
result.

__See Also:__
[databaseContextDidFetchObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirqxiylcmfzwkq3pnz2gk6dufzcgk3dfm5qxizjpmrqxiylcmfzwkq3pnz2gk6duiruwirtforrwqt3cnjswg5dt)

---

### databaseContextShouldInvalidateObjectWithGlobalID

`public abstract boolean databaseContextShouldInvalidateObjectWithGlobalID(
EODatabaseContext aDatabaseContext,
com.apple.yellow.eocontrol.EOGlobalID globalID,
NSDictionary snapshot)`

Invoked from [invalidateObjectsWithGlobalIDs](EODatabaseContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5uw45tbnruwiylumvhwe2tfmn2hgv3jorueo3dpmjqwyskeom).
Delegate can cause _aDatabaseContext_'s
object as identified by _globalID_ to
not be invalidated and that object's _snapshot_ to
not be cleared by returning false.

---

### databaseContextShouldLockObjectWithGlobalID

`public abstract boolean databaseContextShouldLockObjectWithGlobalID(
EODatabaseContext aDatabaseContext,
com.apple.yellow.eocontrol.EOGlobalID globalID,
NSDictionary snapshot)`

Invoked from [lockObjectWithGlobalID](EODatabaseContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3lj5rguzldorlws5dii5wg6ytbnreui).
The delegate should return true if it wants the operation to proceed
or false if it doesn't. Values from _snapshot_ are
used to create a qualifier from the attributes used for locking
specified for the object's entity (that is, the object identified
by _globalID_). Delegates can override
the locking mechanism by implementing their own locking procedure
and returning false. Methods that override the locking mechanism
should throw an exception on the failure to lock exactly one object.

---

### databaseContextShouldRaiseExceptionForLockFailure

`public abstract boolean databaseContextShouldRaiseExceptionForLockFailure(
EODatabaseContext aDatabaseContext,
Throwable exception)`

Invoked from [lockObjectWithGlobalID](EODatabaseContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3lj5rguzldorlws5dii5wg6ytbnreui).
This method allows the delegate to suppress an _exception_ that has
occurred during _aDatabaseContext_'s
attempt to lock the object.

---

### databaseContextShouldSelectObjects

`public abstract boolean databaseContextShouldSelectObjects(
EODatabaseContext aDatabaseContext,
com.apple.yellow.eocontrol.EOFetchSpecification fetchSpecification,
EODatabaseChannel channel)`

Invoked from the EODatabaseChannel method [selectObjectsWithFetchSpecification](EODatabaseChannel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny) to
tell the delegate that _channel_ will
select objects on behalf of _aDatabaseContext_ as
specified by _fetchSpecification_.
The delegate should not modify _fetchSpecification_'s
qualifier or fetch order. If the delegate returns true the channel
will go ahead and select the object; if the delegate returns false (possibly
after issuing custom SQL against the adaptor) the _channel_ will
skip the select and return.

---

### databaseContextShouldUpdateCurrentSnapshot

`public abstract NSDictionary databaseContextShouldUpdateCurrentSnapshot(
EODatabaseContext aDatabaseContext,
NSDictionary currentSnapshot,
NSDictionary newSnapshot,
com.apple.yellow.eocontrol.EOGlobalID globalID,
EODatabaseChannel channel)`

Invoked from the EODatabaseChannel method [fetchObject](EODatabaseChannel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5tgk5ddnbhwe2tfmn2a) when _aDatabaseContext_ already
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
to true-that is, it allows you to overwrite in-memory object values
with values from the database that may have been changed by someone
else.

Returning _currentSnapshot_ (or null)
causes the _aDatabaseContext_ to perform
the default behavior (that is, not updating the older snapshot).

---

### databaseContextShouldUsePessimisticLock

`public abstract boolean databaseContextShouldUsePessimisticLock(
EODatabaseContext databaseContext,
com.apple.yellow.eocontrol.EOFetchSpecification fetchSpecification,
EODatabaseChannel channel)`

Invoked from the EODatabaseChannel method [selectObjectsWithFetchSpecification](EODatabaseChannel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny) regardless
of the update strategy specified on _channel_'s _databaseContext_.
The delegate should not modify the qualifier or fetch order contained
in _fetchSpecification_. If the delegate
returns true the channel locks the rows being selected; if the delegate
returns false the channel selects the rows without locking.

---

### databaseContextWillFireArrayFaultForGlobalID

`public abstract void databaseContextWillFireArrayFaultForGlobalID(
EODatabaseContext dbContext,
com.apple.yellow.eocontrol.EOGlobalID globalID,
EORelationship relationship,
com.apple.yellow.eocontrol.EOFetchSpecification fetchSpec,
com.apple.yellow.eocontrol.EOEditingContext edContext)`

Invoked just before the Framework-generated
fetch specification, _fetchSpec_, is
used to clear the fault for the specified globalID and relationship.

|  |  |
| --- | --- |
| It is very dangerous to modify the fetch specification. |

---

### databaseContextWillFireObjectFaultForGlobalID

`public abstract void databaseContextWillFireObjectFaultForGlobalID(
EODatabaseContext dbContext,
com.apple.yellow.eocontrol.EOGlobalID globalID,
com.apple.yellow.eocontrol.EOFetchSpecification fetchSpec,
com.apple.yellow.eocontrol.EOEditingContext edContext)`

Invoked just before the Framework-generated
fetch specification, _fetchSpec_, is
used to clear the fault for the specified globalID.

|  |
| --- |
| It is very dangerous to modify the fetch specification. |

---

### databaseContextWillOrderAdaptorOperations

`public abstract NSArray databaseContextWillOrderAdaptorOperations(
EODatabaseContext aDatabaseContext,
NSArray databaseOperations)`

Sent from [ownsGlobalID](EODatabaseContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5ygk4tgn5zg2q3imfxgozlt). If the delegate responds
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

### databaseContextWillPerformAdaptorOperations

`public abstract NSArray databaseContextWillPerformAdaptorOperations(
EODatabaseContext aDatabaseContext,
NSArray adaptorOperations,
EOAdaptorChannel adaptorChannel)`

Sent from [ownsGlobalID](EODatabaseContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5ygk4tgn5zg2q3imfxgozlt). The delegate can return
a new _adaptorOperations_ array which _aDatabaseContext_ will
hand to _adaptorChannel_ for execution
in place of the old array of EOAdaptorOperations. This method is
useful for applications that need a special ordering of the EOAdaptorOperations
so as not to violate any database referential integrity constraints.

---

### databaseContextWillRunLoginPanelToOpenDatabaseChannel

`public abstract boolean databaseContextWillRunLoginPanelToOpenDatabaseChannel(
EODatabaseContext aDatabaseContext,
NSArray adaptorOperations,
EOAdaptorChannel adaptorChannel)`

When _aDatabaseContext_ is
about to use a _channel_, it checks
to see if the _channel_'s corresponding EOAdaptorChannel
is open. If it isn't, it attempts to open the EOAdaptorChannel
by sending it an [openChannel](EOAdaptorChannel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpn5ygk3sdnbqw43tfnq) message. If that doesn't
succeed, _aDatabaseContext_ asks the
EOAdaptorChannel's adaptor to run the login panel and open the
channel. _aDatabaseContext_ gives the
delegate a chance to intervene in this by invoking this delegate
method. The delegate can return false to stop _aDatabaseContext_ from running
the login panel. In this case, the delegate is responsible for opening
the channel. If the delegate returns true, _aDatabaseContext_ runs
the login panel.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
