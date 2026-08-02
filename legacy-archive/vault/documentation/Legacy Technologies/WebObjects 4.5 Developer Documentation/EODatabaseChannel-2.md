---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EODatabaseChannel.html
archived_at: '2026-07-15T08:11:33.491166Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EODatabaseChannel

> __Inherits
> from:__  NSObject

> __Declared in:__  EOAccess/EODatabaseChannel.h

---

## Class Description

---

An EODatabaseChannel represents an independent communication
channel to the database server. It's associated with an EODatabaseContext
and an EODatabase, which, together with the EODatabaseChannel, form
the __database level__ of Enterprise Objects Framework's
access layer. See the [EODatabase](EODatabase-3.md#apple-iraukqsginbui) class specification for
more information.

An EODatabaseChannel has an [EOAdaptorChannel](EOAdaptorChannel-3.md#apple-ijaucqsbjfcei) that it uses to connect
to the database server its EODatabase object represents. An EODatabaseChannel
fetches database records as instances of enterprise object classes
that are specified in its EODatabase's EOModel objects. An EODatabaseChannel
also has an [EODatabaseContext](EODatabaseContext-2.md#apple-ivhuiylumfrgc43finxw45dfpb2a),
which uses the channel to perform fetches and to lock rows in the
database. All of the database level objects are used automatically
by EOEditingContexts and other components of Enterprise Objects
Framework. You rarely need to interact with them directly. In particular,
you wouldn't ordinarily use an EODatabaseChannel to fetch objects.
Rather, you'd use an EOEditingContext.

## Method Types

---

> **Creating instances**
> : [- initWithDatabaseContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpnfxgs5cxnf2gqrdborqweyltmvbw63tumv4hioq)
>
> **Accessing cooperating
> objects**
> : [- adaptorChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpmfsgc4dun5zeg2dbnzxgk3a)
> : [- databaseContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpmrqxiylcmfzwkq3pnz2gk6du)
>
> **Fetching objects**
> : [- selectObjectsWithFetchSpecification:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponswyzldorhwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33ohjswi2lunfxgoq3pnz2gk6duhi)
> : [- isFetchInProgress](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpnfzumzlumnues3sqojxwo4tfonzq)
> : [- fetchObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpmzsxiy3ij5rguzldoq)
> : [- cancelFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpmnqw4y3fnrdgk5ddna)
>
> **Accessing internal fetch
> state**
> : [- setCurrentEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponsxiq3vojzgk3tuivxhi2lupe5a)
> : [- setCurrentEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponsxiq3vojzgk3tuivsgs5djnztug33oorsxq5b2)
> : [- setIsLocking:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponsxisltjrxwg23jnzttu)
> : [- isLocking](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpnfzuy33dnnuw4zy)
> : [- setIsRefreshingObjects:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponsxisltkjswm4tfonugs3thj5rguzldorztu)
> : [- isRefreshingObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpnfzvezlgojsxg2djnztu6ytkmvrxi4y)
>
> **Accessing the delegate**
> : [- setDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponsxirdfnrswoylumu5a)
> : [- delegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpmrswyzlhmf2gk)

## Instance Methods

---

### adaptorChannel

`- (EOAdaptorChannel *)adaptorChannel`

Returns the EOAdaptorChannel used by the receiver
for communication with the database server.

__See
Also:__  [- initWithDatabaseContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpnfxgs5cxnf2gqrdborqweyltmvbw63tumv4hioq)

---

### cancelFetch

`- (void)cancelFetch`

Cancels any fetch in progress.

__See
Also:__  [- isFetchInProgress](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpnfzumzlumnues3sqojxwo4tfonzq), [- selectObjectsWithFetchSpecification:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponswyzldorhwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33ohjswi2lunfxgoq3pnz2gk6duhi), [- fetchObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpmzsxiy3ij5rguzldoq)

---

### databaseContext

`- (EODatabaseContext *)databaseContext`

Returns the EODatabaseContext that controls
transactions for the receiver.

__See Also:__  [- initWithDatabaseContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpnfxgs5cxnf2gqrdborqweyltmvbw63tumv4hioq)

---

### delegate

`- (id)delegate`

Returns the receiver's delegate. An EODatabaseChannel
shares the delegate of its EODatabaseContext. See the [EODatabaseContext](EODatabaseContext-2.md#apple-ivhuiylumfrgc43finxw45dfpb2a) class
specification for the delegate methods you can implement.

__See
Also:__  [- setDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponsxirdfnrswoylumu5a)

---

### fetchObject

`- (id)fetchObject`

Fetches and returns the next object in the result
set produced by a [selectObjectsWithFetchSpecification:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponswyzldorhwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33ohjswi2lunfxgoq3pnz2gk6duhi) message;
returns nil if there are no more objects in the current result set
or if an error occurs. This method uses the receiver's EOAdaptorChannel to
fetch a row, records a snapshot with the EODatabaseContext if necessary,
and creates an enterprise object from the row if a corresponding
object doesn't already exist. The new object is sent an __awakeFromFetchInEditingContext:__ message
to allow it to finish setting up its state.

If no snapshot
exists for the fetched object, the receiver sends its EODatabase
a [recordSnapshot:forGlobalID:](EODatabase-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonss64tfmnxxezctnzqxa43in52duztpojdwy33cmfwesrb2) message
to record one. If a snapshot already exists (because the object
was previously fetched), the receiver checks whether it should overwrite
the old snapshot with the new one. It does so by asking the delegate
with a [databaseContext:shouldUpdateCurrentSnapshot:newSnapshot:globalID:databaseChannel:](EODatabaseContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrkxazdborsug5lsojsw45ctnzqxa43in52du3tfo5jw4ylqonug65b2m5wg6ytbnreuiotemf2gcytbonsug2dbnzxgk3b2) method.
If the delegate doesn't respond to this method, the EODatabaseChannel overwrites
the snapshot if it's locking or refreshing fetched objects. Further,
if the EODatabaseChannel is refreshing fetched objects, it posts
an EOObjectsChangedInStoreNotification on behalf of its EODatabaseContext
(which causes any EOEditingContext using that EODatabaseContext
to update its enterprise object with the values recorded in the
new snapshot).

For information on locking and update
strategies, see the [EODatabaseContext](EODatabaseContext-2.md#apple-ivhuiylumfrgc43finxw45dfpb2a) class
specification. For information on refreshing fetched objects, see
the EOFetchSpecification class specification.

Ordinarily,
you don't directly use an EODatabaseChannel to fetch objects.
Rather, you use an EOEditingContext, which uses an underlying EODatabaseChannel
to do its work.

__See Also:__  [- cancelFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpmnqw4y3fnrdgk5ddna), [- isFetchInProgress](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpnfzumzlumnues3sqojxwo4tfonzq), [- isLocking](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpnfzuy33dnnuw4zy), [- isRefreshingObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpnfzvezlgojsxg2djnztu6ytkmvrxi4y)

---

### initWithDatabaseContext:

`- initWithDatabaseContext:(EODatabaseContext
*)aDatabaseContext`

The designated initializer, this method initializes
a newly allocated EODatabaseChannel with _aDatabaseContext_ as
the EODatabaseContext in which it works. The new EODatabaseChannel
retains _aDatabaseContext_, and creates
an EOAdaptorChannel to communicate with the database server. Returns __self__.
Raises if the underlying adaptor context can't create a corresponding
adaptor channel.

Typically, you don't need to programmatically
create EODatabaseChannel objects. Rather, they are created automatically
by the control layer. See the [EODatabase](EODatabase-3.md#apple-iraukqsginbui) class description for more
information.

---

### isFetchInProgress

`- (BOOL)isFetchInProgress`

Returns YES if the receiver is fetching, NO otherwise.
An EODatabaseChannel is fetching if it's been sent a successful [selectObjectsWithFetchSpecification:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponswyzldorhwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33ohjswi2lunfxgoq3pnz2gk6duhi) message.
An EODatabaseChannel stops fetching when there are no more objects
to fetch or when it is sent a [cancelFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpmnqw4y3fnrdgk5ddna) message.

---

### isLocking

`- (BOOL)isLocking`

Returns YES if the receiver is locking the objects
selected, as determined by its EODatabaseContext's update strategy
or the EOFetchSpecification used to perform the select. Returns NO otherwise.
This method always returns NO when no fetch is in progress.

__See
Also:__  - __locksObjects__ (EOFetchSpecification)

---

### isRefreshingObjects

`- (BOOL)isRefreshingObjects`

Returns YES if the receiver overwrites existing
snapshots with fetched values and causes the current EOEditingContext
to overwrite existing enterprise objects with those values as well.
Returns NO otherwise. This behavior is controlled by the EOFetchSpecification
used in a [selectObjectsWithFetchSpecification:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponswyzldorhwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33ohjswi2lunfxgoq3pnz2gk6duhi) message.

__See
Also:__  - __refreshesRefetchedObjects__ (EOFetchSpecification), [- fetchObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpmzsxiy3ij5rguzldoq)

---

### selectObjectsWithFetchSpecification:editingContext:

`- (void)selectObjectsWithFetchSpecification:(EOFetchSpecification
*)fetchSpecification
editingContext:(EOEditingContext
*)anEditingContext`

Selects objects described by _fetchSpecification_ so
that they'll be fetched into _anEditingContext_.
The selected objects compose one or more result sets, each object
of which will be returned by subsequent [fetchObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpmzsxiy3ij5rguzldoq) messages in the order
prescribed by _fetchSpecification_'s
EOSortOrderings.

Raises an exception if an error occurs; the
particular exception depends on the specific error, and is indicated
in the exception's description. Some possible reasons for failure
are:

- _fetchSpecification_ is
  invalid.
- The receiver's EODatabaseContext has no transaction in progress.
- The delegate disallows the select operation.
- The receiver's EOAdaptorChannel fails to perform the select
  operation.

This method invokes the delegate
methods [databaseContext:shouldSelectObjectsWithFetchSpecification:databaseChannel:](EODatabaseContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrjwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny5giylumfrgc43finugc3tomvwdu), databaseContext:shouldUsePessimisticLockWithFetchSpecification: databaseChannel:, and [databaseContext:didSelectObjectsWithFetchSpecification:databaseChannel:](EODatabaseContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2mruwiu3fnrswg5cpmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4otemf2gcytbonsug2dbnzxgk3b2).
See their descriptions in the EODatabaseContext class specification
for more information.

You wouldn't ordinarily invoke
this method directly; rather, you'd use an EOEditingContext to
select and fetch enterprise objects.

__See
Also:__  [- fetchObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpmzsxiy3ij5rguzldoq)

---

### setCurrentEditingContext:

`- (void)setCurrentEditingContext:(EOEditingContext
*)anEditingContext`

Sets the EOEditingContext that's made the
owner of fetched objects to _anEditingContext_.
This method is automatically invoked by [selectObjectsWithFetchSpecification:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponswyzldorhwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33ohjswi2lunfxgoq3pnz2gk6duhi).
You should never invoke it directly.

__See Also:__  [- setCurrentEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponsxiq3vojzgk3tuivxhi2lupe5a)

---

### setCurrentEntity:

`- (void)setCurrentEntity:(EOEntity
*)anEntity`

Sets the EOEntity used when fetching enterprise
objects to _anEntity_. Subsequent [fetchObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpmzsxiy3ij5rguzldoq) messages during
a fetch operation create an object of the class associated with _anEntity_.
This method is invoked automatically by [selectObjectsWithFetchSpecification:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponswyzldorhwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33ohjswi2lunfxgoq3pnz2gk6duhi).You
should never need to invoke it directly.

__See
Also:__  [- setCurrentEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponsxiq3vojzgk3tuivsgs5djnztug33oorsxq5b2)

---

### setDelegate:

`- (void)setDelegate:(id)anObject`

Sets the receiver's delegate to anObject.
An EODatabaseChannel shares the delegate of its EODatabaseContext;
you should never invoke this method directly. See the EODatabaseContext
class specification for the delegate methods you can implement.

__See
Also:__  [delegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bpmrswyzlhmf2gk)

---

### setIsLocking:

`- (void)setIsLocking:(BOOL)flag`

Records whether the receiver locks the records
it selects. A EODatabaseChannel modifies its interaction with the
database server and its snapshotting behavior based on this setting.
If _flag_ is YES the EODatabaseChannel
modifies its fetching behavior to lock objects; if _flag_ is NO it
simply fetches them.

An EODatabaseChannel automatically sets
this flag according to the fetch specification used in a [selectObjectsWithFetchSpecification:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponswyzldorhwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33ohjswi2lunfxgoq3pnz2gk6duhi) message.
You might invoke this method directly if evaluating SQL directly
with EOAdaptorChannel's [evaluateExpression:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fozqwy5lborsuk6dqojsxg43jn5xdu) method.

__See
Also:__  - __locksObjects__ (EOFetchSpecification)

---

### setIsRefreshingObjects:

`- (void)setIsRefreshingObjects:(BOOL)flag`

Records whether the receiver causes existing
snapshots and enterprise objects to be overwritten with fetched
values. If _flag_ is YES the receiver
overwrites existing snapshots with fetched values and posts an EOObjectsChangedInStoreNotification
on behalf of its EODatabaseContext (which typically causes the an
existing object's EOEditingContext to replace its values with
the new ones). If _flag_ is NO, the receiver
relies on the delegate to determine whether snapshots should be
overwritten, and doesn't cause enterprise objects to be overwritten.

An
EODatabaseChannel automatically sets this flag according to the
fetch specification used in a [selectObjectsWithFetchSpecification:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponswyzldorhwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33ohjswi2lunfxgoq3pnz2gk6duhi) message.
You might invoke this method directly if evaluating SQL directly
with EOAdaptorChannel's __evaluateExpression:__ method.

__See
Also:__  - __refreshesRefetchedObjects__ (EOFetchSpecification)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
