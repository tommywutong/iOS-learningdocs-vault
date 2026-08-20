---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOEditingContext.html
archived_at: '2026-07-15T08:11:39.657390Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOEditingContext

> **__Inherits
> from:__**
> : [EOObjectStore](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#//apple_ref/occ/cl/EOObjectStore) : NSObject

> **__Conforms to:__**
> : [EOObserving](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOObserving.html#//apple_ref/occ/intf/EOObserving)
> : NSLocking

> __Declared in:__ : EOControl/EOEditingContext.h

---

### Class at a Glance

---

An EOEditingContext object manages a graph
of enterprise objects in an application; this object graph represents
an internally consistent view of one or more external stores (most
often a database).

#### Principal Attributes

---

- Set of enterprise objects managed by the EOEditingContext
- Parent EOObjectStore
- Set of EOEditor objects messaged by the EOEditingContext
- A message handler

#### Creation

---

|  |  |
| --- | --- |
| [- initWithParentObjectStore:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnzuxiv3jorufaylsmvxhit3cnjswg5ctorxxezj2) | Designated initializer. |

#### Commonly Used Methods

---

|  |  |
| --- | --- |
| [- objectsWithFetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3pmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4oq) | Fetches objects from an external store. |
| [- insertObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnzzwk4tuj5rguzldoq5a) | Registers a new object to be inserted into the parent EOObjectStore when changes are saved. |
| [- deleteObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3emvwgk5dfj5rguzldoq5a) | Registers that an object should be removed from the parent EOObjectStore when changes are saved. |
| [- lockObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rwwt3cnjswg5b2) | Attempts to lock an object in the external store. |
| [- hasChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3imfzug2dbnztwk4y) | Returns YES if any of the receiver has any pending changes to the parent EOObjectStore. |
| [- saveChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmf3gkq3imfxgozlt) | Commits changes made in the receiver to the parent EOObjectStore. |
| [- revert](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smv3gk4tu) | Removes everything from the undo stack, discards all insertions and deletions, and restores updated objects to their original values. |
| [- objectForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3pmjvgky3uizxxer3mn5rgc3cjiq5a) | Given a globalID, returns its associated object. |
| [- globalIDForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3hnrxweylmjfcem33sj5rguzldoq5a) | Given an object, returns its globalID. |
| [- setDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2eizlmmvtwc5dfhi) | Sets the receiver's delegate. |
| [- parentObjectStore](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3qmfzgk3tuj5rguzldorjxi33smu) | Returns the receiver's parent EOObjectStore. |
| [- rootObjectStore](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3sn5xxit3cnjswg5ctorxxezi) | Returns the receiver's root EOObjectStore. |

## Class Description

---

An EOEditingContext object represents a single "object space"
or document in an application. Its primary responsibility is managing
a graph of enterprise objects. This _object graph_ is
a group of related business objects that represent an internally
consistent view of one or more external stores (usually a database).

All objects fetched from an external store are registered
in an editing context along with a global identifier (EOGlobalID)
that's used to uniquely identify each object to the external store.
The editing context is responsible for watching for changes in its
objects (using the EOObserving protocol) and recording snapshots
for object-based undo. A single enterprise object instance exists
in one and only one editing context, but multiple copies of an object
can exist in different editing contexts. Thus object uniquing is
scoped to a particular editing context.

For more information on EOEditingContext, see the sections:

- ["Other Classes that Participate in Object Graph Management"](EOEditingContext-3.md#apple-irauoq2cijauu)
- ["Programmatically Creating an EOEditingContext"](EOEditingContext-3.md#apple-irauorcgjfbek)
- ["Using EOEditingContexts in Different Configurations"](EOEditingContext-3.md#apple-ijeucrcbjfeeq)
- ["Fetching Objects"](EOEditingContext-3.md#apple-irauorcbjfbeq)
- ["Managing Changes in Your Application"](EOEditingContext-3.md#apple-irauoqsgizeue)
- ["Methods for Managing the Object Graph"](EOEditingContext-3.md#apple-irauoqsbizeus)
- ["General Guidelines for Managing the Object Graph"](EOEditingContext-3.md#apple-irauorcfijfec)
- ["Using EOEditingContext to Archive Custom Objects in Web Objects Framework"](EOEditingContext-3.md#apple-irauoqsejfeee)

## Constants

---

In EOEditingContext.h, EOControl defines
the following `int` constant
to specifies the order in which editing contexts perform end of
event processing in [processRecentChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3qojxwgzltonjgky3fnz2eg2dbnztwk4y).

- EditingContextFlushChangesRunLoopOrdering

Messages with lower order numbers are processed before messages
with higher order numbers. In an application built with the Application
Kit, the constant order value schedules the editing context to perform
its processing before the undo stack group is closed or window display
is updated.

EOEditingContext.h also defines NSString
constants for the names of the notifications it posts. See the section ["Notifications"](#apple-ijeuiq2hindec) for
more information.

## Adopted Protocols

---

> EOObserving: [- objectWillChange:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOObserving.html#//apple_ref/occ/intfm/EOObserving/objectWillChange:)
>
> NSLocking: [- lock](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rww)
> : [- unlock](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3vnzwg6y3l)

## Method Types

---

> **Initializing an EOEditingContext**
> : [- initWithParentObjectStore:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnzuxiv3jorufaylsmvxhit3cnjswg5ctorxxezj2)
>
> **Fetching objects**
> : [- objectsWithFetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3pmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4oq)
>
> **Committing or discarding
> changes**
> : [- saveChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmf3gkq3imfxgozlt)
> : [- saveChanges:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmf3gkq3imfxgozlthi)
> : [- tryToSaveChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3uoj4vi32tmf3gkq3imfxgozlt)
> : [- refaultObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvtgc5lmorhwe2tfmn2hg)
> : [- refault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvtgc5lmoq5a)
> : [- refetch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvtgk5ddna5a)
> : [- revert](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smv3gk4tu)
> : [- revert:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smv3gk4tuhi)
> : [- invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnz3gc3djmrqxizkbnrwe6ytkmvrxi4y)
>
> **Registering changes**
> : [- deleteObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3emvwgk5dfj5rguzldoq5a)
> : [- insertObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnzzwk4tuj5rguzldoq5a)
> : [- insertObject:withGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnzzwk4tuj5rguzldoq5ho2lunbdwy33cmfwesrb2)
> : [- objectWillChange:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3pmjvgky3uk5uwy3cdnbqw4z3fhi)
> : [- processRecentChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3qojxwgzltonjgky3fnz2eg2dbnztwk4y)
>
> **Checking changes**
> : [- deletedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3emvwgk5dfmrhwe2tfmn2hg)
> : [- insertedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnzzwk4tumvse6ytkmvrxi4y)
> : [- updatedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3vobsgc5dfmrhwe2tfmn2hg)
> : [- hasChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3imfzug2dbnztwk4y)
>
> **Object registration and
> snapshotting**
> : [- forgetObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3gn5zgozluj5rguzldoq5a)
> : [- recordObject:globalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvrw64tej5rguzldoq5go3dpmjqwyskehi)
> : [- committedSnapshotForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3dn5ww22luorswiu3omfyhg2dpordg64spmjvgky3uhi)
> : [- currentEventSnapshotForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3dovzhezloorcxmzloorjw4ylqonug65cgn5ze6ytkmvrxioq)
> : [- objectForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3pmjvgky3uizxxer3mn5rgc3cjiq5a)
> : [- globalIDForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3hnrxweylmjfcem33sj5rguzldoq5a)
> : [- registeredObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvtws43umvzgkzcpmjvgky3uom)
>
> **Timestamping snapshots**
> : [+ defaultFetchTimestampLag](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxwizlgmf2wy5cgmv2gg2cunfwwk43umfwxatdbm4)
> : [+ setDefaultFetchTimestampLag:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxxgzluirswmylvnr2emzlumnufi2lnmvzxiylnobggczz2)
> : [- fetchTimestamp](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3gmv2gg2cunfwwk43umfwxa)
> : [- setFetchTimestamp:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2emzlumnufi2lnmvzxiylnoa5a)
>
> **Locking objects**
> : [- lockObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rwwt3cnjswg5b2)
> : [- lockObjectWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rwwt3cnjswg5cxnf2gqr3mn5rgc3cjiq5gkzdjoruw4z2dn5xhizlyoq5a)
> : [- isObjectLockedWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jonhwe2tfmn2ey33dnnswiv3jorueo3dpmjqwyskehjswi2lunfxgoq3pnz2gk6duhi)
> : [- setLocksObjectsBeforeFirstModification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2ey33dnnzu6ytkmvrxi42cmvtg64tfizuxe43ujvxwi2lgnfrwc5djn5xdu)
> : [- locksObjectsBeforeFirstModification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rww42pmjvgky3uonbgkztpojsum2lson2e233enftgsy3boruw63q)
>
> **Undoing operations**
> : [- redo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvsg6oq)
> : [- undo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3vnzsg6oq)
> : [- setUndoManager:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2fk3ten5gwc3tbm5sxeoq)
> : [- undoManager](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3vnzsg6tlbnzqwozls)
>
> **Accessing the shared
> editing context**
> : [- sharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tnbqxezleivsgs5djnztug33oorsxq5a)
> : [- setSharedEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2fg2dbojswirlenf2gs3thinxw45dfpb2du)
>
> **Deletion and Validation
> Behavior**
> : [- setPropagatesDeletesAtEndOfEvent:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2fa4tpobqwoylumvzuizlmmv2gk42borcw4zcpmzcxmzlooq5a)
> : [- propagatesDeletesAtEndOfEvent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3qojxxaylhmf2gk42emvwgk5dfonaxirlomrhwmrlwmvxhi)
> : [- setStopsValidationAfterFirstError:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2fg5dpobzvmylmnfsgc5djn5xecztumvzem2lson2ek4tsn5zdu)
> : [- stopsValidationAfterFirstError](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3torxxa42wmfwgszdboruw63sbmz2gk4sgnfzhg5cfojzg64q)
>
> **Returning related object
> stores**
> : [- parentObjectStore](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3qmfzgk3tuj5rguzldorjxi33smu)
> : [- rootObjectStore](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3sn5xxit3cnjswg5ctorxxezi)
>
> **Managing editors**
> : [- editors](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3fmruxi33som)
> : [- addEditor:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3bmrsekzdjorxxeoq)
> : [- removeEditor:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvww65tfivsgs5dpoi5a)
>
> **Setting the delegate**
> : [- setDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2eizlmmvtwc5dfhi)
> : [- delegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3emvwgkz3borsq)
>
> **Setting the message handler**
> : [- setMessageHandler:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2e2zltonqwozkimfxgi3dfoi5a)
> : [- messageHandler](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3nmvzxgylhmvegc3tenrsxe)
>
> **Invalidating objects**
> : [- setInvalidatesObjectsWhenFreed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2es3twmfwgszdborsxgt3cnjswg5dtk5ugk3sgojswkzb2)
> : [- invalidatesObjectsWhenFreed](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnz3gc3djmrqxizltj5rguzldorzvo2dfnzdhezlfmq)
>
> **Locking**
> : [- lock](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rww)
> : [- unlock](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3vnzwg6y3l)
>
> **Working with raw rows**
> : [- faultForRawRow:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3gmf2wy5cgn5zfeylxkjxxootfnz2gs5dzjzqw2zlehi)
>
> **Unarchiving from nib**
> : [+ defaultParentObjectStore](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxwizlgmf2wy5cqmfzgk3tuj5rguzldorjxi33smu)
> : [+ setDefaultParentObjectStore:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxxgzluirswmylvnr2faylsmvxhit3cnjswg5ctorxxezj2)
> : [+ setSubstitutionEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxxgzlukn2we43unf2hk5djn5xekzdjoruw4z2dn5xhizlyoq5a)
> : [+ substitutionEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxxg5lcon2gs5dvoruw63sfmruxi2lom5bw63tumv4hi)
>
> **Nested EOEditingContext
> support**
> : [- objectsWithFetchSpecification:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3pmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4otfmruxi2lom5bw63tumv4hioq)
> : [- objectsForSourceGlobalID:relationshipName:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3pmjvgky3uondg64stn52xey3fi5wg6ytbnreuiotsmvwgc5djn5xhg2djobhgc3lfhjswi2lunfxgoq3pnz2gk6duhi)
> : [- arrayFaultWithSourceGlobalID:relationshipName:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3bojzgc6kgmf2wy5cxnf2gqu3povzggzkhnrxweylmjfcdu4tfnrqxi2lpnzzwq2lqjzqw2zj2mvsgs5djnztug33oorsxq5b2)
> : [- faultForGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3gmf2wy5cgn5zeo3dpmjqwyskehjswi2lunfxgoq3pnz2gk6duhi)
> : [- saveChangesInEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmf3gkq3imfxgozltjfxekzdjoruw4z2dn5xhizlyoq5a)
> : [- refaultObject:withGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvtgc5lmorhwe2tfmn2du53jorueo3dpmjqwyskehjswi2lunfxgoq3pnz2gk6duhi)
> : [- invalidateObjectsWithGlobalIDs:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnz3gc3djmrqxizkpmjvgky3uonlws5dii5wg6ytbnreui4z2)
> : [- initializeObject:withGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnzuxi2lbnruxuzkpmjvgky3uhj3ws5dii5wg6ytbnreuiotfmruxi2lom5bw63tumv4hioq)
>
> **Archiving and unarchiving
> objects**
> : [+ encodeObject:withCoder:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxwk3tdn5sgkt3cnjswg5b2o5uxi2cdn5sgk4r2)
> : [+ initObject:withCoder:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxws3tjorhwe2tfmn2du53jorueg33emvzdu)
> : [+ setUsesContextRelativeEncoding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxxgzlukvzwk42dn5xhizlyorjgk3dboruxmzkfnzrw6zdjnzttu)
> : [+ usesContextRelativeEncoding](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxxk43fonbw63tumv4hiutfnrqxi2lwmvcw4y3pmruw4zy)

## Class Methods

---

### defaultFetchTimestampLag

`+ (NSTimeInterval)defaultFetchTimestampLag`

Returns the default timestamp lag.

---

### defaultParentObjectStore

`+ (EOObjectStore *)defaultParentObjectStore`

Returns the EOObjectStore that is the default
parent object store for new editing contexts. Normally this is the
EOObjectStoreCoordinator returned from the EOObjectStoreCoordinator class method [defaultCoordinator](EOObjectStoreCoordinator-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6ytkmvrxiu3un5zgkq3pn5zgi2lomf2g64rpmrswmylvnr2eg33pojsgs3tborxxe).

__See
Also:__  [+ setDefaultParentObjectStore:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxxgzluirswmylvnr2faylsmvxhit3cnjswg5ctorxxezj2)

---

### encodeObject:withCoder:

`+ (void)encodeObject:(id)object
withCoder:(NSCoder *)encoder`

Invoked by an enterprise object _object_ to
ask the EOEditingContext to encode _object_ using _encoder_.
For more discussion of this subject, see ["Using EOEditingContext to Archive Custom Objects in Web Objects Framework"](EOEditingContext-3.md#apple-irauoqsejfeee).

__See
Also:__  [+ initObject:withCoder:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxws3tjorhwe2tfmn2du53jorueg33emvzdu), [+ setUsesContextRelativeEncoding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxxgzlukvzwk42dn5xhizlyorjgk3dboruxmzkfnzrw6zdjnzttu), [+ usesContextRelativeEncoding](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxxk43fonbw63tumv4hiutfnrqxi2lwmvcw4y3pmruw4zy)

---

### initObject:withCoder:

`+ (id)initObject:(id)object
withCoder:(NSCoder *)decoder`

Invoked by an enterprise object _object_ to
ask the EOEditingContext to initialize _object_ from
data in _decoder_. For more discussion
of this subject, see ["Using EOEditingContext to Archive Custom Objects in Web Objects Framework"](EOEditingContext-3.md#apple-irauoqsejfeee).

__See
Also:__  [+ encodeObject:withCoder:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxwk3tdn5sgkt3cnjswg5b2o5uxi2cdn5sgk4r2), [+ setUsesContextRelativeEncoding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxxgzlukvzwk42dn5xhizlyorjgk3dboruxmzkfnzrw6zdjnzttu), [+ usesContextRelativeEncoding](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxxk43fonbw63tumv4hiutfnrqxi2lwmvcw4y3pmruw4zy)

---

### __instancesRetainRegisteredObjects__

`+ (BOOL)instancesRetainRegisteredObjects`

Returns YES if editing contexts retain their
registered objects; NO otherwise.

---

### setDefaultFetchTimestampLag:

`+ (void)setDefaultFetchTimestampLag:(NSTimeInterval)lag`

Sets the default timestamp lag for newly instantiated
editing contexts to _lag_. The default
lag is 3600.0 seconds (one hour).

When a new editing context
is initialized, it is assigned a fetch timestamp equal to the current
time less the default timestamp lag. Setting the lag to a large
number might cause every new editing context to accept very old
cached data. Setting the lag to too low a value might degrade performance
due to excessive fetching. A negative lag value is treated as 0.0.

---

### setDefaultParentObjectStore:

`+ (void)setDefaultParentObjectStore:(EOObjectStore
*)store`

Sets thedefault
parent EOObjectStore to _store_. You
use this method before loading a nib file to change the default
parent EOObjectStores of the EOEditingContexts in the nib file.
The object you supply for _store_ can
be a different EOObjectStoreCoordinator or another EOEditingContext
(if you're using a nested EOEditingContext). After loading a nib
with an EOEditingContext substituted as the default parent EOObjectStore,
you should restore the default behavior by setting the default parent EOObjectStore
to nil. For example:
> ```
> [EOEditingContext setDefaultParentObjectStore:editingContext];
> nibLoaded = [NSBundle loadNibNamed:@"thirdNib" owner:self];
> [EOEditingContext setDefaultObjectStore:nil]; // Restore default
> ```

A default parent object
store is global until it is changed again. For more discussion of
this topic, see the chapter "Application Configurations" in
the _Enterprise Objects Framework Developer's Guide_.

__See
Also:__  [+ defaultParentObjectStore](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxwizlgmf2wy5cqmfzgk3tuj5rguzldorjxi33smu)

---

### __setInstancesRetainRegisteredObjects:__

`+ (void)setInstancesRetainRegisteredObjects:(BOOL)flag`

If _flag_ is YES,
editing contexts retain their registered objects; if NO, they don't.
Retaining objects is necessary to prevent enterprise objects from
being finalized asynchronously on the Java side of the Java Bridge.
The default value for _flag_ is YES if
an application contains Java code; NO otherwise.

---

### setSubstitutionEditingContext:

`+ (void)setSubstitutionEditingContext:(EOEditingContext
*)anEditingContext`

Assigns _anEditingContext_ as
the EOEditingContext to substitute for the one specified in a nib
file you're about to load. Using this method causes all of the
connections in your nib file to be redirected to _anEditingContext_.
This can be useful when you want an interface loaded from a second
nib file to use an existing EOEditingContext. After loading a nib
with a substitution EOEditingContext, you should restore the default
behavior by setting the substitution EOEditingContext to nil. For
example:
> ```
> [EOEditingContext setSubstitutionEditingContext:editingContext];
> nibLoaded = [NSBundle loadNibNamed:@"thirdNib" owner:self];
> [EOEditingContext setSubstitutionEditingContext:nil]; // Restore default
> ```

A substitution
editing context is global until it is changed again. For more discussion
of this topic, see the chapter "Application Configurations"
in the _Enterprise Objects Framework Developer's Guide_.

__See
Also:__  [+ substitutionEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxxg5lcon2gs5dvoruw63sfmruxi2lom5bw63tumv4hi)

---

### setUsesContextRelativeEncoding:

`+ (void)setUsesContextRelativeEncoding:(BOOL)flag`

Sets according to _flag_ whether [encodeObject:withCoder:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxwk3tdn5sgkt3cnjswg5b2o5uxi2cdn5sgk4r2) uses context-relative
encoding. For more discussion of this subject, see ["Using EOEditingContext to Archive Custom Objects in Web Objects Framework"](EOEditingContext-3.md#apple-irauoqsejfeee).

__See
Also:__  [+ usesContextRelativeEncoding](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxxk43fonbw63tumv4hiutfnrqxi2lwmvcw4y3pmruw4zy), [+ encodeObject:withCoder:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxwk3tdn5sgkt3cnjswg5b2o5uxi2cdn5sgk4r2)

---

### substitutionEditingContext

`+ (EOEditingContext *)substitutionEditingContext`

Returns the substitution EOEditingContext if
one has been specified. Otherwise returns nil.

__See
Also:__  [+ setSubstitutionEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxxgzlukn2we43unf2hk5djn5xekzdjoruw4z2dn5xhizlyoq5a)

---

### usesContextRelativeEncoding

`+ (BOOL)usesContextRelativeEncoding`

Returns YES to indicate that [encodeObject:withCoder:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxwk3tdn5sgkt3cnjswg5b2o5uxi2cdn5sgk4r2) uses context
relative encoding, NO otherwise. For more discussion of this subject,
see ["Using EOEditingContext to Archive Custom Objects in Web Objects Framework"](EOEditingContext-3.md#apple-irauoqsejfeee).

__See
Also:__  [+ setUsesContextRelativeEncoding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxxgzlukvzwk42dn5xhizlyorjgk3dboruxmzkfnzrw6zdjnzttu)

---

## Instance Methods

---

### addEditor:

`- (void)addEditor:(id)editor`

Adds _editor_ to
the receiver's set of [EOEditors](EOEditors.md#apple-inbecrckindee). For more
explanation, see the method description for [editors](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3fmruxi33som) and the [EOEditors](EOEditors.md#apple-inbecrckindee) informal protocol specification.

__See
Also:__  [- removeEditor:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvww65tfivsgs5dpoi5a)

---

### arrayFaultWithSourceGlobalID:relationshipName:editingContext:

`- (NSArray *)arrayFaultWithSourceGlobalID:(EOGlobalID
*)globalID
relationshipName:(NSString *)name
editingContext:(EOEditingContext
*)anEditingContext`

Overrides the implementation inherited from
EOObjectStore. If the objects associated with the EOGlobalID _globalID_ are
already registered in the receiver, returns those objects. Otherwise, propagates
the message down the object store hierarchy, through the parent
object store, ultimately to the associated EODatabaseContext. The
EODatabaseContext creates and returns a to-many fault.

When
a parent EOEditingContext receives this on behalf of a child EOEditingContext
and the EOGlobalID _globalID_ identifies
a newly inserted object in the parent, the parent returns a copy
of its object's relationship array with the member objects translated
into objects in the child EOEditingContext.

For more
information on faults, see the EOObjectStore, EODatabaseContext
(EOAccess), EOFault, and EOFaultHandler class specifications.

__See
Also:__  [- faultForGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3gmf2wy5cgn5zeo3dpmjqwyskehjswi2lunfxgoq3pnz2gk6duhi)

---

### committedSnapshotForObject:

`- (NSDictionary *)committedSnapshotForObject:(id)object`

Returns a dictionary containing a snapshot
of _object_ that reflects its committed
values (that is, its values as they were last committed to the database).In
other words, this snapshot represents the state of the object before
any modifications were made to it. The snapshot is updated to the
newest object state after a save.

__See
Also:__  [- currentEventSnapshotForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3dovzhezloorcxmzloorjw4ylqonug65cgn5ze6ytkmvrxioq)

---

### currentEventSnapshotForObject:

`- (NSDictionary *)currentEventSnapshotForObject:(id)object`

Returns a dictionary containing a snapshot
of _object_ that reflects its state
as it was at the beginning of the current event loop. After the
end of the current event-upon invocation of __processRecentChanges__-this
snapshot is updated to hold the modified state of the object.

__See
Also:__  [- committedSnapshotForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3dn5ww22luorswiu3omfyhg2dpordg64spmjvgky3uhi), [- processRecentChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3qojxwgzltonjgky3fnz2eg2dbnztwk4y)

---

### delegate

`- (id)delegate`

Returns the receiver's delegate.

__See
Also:__  [- setDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2eizlmmvtwc5dfhi)

---

### deleteObject:

`- (void)deleteObject:(id)object`

Specifies that _object_ should
be removed from the receiver's parent EOObjectStore when changes
are committed. At that time, the object will be removed from the
uniquing tables.

__See Also:__  [- deletedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3emvwgk5dfmrhwe2tfmn2hg)

---

### deletedObjects

`- (NSArray *)deletedObjects`

Returns the objects that have been deleted from
the receiver's object graph.

__See Also:__  [- updatedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3vobsgc5dfmrhwe2tfmn2hg), [- insertedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnzzwk4tumvse6ytkmvrxi4y)

---

### editors

`- (NSArray *)editors`

Returns the receiver's editors. Editors are
special-purpose delegate objects that may contain uncommitted changes
that need to be validated and applied to enterprise objects before
the EOEditingContext saves changes. For example, EODisplayGroups
(EOInterface) register themselves as editors with the EOEditingContext
of their data sources so that they can save any changes in the key text
field. For more information, see the [EOEditors](EOEditors.md#apple-inbecrckindee) informal protocol specification
and the EODisplayGroup class specification.

__See
Also:__  [- addEditor:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3bmrsekzdjorxxeoq), [- removeEditor:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvww65tfivsgs5dpoi5a)

---

### faultForGlobalID:editingContext:

`- (id)faultForGlobalID:(EOGlobalID
*)globalID
editingContext:(EOEditingContext
*)anEditingContext`

Overrides the implementation inherited from
EOObjectStore. If the object associated with the EOGlobalID _globalID_ is
already registered in the receiver (or in the receiver's [sharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tnbqxezleivsgs5djnztug33oorsxq5a)), this
method returns that object. Otherwise, the method propagates the
message down the object store hierarchy, through the parent object
store, ultimately to the associated EODatabaseContext. The EODatabaseContext
creates and returns a to-one fault.

For example, suppose you
want the department object whose __deptID__ has
a particular value. The most efficient way to get it is to look
it up by its globalID using __faultForGlobalID:editingContext:__:

> ```
> EOEntity *entity = [[[editingContext rootObjectStore] modelGroup]
>         entityNamed:entityName];
> EOGlobalID *gid = [entity globalIDForRow:[NSDictionary
>         dictionaryWithObjectsAndKeys:deptIdentifier, @"deptID", nil]];
> return [editingContext faultForGlobalID:gid editingContext:editingContext];
> ```

If
the department object is already registered in the EOEditingContext, this
code returns the object (without going to the database). If not,
a fault for this object is created, and the object is fetched only when
you trigger the fault.

In a nested editing context configuration,
when a parent EOEditingContext is sent __faultForGlobalID:editingContext:__ on
behalf of a child EOEditingContext and _globalID_ identifies
a newly inserted object in the parent, the parent registers a copy
of the object in the child.

For more discussion of
this method, see the section ["Working with Objects Across Multiple EOEditingContexts"](EOEditingContext-3.md#apple-ijeucq2fiveei).
For more information on faults, see the EOObjectStore, EODatabaseContext (EOAccess), EOFault, and
EOFaultHandler class specifications.

__See
Also:__  [- arrayFaultWithSourceGlobalID:relationshipName:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3bojzgc6kgmf2wy5cxnf2gqu3povzggzkhnrxweylmjfcdu4tfnrqxi2lpnzzwq2lqjzqw2zj2mvsgs5djnztug33oorsxq5b2)

---

### faultForRawRow:entityNamed:

`- (id)faultForRawRow:(id)row
entityNamed:(NSString *)entityName`

Returns a fault for the raw row _row_ by
invoking [faultForRawRow:entityNamed:editingContext:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#//apple_ref/occ/instm/EOObjectStore/faultForRawRow:entityNamed:editingContext:) with __self__ as
the editing context.

---

### fetchTimestamp

`- (NSTimeInterval)fetchTimestamp`

Returns
the receiver's fetch timestamp.

---

### forgetObject:

`- (void)forgetObject:(id)object`

Removes _object_ from
the uniquing tables and causes the receiver to remove itself as
the object's observer. This method is invoked whenever an object
being observed by an EOEditingContext is deallocated. Note that
this method does not have the effect of releasing and freeing the
object. You should never invoke this method directly. The correct
way to remove an object from its editing context is to remove every
reference to the object by refaulting any object that references
it (using [refaultObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvtgc5lmorhwe2tfmn2hg) or [invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnz3gc3djmrqxizkbnrwe6ytkmvrxi4y)).
Also note that this method does _not_ have
the effect of deleting an object-to delete an object you should
either use the [deleteObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3emvwgk5dfj5rguzldoq5a) method
or remove the object from an owning relationship.

---

### globalIDForObject:

`- (EOGlobalID *)globalIDForObject:object`

Returns the EOGlobalID for _object_.
All objects fetched from an external store are registered in an EOEditingContext
along with a global identifier (EOGlobalID) that's used to uniquely
identify each object to the external store. If _object_ hasn't
been registered in the EOEditingContext or in its [sharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tnbqxezleivsgs5djnztug33oorsxq5a) (that
is, if no match is found), this method returns nil. Objects are
registered in an EOEditingContext using the [insertObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnzzwk4tuj5rguzldoq5a) method,
or, when fetching, with [recordObject:globalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvrw64tej5rguzldoq5go3dpmjqwyskehi).

__See
Also:__  [- objectForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3pmjvgky3uizxxer3mn5rgc3cjiq5a)

---

### hasChanges

`- (BOOL)hasChanges`

Returns YES if any of the objects in the receiver's
object graph have been modified-that is, if any objects have been
inserted, deleted, or updated.

---

### initWithParentObjectStore:

`- initWithParentObjectStore:(EOObjectStore
*)anObjectStore`

Initializes the receiver with _anObjectStore_ as
its parent EOObjectStore and returns `self`.
The receiver shares objects with the default shared editing context
(if any) unless you change its shared editing context with [setSharedEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2fg2dbojswirlenf2gs3thinxw45dfpb2du).This
method is the designated initializer for EOEditingContext. For more
discussion of parent EOObjectStores, see ["Other Classes that Participate in Object Graph Management"](EOEditingContext-3.md#apple-irauoq2cijauu).

---

### initializeObject:withGlobalID:editingContext:

`- (void)initializeObject:(id)object
withGlobalID:(EOGlobalID *)globalID
editingContext:(EOEditingContext
*)anEditingContext`

Overrides the implementation inherited from
EOObjectStore to build the properties for the _object_ identified
by _globalID_. When a parent EOEditingContext
receives this on behalf of a child EOEditingContext (as represented
by _anEditingContext_), and the _globalID_ identifies
an object instantiated in the parent, the parent returns properties
extracted from its object and translated into the child's context.
This ensures that a nested context "inherits" modified values
from its parent EOEditingContext. If the receiver doesn't have _object_,
the request is forwarded the receiver's parent EOObjectStore.

---

### insertedObjects

`- (NSArray *)insertedObjects`

Returns the objects that have been inserted
into the receiver's object graph.

__See Also:__  [- deletedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3emvwgk5dfmrhwe2tfmn2hg), [- updatedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3vobsgc5dfmrhwe2tfmn2hg)

---

### insertObject:

`- (void)insertObject:(id)object`

Registers (by invoking [insertObject:withGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnzzwk4tuj5rguzldoq5ho2lunbdwy33cmfwesrb2)) _object_ to
be inserted in the receiver's parent EOObjectStore the next time
changes are saved. In the meantime, _object_ is
registered in the receiver with a temporary globalID.

__See
Also:__  [- insertedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnzzwk4tumvse6ytkmvrxi4y), [- deletedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3emvwgk5dfmrhwe2tfmn2hg), [- insertObject:withGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnzzwk4tuj5rguzldoq5ho2lunbdwy33cmfwesrb2)

---

### insertObject:withGlobalID:

`- (void)insertObject:object
withGlobalID:(EOGlobalID *)globalID`

Registers a new _object_ identified
by _globalID_ that should be inserted
in the parent EOObjectStore when changes are saved. Works by invoking [recordObject:globalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvrw64tej5rguzldoq5go3dpmjqwyskehi), unless the
receiver already contains the object. Sends _object_ the
message [awakeFromInsertionInEditingContext:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxoyllmvdhe33njfxhgzlsoruw63sjnzcwi2lunfxgoq3pnz2gk6duhi). _globalID_ must
respond YES to [isTemporary](EOGlobalID-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2hnrxweylmjfcc62ltkrsw24dpojqxe6i). When the external store
commits _object_, it re-records it
with the appropriate permanent globalID.

It is an error to
insert an object that's already registered in an editing context
unless you are effectively undeleting the object by reinserting
it.

__See Also:__  [- insertObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnzzwk4tuj5rguzldoq5a)

---

### invalidateAllObjects

`- (void)invalidateAllObjects`

Overrides the implementation inherited from
EOObjectStore to discard the values of objects cached in memory
and refault them, which causes them to be refetched from the external
store the next time they're accessed. This method sends the message __invalidateObjectsWithGlobalIDs:__ to
the parent object store with the globalIDs of all of the objects
cached in the receiver. When an EOEditingContext receives this message,
it propagates the message down the object store hierarchy. EODatabaseContexts
discard their snapshots for invalidated objects and broadcast an [EOObjectsChangedInStoreNotification](#apple-ijeuirceifbuu). (EODatabaseContext
is defined in EOAccess.)

The final effect of this method is
to refault all objects currently in memory. This refaulting in turn releases
all objects not retained by your application or by an EODisplayGroup. The
next time you access one of these objects, it's refetched from
the database.

To flush the entire application's cache
of all values fetched from an external store, use a statement such as
the following:

> ```
> [[editingContext rootObjectStore] invalidateAllObjects];
> ```

If
you just want to discard uncommitted changes but you don't want
to sacrifice the values cached in memory, use the EOEditingContext [revert](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smv3gk4tu) method, which
reverses all changes and clears the undo stack. For more discussion
of this topic, see the section ["Methods for Managing the Object Graph"](EOEditingContext-3.md#apple-irauoqsbizeus).

__See
Also:__  [- refetch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvtgk5ddna5a), [- invalidateObjectsWithGlobalIDs:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnz3gc3djmrqxizkpmjvgky3uonlws5dii5wg6ytbnreui4z2)

---

### invalidateObjectsWithGlobalIDs:

`- (void)invalidateObjectsWithGlobalIDs:(NSArray
*)globalIDs`

Overrides the implementation inherited from
EOObjectStore to signal to the parent object store that the cached
values for the objects identified by _globalID_s
should no longer be considered valid and that they should be refaulted.
Invokes [processRecentChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3qojxwgzltonjgky3fnz2eg2dbnztwk4y) before
refaulting the objects. This message is propagated to any underlying
object store, resulting in a refetch the next time the objects are
accessed. Any related (child or peer) object stores are notified
that the objects are no longer valid. All uncommitted changed to
the objects are lost. For more discussion of this topic, see the
section ["Methods for Managing the Object Graph"](EOEditingContext-3.md#apple-irauoqsbizeus).

__See
Also:__  [- invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnz3gc3djmrqxizkbnrwe6ytkmvrxi4y)

---

### invalidatesObjectsWhenFreed

`- (BOOL)invalidatesObjectsWhenFreed`

Returns YES to indicate that the receiver
clears and "booby-traps" all of the objects registered with
it when the receiver is deallocated, NO otherwise. The default is YES.
In this method, "invalidate" has a different meaning than it
does in the other __invalidate...__ methods.
For more discussion of this topic, see the method description for [setInvalidatesObjectsWhenFreed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2es3twmfwgszdborsxgt3cnjswg5dtk5ugk3sgojswkzb2).

---

### isObjectLockedWithGlobalID:editingContext:

`- (BOOL)isObjectLockedWithGlobalID:(EOGlobalID
*)globalID
editingContext:(EOEditingContext
*)anEditingContext`

Returns YES if the object identified by _globalID_ in _anEditingContext_ is
locked, NO otherwise. This method works by forwarding the message __isObjectLockedWithGlobalID:editingContext:__ to
its parent object store.

__See Also:__  [- lockObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rwwt3cnjswg5b2), [- lockObjectWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rwwt3cnjswg5cxnf2gqr3mn5rgc3cjiq5gkzdjoruw4z2dn5xhizlyoq5a),
[- locksObjectsBeforeFirstModification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rww42pmjvgky3uonbgkztpojsum2lson2e233enftgsy3boruw63q)

---

### lock

`- (void)lock`

Locks access to the receiver to prevent
other threads from accessing it. If the receiver has a [sharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tnbqxezleivsgs5djnztug33oorsxq5a),
the receiver takes a reader lock on it, as well. You should lock
an editing context when you are accessing or modifying objects managed
by the editing context. The thread-safety provided by Enterprise
Objects Framework allows one thread to be active in each EOEditingContext and
one thread to be active in each EODatabaseContext (EOAccess). In
other words, multiple threads can access and modify objects concurrently
in different editing contexts, but only one thread can access the
database at a time (to save, fetch, or fault).

This method
creates an NSAutoreleasePool that is released when __unlock__ is
called. Consequently, objects that have been autoreleased within
the scope of a __lock__/__unlock__ pair
may not be valid after the __unlock__.

> ```
> // The following code is WRONG!
> [editingContext lock];
> objects = [editingContext objectsWithFetchSpecification:fetchSpec];
> title = [[objects objectAtIndex:0] valueForKey:@"title"];
> [editingContext unlock]; NSLog(title); // WARNING: title might not be valid here.
>
> // This code is CORRECT.
> [editingContext lock];
> objects = [editingContext objectsWithFetchSpecification:fetchSpec];
> title = [[[objects objectAtIndex:0] valueForKey:@"title"] retain];
> [editingContext unlock];
> NSLog(title);
> [title release]
> ```

Similarly,
when you catch exceptions, you need to retain the local exception
before raising because the exception is in the lock's pool.

---

### lockObject:

`- (void)lockObject:(id)anObject`

Attempts to lock _anObject_ in
the external store. This method works by invoking [lockObjectWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rwwt3cnjswg5cxnf2gqr3mn5rgc3cjiq5gkzdjoruw4z2dn5xhizlyoq5a). Raises an `NSInvalidArgumentException` if
it can't find the globalID for _anObject_ to
pass to __lockObjectWithGlobalID:editingContext:__.

__See
Also:__  [- isObjectLockedWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jonhwe2tfmn2ey33dnnswiv3jorueo3dpmjqwyskehjswi2lunfxgoq3pnz2gk6duhi), [- locksObjectsBeforeFirstModification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rww42pmjvgky3uonbgkztpojsum2lson2e233enftgsy3boruw63q)

---

### lockObjectWithGlobalID:editingContext:

`- (void)lockObjectWithGlobalID:(EOGlobalID
*)globalID
editingContext:(EOEditingContext
*)anEditingContext`

Overrides the implementation inherited from
EOObjectStore to attempt to lock the object identified by _globalID_ in _anEditingContext_ in
the external store. Raises an `NSInternalInconsistencyException` if unable
to obtain the lock. This method works by forwarding the message __lockObjectWithGlobalID:editingContext:__ to
its parent object store.

__See Also:__  [- lockObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rwwt3cnjswg5b2), [- isObjectLockedWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jonhwe2tfmn2ey33dnnswiv3jorueo3dpmjqwyskehjswi2lunfxgoq3pnz2gk6duhi), [- locksObjectsBeforeFirstModification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rww42pmjvgky3uonbgkztpojsum2lson2e233enftgsy3boruw63q)

---

### locksObjectsBeforeFirstModification

`- (BOOL)locksObjectsBeforeFirstModification`

Returns YES if the receiver locks _object_ in
the external store (with [lockObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rwwt3cnjswg5b2)) the first time _object_ is modified.

__See
Also:__  [- setLocksObjectsBeforeFirstModification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2ey33dnnzu6ytkmvrxi42cmvtg64tfizuxe43ujvxwi2lgnfrwc5djn5xdu), [- isObjectLockedWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jonhwe2tfmn2ey33dnnswiv3jorueo3dpmjqwyskehjswi2lunfxgoq3pnz2gk6duhi), [- lockObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rwwt3cnjswg5b2), [- lockObjectWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rwwt3cnjswg5cxnf2gqr3mn5rgc3cjiq5gkzdjoruw4z2dn5xhizlyoq5a)

---

### messageHandler

`- (id)messageHandler`

Returns the EOEditingContext's message handler.
A message handler is a special-purpose delegate responsible for
presenting errors to the user. Typically, an EODisplayGroup (EOInterface)
registers itself as the message handler for its EOEditingContext.
For more information, see the [EOMessageHandlers](EOMessageHandlers.md#apple-ijdusrciinbek) informal
protocol specification.

__See Also:__  [- setMessageHandler:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2e2zltonqwozkimfxgi3dfoi5a)

---

### objectForGlobalID:

`- (id)objectForGlobalID:(EOGlobalID
*)globalID`

Returns the object identified by _globalID_,
or nil if no object has been registered in the EOEditingContext
(or its [sharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tnbqxezleivsgs5djnztug33oorsxq5a))
with _globalID_.

__See
Also:__  [- globalIDForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3hnrxweylmjfcem33sj5rguzldoq5a)

---

### objectsForSourceGlobalID:relationshipName:editingContext:

`- (NSArray *)objectsForSourceGlobalID:(EOGlobalID
*)globalID
relationshipName:(NSString *)name
editingContext:(EOEditingContext
*)anEditingContext`

Overrides the implementation inherited from
EOObjectStore to service a to-many fault for a relationship named _name_.
When a parent EOEditingContext receives a __objectsForSourceGlobalID:relationshipName:editingContext:__ message
on behalf of a child editing context and _globalID_ matches an
object instantiated in the parent, the parent returns a copy of
its relationship array and translates its objects into the child
editing context. This ensures that a child editing context "inherits"
modified values from its parent. If the receiving editing context
does not have the specified object or if the parent's relationship
property is still a fault, the request is fowarded to its parent
object store.

---

### objectsWithFetchSpecification:

`- (NSArray *)objectsWithFetchSpecification:(EOFetchSpecification
*)fetchSpecification`

Invokes [objectsWithFetchSpecification:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3pmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4otfmruxi2lom5bw63tumv4hioq) with `self` as
the EOEditingContext and returns the result.

---

### objectsWithFetchSpecification:editingContext:

`- (NSArray *)objectsWithFetchSpecification:(EOFetchSpecification
*)fetchSpecification
editingContext:(EOEditingContext
*)anEditingContext`

Overrides the implementation inherited
from EOObjectStore to fetch objects from an external store according
to the criteria specified by _fetchSpecification_ and
return them in an array. If one of these objects is already present
in memory, this method doesn't overwrite its values with the new
values from the database. This method raises an exception if an
error occurs; the error message indicates the nature of the problem.

When
an EOEditingContext receives this message, it forwards the message
to its root object store. Typically the root object store is an
EOObjectStoreCoordinator with underlying EODatabaseContexts. In
this case, the object store coordinator forwards the request to
the appropriate database context based on the entity name in _fetchSpecification_.
The database context then obtains an EODatabaseChannel and performs
the fetch, registering all fetched objects in _anEditingContext_ or
in the receiver if _anEditingContext_ isn't
provided. (Note that EODatabaseContext and EODatabaseChannel are
defined in EOAccess.)

---

### objectWillChange:

`- (void)objectWillChange:(id)object`

This method is automatically invoked when any
of the objects registered in the receiver invokes its [willChange](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf53ws3dminugc3thmu) method. This method is
EOEditingContext's implementation of the EOObserving protocol.

---

### parentObjectStore

`- (EOObjectStore *)parentObjectStore`

Returns the EOObjectStore from which the receiver
fetches and to which it saves objects.

---

### processRecentChanges

`- (void)processRecentChanges`

Forces the receiver to process pending insertions,
deletions, and updates.Normally,
when objects are changed, the processing of the changes is deferred
until the end of the current event. At that point, an EOEditingContext
moves objects to the inserted, updated, and deleted lists, delete
propagation is performed, undos are registered, and [EOObjectsChangedInStoreNotification](#apple-ijeuirceifbuu) and [EOObjectsChangedInEditingContextNotification](#apple-ijeuiq2gjbeem) are
posted. You can use this method to explicitly force changes to be
processed. An EOEditingContext automatically invokes this method
on itself before performing certain operations such as [saveChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmf3gkq3imfxgozlt).

---

### propagatesDeletesAtEndOfEvent

`- (BOOL)propagatesDeletesAtEndOfEvent`

Returns YES if the receiver propagates deletes
at the end of the event in which a change was made, NO if it propagates
deletes only right before saving changes. The default is YES.

__See
Also:__  [- setPropagatesDeletesAtEndOfEvent:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2fa4tpobqwoylumvzuizlmmv2gk42borcw4zcpmzcxmzlooq5a)

---

### recordObject:globalID:

`- (void)recordObject:(id)object
globalID:(EOGlobalID *)globalID`

Makes the receiver aware of an object identified
by _globalID_ existing in its parent
object store. EOObjectStores (such as the access layer's EODatabaseContext)
usually invoke this method for each object fetched. When it receives
this message, the receiver enters the object in its uniquing table
and registers itself as an observer of the object.

---

### redo:

`- (void)redo:(id)sender`

Sends [editingContextWillSaveChanges:](EOEditors.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi33somxwkzdjoruw4z2dn5xhizlyorlws3dmknqxmzkdnbqw4z3fom5a) messages
to the receiver's [editors](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3fmruxi33som),
and sends a __redo__ message to the receiver's
NSUndoManager, asking it to reverse the latest undo operation applied
to objects in the object graph.

__See
Also:__  [- undo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3vnzsg6oq)

---

### refault:

`- (void)refault:(id)sender`

Sends [editingContextWillSaveChanges:](EOEditors.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi33somxwkzdjoruw4z2dn5xhizlyorlws3dmknqxmzkdnbqw4z3fom5a) messages
to the receiver's [editors](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3fmruxi33som),
and invokes __refaultObjects__.

---

### refaultObject:withGlobalID:editingContext:

`- (void)refaultObject:(id)anObject
withGlobalID:(EOGlobalID *)globalID
editingContext:(EOEditingContext
*)anEditingContext`

Overrides the implementation inherited
from EOObjectStore to refault the enterprise object _object_ identified
by _globalID_ in _anEditingContext_.
This method should be used with caution since refaulting an object
does not remove the object snapshot from the undo stack. Objects
that have been newly inserted or deleted should not be refaulted.

The
main purpose of this method is to break retain cycles between enterprise
objects. This means that you might still need to break retain cycles
to help keep your application's memory in check. For example,
suppose you have an Employee object that has a to-one relationship
to its Department, and the Department object in turn has an array
of Employee objects. You can use this method to break the retain cycle.
Note that retain cycles are automatically broken if the EOEditingContext
is finalized. For more discussion of this topic, see the section ["Methods for Managing the Object Graph"](EOEditingContext-3.md#apple-irauoqsbizeus).

---

### refaultObjects

`- (void)refaultObjects`

Refaults all objects cached in the receiver
that haven't been inserted, deleted, or updated. Invokes [processRecentChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3qojxwgzltonjgky3fnz2eg2dbnztwk4y),
then invokes [refaultObject:withGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvtgc5lmorhwe2tfmn2du53jorueo3dpmjqwyskehjswi2lunfxgoq3pnz2gk6duhi) for
all objects that haven't been inserted, deleted, or updated. For
more discussion of this topic, see the section ["Methods for Managing the Object Graph"](EOEditingContext-3.md#apple-irauoqsbizeus) in
the class description.

---

### refetch:

`- (void)refetch:(id)sender`

Sends [editingContextWillSaveChanges:](EOEditors.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi33somxwkzdjoruw4z2dn5xhizlyorlws3dmknqxmzkdnbqw4z3fom5a) messages
to the receiver's [editors](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3fmruxi33som),
and invokes the [invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnz3gc3djmrqxizkbnrwe6ytkmvrxi4y)method.

---

### registeredObjects

`- (NSArray *)registeredObjects`

Returns the enterprise objects managed by the
receiver.

---

### removeEditor:

`- (void)removeEditor:(id)editor`

Unregisters _editor_ from
the receiver. For more discussion of EOEditors, see the [editors](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3fmruxi33som) method description
and the [EOEditors](EOEditors.md#apple-inbecrckindee) informal protocol specification.

__See
Also:__  [- addEditor:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3bmrsekzdjorxxeoq)

---

### reset

`- (void)reset`

Forgets all objects and makes them unusable.
If [instancesRetainRegisteredObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhukzdjoruw4z2dn5xhizlyoqxws3ttorqw4y3fonjgk5dbnfxfezlhnfzxizlsmvse6ytkmvrxi4y) is YES,
an invocation of this method is necessary to get the editing context
to release all of its registered objects. This method also resets
the [fetchTimestamp](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3gmv2gg2cunfwwk43umfwxa) as
if the editing context were just initialized.

---

### revert

`- (void)revert`

Removes everything from the undo stack,
discards all insertions and deletions, and restores updated objects
to their last committed values. Does not refetch from the database.
Note that __revert__ doesn't automatically
cause higher level display groups (WebObject's WODisplayGroups
or the interface layer's EODisplayGroups) to refetch. Display
groups that allow insertion and deletion of objects need to be explicitly
synchronized whenever this method is invoked on their EOEditingContext.

__See
Also:__  [- invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnz3gc3djmrqxizkbnrwe6ytkmvrxi4y)

---

### revert:

`- (void)revert:(id)sender`

Sends [editingContextWillSaveChanges:](EOEditors.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi33somxwkzdjoruw4z2dn5xhizlyorlws3dmknqxmzkdnbqw4z3fom5a) messages
to the receiver's [editors](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3fmruxi33som),
and invokes revert.

---

### rootObjectStore

`- (EOObjectStore *)rootObjectStore`

Returns the EOObjectStore at the base of the
object store hierarchy (usually an EOObjectStoreCoordinator).

---

### saveChanges

`- (void)saveChanges`

Sends [editingContextWillSaveChanges:](EOEditors.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi33somxwkzdjoruw4z2dn5xhizlyorlws3dmknqxmzkdnbqw4z3fom5a) messages
to the receiver's [editors](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3fmruxi33som),
and commits changes made in the receiver to its parent EOObjectStore
by sending it the message [saveChangesInEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmf3gkq3imfxgozltjfxekzdjoruw4z2dn5xhizlyoq5a).
If the parent is an EOObjectStoreCoordinator, it guides its EOCooperatingObjectStores,
typically EODatabaseContexts, through a multi-pass save operation
(see the EOObjectStoreCoordinator class specification for more information).
If a database error occurs, an exception is raised. The error message indicates
the nature of the problem.

---

### saveChanges:

`- (void)saveChanges:(id)sender`

This action method invokes [saveChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmf3gkq3imfxgozlt), handling
an exception by passing it to the message handler. For example,
if a validation error occurs, the message handler (usually an EODisplayGroup)
presents an alert panel with the text of the validation exception.

__See
Also:__  [- editingContext:presentErrorMessage:](EOMessageHandlers.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2nmvzxgylhmvegc3tenrsxe4zpmvsgs5djnztug33oorsxq5b2obzgk43fnz2ek4tsn5ze2zltonqwozj2)(EOMessageHandlers), [- editingContext:shouldPresentException:](EOEditingContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi2lom5bw63tumv4hiicemvwgkz3borss6zlenf2gs3thinxw45dfpb2du43in52wyzcqojsxgzloorcxqy3fob2gs33ohi) (EOEditingContext
Delegate)

---

### saveChangesInEditingContext:

`- (void)saveChangesInEditingContext:(EOEditingContext
*)anEditingContext`

Overrides the implementation inherited from
EOObjectStore to tell the receiver's EOObjectStore to accept changes
from a child EOEditingContext. This method shouldn't be invoked
directly. It's invoked by a nested EOEditingContext when it's
committing changes to a parent EOEditingContext. The receiving parent
EOEditingContext incorporates all changes from the nested EOEditingContext
into its own copies of the objects, but it doesn't immediately
save those changes to the database. If the parent itself is later
sent [saveChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmf3gkq3imfxgozlt),
it propagates any changes received from the child along with any
other changes to its parent EOObjectStore. Raises an exception if
an error occurs; the error message indicates the nature of the problem.

---

### setDelegate:

`- (void)setDelegate:(id)anObject`

Set the receiver's delegate to be _anObject_,
without retaining it.

__See Also:__  [- delegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3emvwgkz3borsq)

---

### setFetchTimestamp:

`- (void)setFetchTimestamp:(NSTimeInterval)timestamp`

Sets the receiver's fetch timestamp. When
an editing context fetches objects from its parent object store, the
parent object store can use the timestamp to determine whether to
use cached data or to refetch the most current values. An editing
context prefers that fetched values are at least as recent as its
fetch timestamp. Note that the parent object store is free to ignore
the timestamp; so this value should be considered a hint or request
and not a guarantee.

|  |
| --- |
| __Note:__ Changing the fetch timestamp has no effect on existing objects in the editing context; it can affect only subsequent fetches. To refresh existing objects, invoke __refaultObjects__ before you invoke __setFetchTimestamp:__. |

The initial value for the fetch timestamp of a new
non-nested editing context is the current time less the __defaultFetchTimestampLag__.
A nested editing context always uses its parent's fetch timestamp. __setFetchTimestamp:__ raises
if it's invoked on a nested editing context.

---

### setSharedEditingContext:

`- (void)setSharedEditingContext:(EOSharedEditingContext
*)sharedEC`

Sets the receiver's shared editing context.
Raises if the receiver and _sharedEC_ both
contain the same object (otherwise object uniquing would be violated)
or if _sharedEC_ is not an instance
of the EOSharedEditingContext class.By default, an editing context
that has no shared editing context listens for [EODefaultSharedEditingContextWasInitializedNotification](EOSharedEditingContext-2.md#apple-ijeuirkbjbduc)s.
If a notification is posted while the context has no registered
objects, the editing context sets its shared editing context to
the newly initialized default shared editing context.
Invoke this method with nil to remove the receiver
as an observer of this notification and to prevent the context from
accessing any objects in the default shared editing context.

---

### setInvalidatesObjectsWhenFreed:

`- (void)setInvalidatesObjectsWhenFreed:(BOOL)flag`

Sets according to _flag_ whether
the receiver clears and "booby-traps" all of the objects registered
with it when the receiver is deallocated. If an editing context
invalidates objects when it's deallocated, it sends a [clearProperties](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5rwyzlbojihe33qmvzhi2lfom) message to all of
its objects, thereby breaking any retain cycles between objects that
would prevent them from being deallocated. This method leaves the
objects in a state in which sending them any message other than
dealloc or release raises an exception.

The default
is YES, and as a general rule, this setting must be YES for enterprise
objects with cyclic references to be freed when their EOEditingContext
is freed.

Note that the word "invalidate" in this
method name has a different meaning than it does in the other __invalidate...__ methods,
which discard object values and refault them.

__See
Also:__  [- invalidatesObjectsWhenFreed](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnz3gc3djmrqxizltj5rguzldorzvo2dfnzdhezlfmq)

---

### setLocksObjectsBeforeFirstModification:

`- (void)setLocksObjectsBeforeFirstModification:(BOOL)flag`

Sets according to _flag_ whether
the receiver locks _object_ in the
external store (with [lockObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rwwt3cnjswg5b2))
the first time _object_ is modified.
The default is NO. If _flag_ is YES,
an exception will be raised if a lock can't be obtained when _object_ invokes [willChange](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf53ws3dminugc3thmu). There are two reasons
a lock might fail: because the row is already locked in the server,
or because your snapshot is out of date. If your snapshot is out
of date, you can explicitly refetch the object using an EOFetchSpecification
with [setRefreshesRefetchedObjects:](EOFetchSpecification-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forjgkztsmvzwqzltkjswmzlumnugkzcpmjvgky3uom5a) set to YES.
To handle the exception, you can implement the EODatabaseContext
delegate method __databaseContextShouldRaiseExceptionForLockFailure:__.

You
should avoid using this method or pessimistic locking in an interactive
end-user application. For example, a user might make a change in
a text field and neglect to save it, thereby leaving the data locked
in the server indefinitely. Consider using optimistic locking or
application level explicit check-in/check-out instead.

__See
Also:__  [- locksObjectsBeforeFirstModification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rww42pmjvgky3uonbgkztpojsum2lson2e233enftgsy3boruw63q)

---

### setMessageHandler:

`- (void)setMessageHandler:(id)handler`

Set the receiver's message handler to be _handler_.

__See
Also:__  [- messageHandler](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3nmvzxgylhmvegc3tenrsxe)

---

### setPropagatesDeletesAtEndOfEvent:

`- (void)setPropagatesDeletesAtEndOfEvent:(BOOL)flag`

Sets according to _flag_ whether
the receiver propagates deletes at the end of the event in which
a change was made, or only just before saving changes.

If _flag_ is YES,
deleting an enterprise object triggers delete propagation at the
end of the event in which the deletion occurred (this is the default
behavior). If _flag_ is NO, delete
propagation isn't performed until [saveChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmf3gkq3imfxgozlt) is invoked.

You
can delete enterprise objects explicitly by using the [deleteObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3emvwgk5dfj5rguzldoq5a) method
or implicitly by removing the enterprise object from an owning relationship.
Delete propagation uses the delete rules in the EOClassDescription
to determine whether objects related to the deleted object should
also be deleted (for more information, see the [EOClassDescription](EOClassDescription-3.md#apple-ivhug3dbonzuizltmnzgs4dunfxw4) class
specification and the [EOEnterpriseObject](EOEnterpriseObject-3.md#apple-ijaueqsdjbfeq) interface
informal protocol specification). If delete propagation fails (that
is, if an enterprise object refuses to be deleted-possibly due
to a deny rule), all changes made during the event are rolled back.

__See
Also:__  [- propagatesDeletesAtEndOfEvent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3qojxxaylhmf2gk42emvwgk5dfonaxirlomrhwmrlwmvxhi)

---

### setStopsValidationAfterFirstError:

`- (void)setStopsValidationAfterFirstError:(BOOL)flag`

Sets according to _flag_ whether
the receiver stops validating after the first error is encountered,
or continues for all objects (validation typically occurs during
a save operation). The default is YES. Setting it to NO is useful
if the delegate implements [editingContext:shouldPresentException:](EOEditingContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi2lom5bw63tumv4hiicemvwgkz3borss6zlenf2gs3thinxw45dfpb2du43in52wyzcqojsxgzloorcxqy3fob2gs33ohi) to
handle the presentation of aggregate exceptions.

__See
Also:__  [- stopsValidationAfterFirstError](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3torxxa42wmfwgszdboruw63sbmz2gk4sgnfzhg5cfojzg64q)

---

### setUndoManager:

`- (void)setUndoManager:(NSUndoManager
*)undoManager`

Sets the receiver's NSUndoManager to _undoManager_.
You might invoke this method with nil if your application doesn't
need undo and you want to avoid the overhead of an undo stack. For
more information on editing context's undo support, see the section ["Undo and Redo"](EOEditingContext-3.md#apple-irauoq2eivcuo).

__See
Also:__  [- undoManager](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3vnzsg6tlbnzqwozls)

---

### sharedEditingContext

`- (EOSharedEditingContext *)sharedEditingContext`

Returns the shared editing context used by
the receiver.

---

### stopsValidationAfterFirstError

`- (BOOL)stopsValidationAfterFirstError`

Returns YES to indicate that the receiver should
stop validating after it encounters the first error, or NO to indicate
that it should continue for all objects.

__See
Also:__  [- setStopsValidationAfterFirstError:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2fg5dpobzvmylmnfsgc5djn5xecztumvzem2lson2ek4tsn5zdu)

---

### tryToSaveChanges

`- (NSException *)tryToSaveChanges`

Invokes the [saveChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmf3gkq3imfxgozlt) method, and catches and
returns any exceptions that are raised.

---

### undo:

`- (void)undo:(id)sender`

Sends [editingContextWillSaveChanges:](EOEditors.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi33somxwkzdjoruw4z2dn5xhizlyorlws3dmknqxmzkdnbqw4z3fom5a) messages
to the receiver's [editors](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3fmruxi33som),
and sends an undo message to the receiver's NSUndoManager, asking
it to reverse the latest uncommitted changes applied to objects
in the object graph. For more information on editing context's
undo support, see the section ["Undo and Redo"](EOEditingContext-3.md#apple-irauoq2eivcuo).

__See
Also:__  [redo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvsg6oq)

---

### undoManager

`- (NSUndoManager *)undoManager`

Returns the receiver's NSUndoManager.

__See
Also:__  [- setUndoManager:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2fk3ten5gwc3tbm5sxeoq)

---

### unlock

`- (void)unlock`

Unlocks access to the receiver so that
other threads may access it. If the receiver has a [sharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tnbqxezleivsgs5djnztug33oorsxq5a),
the receiver unlocks a reader lock on the shared context.

__See
Also:__  [- lock](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3mn5rww)

---

### updatedObjects

`- (NSArray *)updatedObjects`

Returns the objects in the receiver's object
graph that have been updated.

__See Also:__  [- deletedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3emvwgk5dfmrhwe2tfmn2hg), [- insertedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnzzwk4tumvse6ytkmvrxi4y)

---

## Notifications

---

The following notifications are declared (except where otherwise
noted) and posted by EOEditingContext.

### EOEditingContextDidSaveChangesNotification

This notification is broadcast after changes
are saved to the EOEditingContext's parent EOObjectStore. The
notification contains:

**Notification Object**
: The EOEditingContext

**userInfo**
: A dictionary with the following keys (constants defined
in EOObjectStore.h) and values

|  |  |
| --- | --- |
| __Key__ | __Value__ |
| [EOUpdatedKey](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#CBJBJFDJ) | An NSArray containing the changed objects |
| [EOInsertedKey](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#CBJHEEDI) | An NSArray containing the inserted objects |
| [EODeletedKey](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#CBJFFHFB) | An NSArray containing the deleted objects |

### EOInvalidatedAllObjectsInStoreNotification

This notification is defined by EOObjectStore.
When posted by an EOEditingContext, it's the result of the editing
context invalidating all its objects. When an EOEditingContext receives
an `EOInvalidatedAllObjectsInStoreNotification` from
its parent EOObjectStore, it clears its lists of inserted, updated,
and deleted objects, and resets its undo stack. The notification
contains:

|  |  |
| --- | --- |
| Notification Object | The EOEditingContext |
| userInfo Dictionary | None. |

An interface layer EODisplayGroup (not a WebObjects
WODisplayGroup) listens for this notification to refetch its contents.
See the EOObjectStore class specification for more information on
this notification.

### EOObjectsChangedInStoreNotification

This notification is defined by EOObjectStore.
When posted by an EOEditingContext, it's the result of the editing
context processing [objectWillChange:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3pmjvgky3uk5uwy3cdnbqw4z3fhi) observer
notifications in [processRecentChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3qojxwgzltonjgky3fnz2eg2dbnztwk4y), which
is usually as the end of the event in which the changes occurred.
See the EOObjectStore class specification for more information on `EOObjectsChangedInStoreNotification`.

This
notification contains:

**Notification Object**
: The EOEditingContext

**userInfo**
: A dictionary with the following keys (constants defined
in EOObjectStore.h) and values

|  |  |
| --- | --- |
| __Key__ | __Value__ |
| [EOUpdatedKey](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#CBJBJFDJ) | An NSArray of EOGlobalIDs for objects whose properties have changed. A receiving EOEditingContext typically responds by refaulting the objects. |
| [EOInsertedKey](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#CBJHEEDI) | An NSArray of EOGlobalIDs for objects that have been inserted into the EOObjectStore. |
| [EODeletedKey](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#CBJFFHFB) | An NSArray of EOGlobalIDs for objects that have been deleted from the EOObjectStore. |
| [EOInvalidatedKey](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#CBJIEFEE) | An NSArray of EOGlobalIDs for objects that have been turned into faults. Invalidated objects are those for which the cached view should no longer be trusted. Invalidated objects should be refaulted so that they are refetched when they're next examined. |

### EOObjectsChangedInEditingContextNotification

`EOCONTROL_EXTERN NSString *EOObjectsChangedInEditingContextNotification`

This notification is broadcast whenever
changes are made in an EOEditingContext. It's similar to `EOObjectsChangedInStoreNotification`,
except that it contains objects rather than globalIDs. The notification
contains:

**Notification
Object**
: The EOEditingContext

**userInfo**
: A dictionary with the following keys (constants defined
in EOObjectStore.h) and values

|  |  |
| --- | --- |
| __Key__ | __Value__ |
| [EOUpdatedKey](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#CBJBJFDJ) | An NSArray containing the changed objects |
| [EODeletedKey](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#CBJFFHFB) | An NSArray containing the deleted objects |
| [EOInsertedKey](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#CBJHEEDI) | An NSArray containing the inserted objects |
| [EOInvalidatedKey](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#CBJIEFEE) | An NSArray containing invalidated objects. |

Interface layer EODisplayGroups (not WebObjects WODisplayGroups)
listen for this notification to redisplay their contents.

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
