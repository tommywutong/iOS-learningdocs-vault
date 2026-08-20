---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOSharedEditingContext.html
archived_at: '2026-07-15T08:11:40.011636Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOSharedEditingContext

> **__Inherits
> from:__**
> : [EOEditingContext](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5cwi2lunfxgoq3pnz2gk6du) : [EOObjectStore](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#//apple_ref/occ/cl/EOObjectStore) : NSObject

> __Declared in:__ : EOControl/EOSharedEditingContext.h

---

## Class Description

---

The EOSharedEditingContext class defines a
mechanism that allows EOEditingContexts to share enterprise objects
for reading. This mechanism can reduce redundant pointers and the
number of fetches an application requires.

Shared enterprise objects are read-only and persist for the
life of the application; they can't be modified or deleted. They
must be unique in the shared context and across all other editing
contexts that share objects from the shared context.

Objects can be fetched into a shared context using [objectsWithFetchSpecification:](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3pmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4oq) and [bindObjectsWithFetchSpecification:toName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpmjuw4zcpmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4otun5hgc3lfhi).
The latter method makes it easier to access result sets, using [objectsByEntityNameAndFetchSpecificationName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpn5rguzldorzue6kfnz2gs5dzjzqw2zkbnzsemzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zi).

In multithreaded applications, shared objects can be used
safely by many threads at once. Shared editing contexts use EOMultiReaderLocks
to maintain thread safety. The methods [objectsWithFetchSpecification:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpn5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63r2mvsgs5djnztug33oorsxq5b2) (and
the inherited [objectsWithFetchSpecification:](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3pmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4oq)), [bindObjectsWithFetchSpecification:toName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpmjuw4zcpmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4otun5hgc3lfhi), [faultForGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpmzqxk3duizxxer3mn5rgc3cjiq5gkzdjoruw4z2dn5xhizlyoq5a),
and [objectForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpn5rguzldordg64shnrxweylmjfcdu) are
thread-safe, but you must lock the context before using any other
shared context API.

It is possible to modify shared objects while an application
is running, but only indirectly. You can create a regular editing
context that doesn't share objects by setting it's [sharedEditingContext](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tnbqxezleivsgs5djnztug33oorsxq5a) to nil. Fetch
the object that you want to change into the regular context, modify
or delete it, and save. Since shared editing contexts listen for [EOObjectsChangedInStoreNotification](EOEditingContext-2.md#apple-ijeuirceifbuu)s,
the shared editing context updates when it learns that an object
was modified. The shared context removes from its [objectsByEntityName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpn5rguzldorzue6kfnz2gs5dzjzqw2zi) and [objectsByEntityNameAndFetchSpecificationName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpn5rguzldorzue6kfnz2gs5dzjzqw2zkbnzsemzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zi) dictionaries
any objects that have been deleted, and it refaults any objects
that have been updated. However, to register newly inserted objects
in the shared editing context, you should refetch.

## Constants

---

In EOSharedEditingContext.h, EOControl defines
constants for the notifications EOSharedEditingContexts posts. For
more information, see ["Notifications"](#apple-ijeuir2ijbauq).

## Method Types

---

> **Accessing a shared editing
> context**
> : [+ defaultSharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvg2dbojswirlenf2gs3thinxw45dfpb2c6zdfmzqxk3duknugc4tfmrcwi2lunfxgoq3pnz2gk6du)
> : [+ setDefaultSharedEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvg2dbojswirlenf2gs3thinxw45dfpb2c643forcgkztbovwhiu3imfzgkzcfmruxi2lom5bw63tumv4hioq)
> : [- sharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bponugc4tfmrcwi2lunfxgoq3pnz2gk6du)
> : [- setSharedEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bponsxiu3imfzgkzcfmruxi2lom5bw63tumv4hioq)
>
> **Accessing shared objects**
> : [- bindObjectsWithFetchSpecification:toName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpmjuw4zcpmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4otun5hgc3lfhi)
> : [- objectsByEntityName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpn5rguzldorzue6kfnz2gs5dzjzqw2zi)
> : [- objectsByEntityNameAndFetchSpecificationName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpn5rguzldorzue6kfnz2gs5dzjzqw2zkbnzsemzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zi)
> : [- objectsWithFetchSpecification:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpn5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63r2mvsgs5djnztug33oorsxq5b2)
>
> **Locking a shared editing
> context**
> : [- lockForReading](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpnrxwg22gn5zfezlbmruw4zy)
> : [- tryLockForReading](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bporzhstdpmnvum33skjswczdjnztq)
> : [- unlockForReading](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpovxgy33dnndg64ssmvqwi2lom4)
>
> **Overridden EOEditingContext
> methods**
> : [- deleteObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpmrswyzlumvhwe2tfmn2du)
> : [- deletedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpmrswyzlumvse6ytkmvrxi4y)
> : [- faultForGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpmzqxk3duizxxer3mn5rgc3cjiq5gkzdjoruw4z2dn5xhizlyoq5a)
> : [- hasChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpnbqxgq3imfxgozlt) [- insertedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpnfxhgzlsorswit3cnjswg5dt)
> : [- insertObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpnfxhgzlsorhwe2tfmn2du)
> : [- objectForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpn5rguzldordg64shnrxweylmjfcdu)
> : [- objectWillChange:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpn5rguzldorlws3dminugc3thmu5a)
> : [- refaultObject:withGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpojswmylvnr2e6ytkmvrxiotxnf2gqr3mn5rgc3cjiq5gkzdjoruw4z2dn5xhizlyoq5a)
> : [- registeredObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpojswo2ltorsxezlej5rguzldorzq)
> : [- reset](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpojsxgzlu)
> : [- saveChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bponqxmzkdnbqw4z3fom)
> : [- setUndoManager:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bponsxivlomrxu2ylomftwk4r2)
> : [- updatedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpovygiylumvse6ytkmvrxi4y)
> : [- validateChangesForSave](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpozqwy2lemf2gkq3imfxgozltizxxeu3bozsq)

## Class Methods

---

### defaultSharedEditingContext

`+ (EOSharedEditingContext *)defaultSharedEditingContext`

Returns the default EOSharedEditingContext. If
a shared context hasn't yet been created, this method creates
one and posts an [EODefaultSharedEditingContextWasInitializedNotification](#apple-ijeuirkbjbduc).

---

### setDefaultSharedEditingContext:

`+ (void)setDefaultSharedEditingContext:(EOSharedEditingContext
*)context`

Sets the default shared editing
context. If _context_ is nil,
object sharing is disabled in subsequently created EOEditingContexts.

---

## Instance Methods

---

### bindObjectsWithFetchSpecification:toName:

`- (void)bindObjectsWithFetchSpecification:(EOFetchSpecification
*)fetchSpecification
toName:(NSString *)name`

Fetches objects with _fetchSpecification_ and
binds the results to _fetchSpecification_'s
entity and _fetchSpecification_'s
name, which is provided with the _name_ argument. You
can later retrieve the resulting shared objects using the methods [objectsByEntityName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpn5rguzldorzue6kfnz2gs5dzjzqw2zi) and [objectsByEntityNameAndFetchSpecificationName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpn5rguzldorzue6kfnz2gs5dzjzqw2zkbnzsemzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zi).

---

### deleteObject:

`- (void)deleteObject:object`

Raises an exception. You
can't modify or delete the shared objects in a shared editing
context.

---

### deletedObjects

`- (NSArray *)deletedObjects`

Returns an empty array. The
shared objects in a shared editing context can't be deleted.

---

### faultForGlobalID:editingContext:

`- (id)faultForGlobalID:(EOGlobalID
*)gid
editingContext:(EOEditingContext
*)context`

A thread-safe version of the
superclass implementation.

__See
Also:__  [- faultForGlobalID:editingContext:](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3gmf2wy5cgn5zeo3dpmjqwyskehjswi2lunfxgoq3pnz2gk6duhi) ( [EOEditingContext](EOEditingContext-2.md#apple-ivhukzdjoruw4z2dn5xhizlyoq))

---

### hasChanges

`- (BOOL)hasChanges`

Returns NO. You
can't modify or delete the shared objects in a shared editing
context.

---

### insertedObjects

`- (NSArray *)insertedObjects`

Returns an empty array. You
can't insert objects into a shared editing context.

---

### insertObject:

`- (void)insertObject:object`

Raises an exception. You
can't insert objects into a shared editing context. Instead, insert
an enterprise object into a regular editing context and then fetch
it into the shared context.

---

### lockForReading

`- (void)lockForReading`

Locks the receiver for reading.

__See
Also:__  [- tryLockForReading](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bporzhstdpmnvum33skjswczdjnztq)

---

### objectForGlobalID:

`- (id)objectForGlobalID:(EOGlobalID
*)gid`

A thread-safe version of the
superclass implementation.

__See
Also:__  [- objectForGlobalID:](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3pmjvgky3uizxxer3mn5rgc3cjiq5a) ( [EOEditingContext](EOEditingContext-2.md#apple-ivhukzdjoruw4z2dn5xhizlyoq))

---

### objectsByEntityName

`- (NSDictionary *)objectsByEntityName`

Returns a dictionary of all
the objects fetched into the shared context. The
dictionary keys are entity names and the corresponding values are
NSArrays of enterprise objects for that entity.

__See
Also:__  [bindObjectsWithFetchSpecification:toName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpmjuw4zcpmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4otun5hgc3lfhi)

---

### objectsByEntityNameAndFetchSpecificationName

`- (NSDictionary *)objectsByEntityNameAndFetchSpecificationName`

Returns the objects fetched
into the receiver with [bindObjectsWithFetchSpecification:toName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpmjuw4zcpmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4otun5hgc3lfhi).
The return value is a dictionary whose keys are entity names and
whose values are subdictionaries. The keys of the subdictionaries
are fetch specification names, and the values are NSArrays of the
enterprise objects fetched with the corresponding fetch specification.
The fetch specification names are the names specified in __bindObjectsWithFetchSpecification:toName:__.
Generally these names are the same names used to identify stored
fetch specifications in EOModeler.

|  |
| --- |
| __Note:__ The dictionary returned from this method might not contain all the receiver's shared objects. It only contains objects fetched with a named fetch specification using [bindObjectsWithFetchSpecification:toName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpmjuw4zcpmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4otun5hgc3lfhi). Shared objects fetched into the receiver with other methods are not returned from this method. |

---

### objectsWithFetchSpecification:editingContext:

`- (NSArray *)objectsWithFetchSpecification:(EOFetchSpecification
*)fetchSpecification
editingContext:(EOEditingContext
*)anEditingContext`

A thread-safe version of the
superclass implementation that binds the results to _fetchSpecification_'s entity. You
can later retrieve the resulting shared objects using the method [objectsByEntityName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tnbqxezleivsgs5djnztug33oorsxq5bpn5rguzldorzue6kfnz2gs5dzjzqw2zi).

__See
Also:__  [- objectsWithFetchSpecification:editingContext:](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3pmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4otfmruxi2lom5bw63tumv4hioq) ( [EOEditingContext](EOEditingContext-2.md#apple-ivhukzdjoruw4z2dn5xhizlyoq))

---

### objectWillChange:

`- (void)objectWillChange:object`

Raises an exception. You
can't modify the shared objects in a shared editing context.

---

### refaultObject:withGlobalID:editingContext:

`- (void)refaultObject:object
withGlobalID:(EOGlobalID *)gid
editingContext:(EOEditingContext
*)context`

See the [refaultObject:withGlobalID:editingContext:](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvtgc5lmorhwe2tfmn2du53jorueo3dpmjqwyskehjswi2lunfxgoq3pnz2gk6duhi) method
description in the [EOEditingContext](EOEditingContext-2.md#apple-ivhukzdjoruw4z2dn5xhizlyoq) class specification. Note
that this method is not thread safe.

---

### registeredObjects

`- (NSArray *)registeredObjects`

A thread-safe version of the
superclass implementation.

__See
Also:__  [- registeredObjects](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smvtws43umvzgkzcpmjvgky3uom) ( [EOEditingContext](EOEditingContext-2.md#apple-ivhukzdjoruw4z2dn5xhizlyoq))

---

### reset

`- (void)reset`

Overrides the superclass implementation
to do nothing.

---

### saveChanges

`- (void)saveChanges`

Raises an exception. You
can't modify the shared objects in a shared editing context.

---

### setSharedEditingContext:

`- (void)setSharedEditingContext:(EOSharedEditingContext
*)sharedEC`

Raises an exception unless _sharedEC_ is nil.

---

### setUndoManager:

`- (void)setUndoManager:(NSUndoManager
*)undoManager`

Raises an exception unless _undoManager_ is nil.

---

### sharedEditingContext

`- (EOSharedEditingContext *)sharedEditingContext`

Returns nil.

---

### tryLockForReading

`- (BOOL)tryLockForReading`

Tries to lock the receiver
for reading. Returns YES if the receiver is successfully locked, NO otherwise.

---

### unlockForReading

`- (void)unlockForReading`

Unlocks the receiver for reading.

---

### updatedObjects

`- (NSArray *)updatedObjects`

Returns an empty array. You
can't modify objects that are in a shared editing context.

---

### validateChangesForSave

`- (void)validateChangesForSave`

Overrides the superclass implementation
to do nothing.

---

## Notifications

---

### EODefaultSharedEditingContextWasInitializedNotification

`EOCONTROL_EXTERN NSString *EODefaultSharedEditingContextWasInitializedNotification`

Posted when an
EOSharedEditingContext is created and assigned as the [defaultSharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvg2dbojswirlenf2gs3thinxw45dfpb2c6zdfmzqxk3duknugc4tfmrcwi2lunfxgoq3pnz2gk6du).

|  |  |
| --- | --- |
| Notification Object | None |
| userInfo Dictionary | None |

### EOSharedEditingContextInitializedObjectsNotification

`EOCONTROL_EXTERN NSString *EOSharedEditingContextInitializedObjectsNotification`

Posted when new
objects are added to a shared editing context (by fetching or fault
firing).

|  |  |
| --- | --- |
| Notification Object | The shared editing context |
| userInfo Dictionary | NSArray of global IDs of the initialized objects |

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
