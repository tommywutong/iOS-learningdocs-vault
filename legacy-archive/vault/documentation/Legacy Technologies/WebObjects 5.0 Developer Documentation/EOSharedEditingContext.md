---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOSharedEditingContext.html
archived_at: '2026-07-15T08:13:47.346945Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

# EOSharedEditingContext

> **__Inherits from:__**
> : [EOEditingContext](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhukzdjoruw4z2dn5xhizlyoq) : [EOObjectStore](EOObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhu6ytkmvrxiu3un5zgk)

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

The EOSharedEditingContext class defines a mechanism that allows EOEditingContexts to share enterprise objects for reading. This mechanism can reduce redundant data and the number of fetches an application requires.

Shared enterprise objects are read-only and persist for the life of the application; they can't be modified or deleted. They must be unique in the shared context and across all other editing contexts that share objects from the shared context.

Objects can be fetched into a shared context using [objectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5xwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33o) and [bindObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5rgs3tej5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63q). The latter method makes it easier to access result sets, using [objectsByEntityNameAndFetchSpecificationName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5xwe2tfmn2hgqtzivxhi2lupfhgc3lfifxgirtforrwqu3qmvrwsztjmnqxi2lpnzhgc3lf).

In multithreaded applications, shared objects can be used safely by many threads at once. Shared editing contexts use EOMultiReaderLocks to maintain thread safety. The methods [objectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5xwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33o) [bindObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5rgs3tej5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63q), [faultForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5tgc5lmordg64shnrxweylmjfca), and [objectForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5xwe2tfmn2em33si5wg6ytbnreui) are thread-safe, but you must lock the context before using any other shared context API.

It is possible to modify shared objects while an application is running, but only indirectly. You can create a regular editing context that doesn't share objects by setting it's sharedEditingContext to null. Fetch the object that you want to change into the regular context, modify or delete it, and save. Since shared editing contexts listen for ObjectsChangedInStoreNotifications, the shared editing context updates when it learns that an object was modified. The shared context removes from its [objectsByEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5xwe2tfmn2hgqtzivxhi2lupfhgc3lf) and [objectsByEntityNameAndFetchSpecificationName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5xwe2tfmn2hgqtzivxhi2lupfhgc3lfifxgirtforrwqu3qmvrwsztjmnqxi2lpnzhgc3lf) dictionaries any objects that have been deleted, and it refaults any objects that have been updated. However, to register newly inserted objects in the shared editing context, you should refetch.

## Constants

---

EOSharedEditingContext defines constants for the notifications it post. For more information, see ["Notifications" (page 346)](#apple-ijeuir2ijbauq).

## Method Types

---

> **Accessing a shared editing context**
> : [defaultSharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3imfzgkzcfmruxi2lom5bw63tumv4hil3emvtgc5lmorjwqylsmvsekzdjoruw4z2dn5xhizlyoq): [setDefaultSharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3imfzgkzcfmruxi2lom5bw63tumv4hil3tmv2eizlgmf2wy5ctnbqxezleivsgs5djnztug33oorsxq5a): [sharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5zwqylsmvsekzdjoruw4z2dn5xhizlyoq): [setSharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5zwk5ctnbqxezleivsgs5djnztug33oorsxq5a)
>
> **Accessing shared objects**
> : [bindObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5rgs3tej5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63q): [objectsByEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5xwe2tfmn2hgqtzivxhi2lupfhgc3lf): [objectsByEntityNameAndFetchSpecificationName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5xwe2tfmn2hgqtzivxhi2lupfhgc3lfifxgirtforrwqu3qmvrwsztjmnqxi2lpnzhgc3lf): [objectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5xwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33o)
>
> **Locking a shared editing context**
> : [lockForReading](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5wg6y3lizxxeutfmfsgs3th): [tryLockForReading](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf52he6kmn5rwwrtpojjgkylenfxgo): [unlockForReading](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf52w43dpmnvum33skjswczdjnztq)
>
> **Overridden EOEditingContext methods**
> : [deleteObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5sgk3dforsu6ytkmvrxi): [deletedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5sgk3dforswit3cnjswg5dt): [faultForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5tgc5lmordg64shnrxweylmjfca): [hasChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5ugc42dnbqw4z3fom) [insertedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5uw443foj2gkzcpmjvgky3uom): [insertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5uw443foj2e6ytkmvrxi): [objectForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5xwe2tfmn2em33si5wg6ytbnreui): [objectWillChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5xwe2tfmn2fo2lmnrbwqylom5sq): [refaultObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5zgkztbovwhit3cnjswg5a) [registeredObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5zgkz3jon2gk4tfmrhwe2tfmn2hg): [reset](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5zgk43foq): [saveChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5zwc5tfinugc3thmvzq): [setUndoManager](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5zwk5cvnzsg6tlbnzqwozls): [updatedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf52xazdborswit3cnjswg5dt): [validateChangesForSave](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf53gc3djmrqxizkdnbqw4z3fondg64stmf3gk)

## Constructors

---

### EOSharedEditingContext

`public EOSharedEditingContext(EOObjectStore anObjectStore)`

Creates a new EOSharedEditingContext object with the defaultParentObjectStore as its parent object store. _anObjectStore_ is ignored.

`public EOSharedEditingContext()`

Description forthcoming.

---

## Static Methods

---

### defaultSharedEditingContext

`public static EOSharedEditingContext defaultSharedEditingContext()`

Returns the default EOSharedEditingContext. If a shared context hasn't yet been created, this method creates one and posts a [DefaultSharedEditingContextWasInitializedNotification](#apple-ijeuirkbjbduc).

---

### setDefaultSharedEditingContext

`public static synchronized void setDefaultSharedEditingContext(EOSharedEditingContext context)`

Sets the default shared editing context. If _context_ is null, object sharing is disabled in subsequently created EOEditingContexts.

---

## Instance Methods

---

### bindObjectsWithFetchSpecification

`public void bindObjectsWithFetchSpecification( EOFetchSpecification fetchSpecification, String name)`

Fetches objects with _fetchSpecification_ and binds the results to _fetchSpecification_'s entity and _fetchSpecification_'s name, which is provided with the _name_ argument. You can later retrieve the resulting shared objects using the methods [objectsByEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5xwe2tfmn2hgqtzivxhi2lupfhgc3lf) and [objectsByEntityNameAndFetchSpecificationName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5xwe2tfmn2hgqtzivxhi2lupfhgc3lfifxgirtforrwqu3qmvrwsztjmnqxi2lpnzhgc3lf).

---

### deleteObject

`public void deleteObject(EOEnterpriseObject object)`

Raises an exception. You can't modify or delete the shared objects in a shared editing context.

---

### deletedObjects

`public NSArray deletedObjects()`

Returns an empty array. The shared objects in a shared editing context can't be deleted.

---

### __dispose__

`public void dispose()`

Description forthcoming.

---

### faultForGlobalID

`public EOEnterpriseObject faultForGlobalID( EOGlobalID gid, EOEditingContext context)`

A thread-safe version of the superclass implementation.

__See Also:__ faultForGlobalID (EOEditingContext)

---

### __forgetObject__

`public void forgetObject(EOEnterpriseObject anEO)`

Description forthcoming.

---

### __globalIDForObject__

`public EOGlobalID globalIDForObject(EOEnterpriseObject anEO)`

Description forthcoming.

---

### hasChanges

`public boolean hasChanges()`

Returns false. You can't modify or delete the shared objects in a shared editing context.

---

### __initializeObject__

`public void initializeObject( EOEnterpriseObject anEO, EOGlobalID anID, EOEditingContext aEC)`

Description forthcoming.

---

### insertedObjects

`public NSArray insertedObjects()`

Returns an empty array. You can't insert objects into a shared editing context.

---

### insertObject

`public void insertObject(EOEnterpriseObject object)`

Raises an exception. You can't insert objects into a shared editing context. Instead, insert an enterprise object into a regular editing context and then fetch it into the shared context.

---

### __insertObjectWithGlobalID__

`public void insertObjectWithGlobalID( EOEnterpriseObject anEO, EOGlobalID anID)`

Description forthcoming.

---

### __invalidateAllObjects__

`public void invalidateAllObjects()`

Description forthcoming.

---

### __invalidateObjectsWithGlobalIDs__

`public void invalidateObjectsWithGlobalIDs(NSArray arrayOfIDs)`

Description forthcoming.

---

### __lock__

`public void lock()`

Description forthcoming.

---

### lockForReading

`public void lockForReading()`

Locks the receiver for reading.

__See Also:__ [tryLockForReading](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf52he6kmn5rwwrtpojjgkylenfxgo)

---

### objectForGlobalID

`public EOEnterpriseObject objectForGlobalID(EOGlobalID gid)`

A thread-safe version of the superclass implementation.

__See Also:__ objectForGlobalID (EOEditingContext)

---

### objectsByEntityName

`public NSDictionary objectsByEntityName()`

Returns a dictionary of all the objects fetched into the shared context. The dictionary keys are entity names and the corresponding values are NSArrays of enterprise objects for that entity.

__See Also:__ [bindObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5rgs3tej5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63q)

---

### objectsByEntityNameAndFetchSpecificationName

`public NSDictionary objectsByEntityNameAndFetchSpecificationName()`

Returns the objects fetched into the receiver with [bindObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5rgs3tej5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63q). The return value is a dictionary whose keys are entity names and whose values are subdictionaries. The keys of the subdictionaries are fetch specification names, and the values are NSArrays of the enterprise objects fetched with the corresponding fetch specification. The fetch specification names are the names specified in __bindObjectsWithFetchSpecification__. Generally these names are the same names used to identify stored fetch specifications in EOModeler.

|  |
| --- |
| __Note:__ The dictionary returned from this method might not contain all the receiver's shared objects. It only contains objects fetched with a named fetch specification using [bindObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5rgs3tej5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63q). Shared objects fetched into the receiver with other methods are not returned from this method. |

---

### objectsWithFetchSpecification

`public NSArray objectsWithFetchSpecification( EOFetchSpecification fetchSpecification, EOEditingContext anEditingContext)`

A thread-safe version of the superclass implementation that binds the results to _fetchSpecification_'s entity. You can later retrieve the resulting shared objects using the method [objectsByEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5xwe2tfmn2hgqtzivxhi2lupfhgc3lf).

__See Also:__ [objectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknugc4tfmrcwi2lunfxgoq3pnz2gk6duf5xwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33o) (EOEditingContext)

---

### objectWillChange

`public void objectWillChange(Object object)`

Raises an exception. You can't modify the shared objects in a shared editing context.

---

### refaultObject

`public void refaultObject( EOEnterpriseObject object, EOGlobalID gid, EOEditingContext context)`

See the refaultObject method description in the EOEditingContext class specification. Note that this method is not thread safe.

---

### __refaultObjects__

`public void refaultObjects()`

Description forthcoming.

---

### registeredObjects

`public NSArray registeredObjects()`

A thread-safe version of the superclass implementation.

__See Also:__ registeredObjects (EOEditingContext)

---

### reset

`public void reset()`

Overrides the superclass implementation to do nothing.

---

### __retrieveReaderLocks__

`public void retrieveReaderLocks()`

Description forthcoming.

---

### saveChanges

`public void saveChanges()`

Raises an exception. You can't modify the shared objects in a shared editing context.

---

### setSharedEditingContext

`public void setSharedEditingContext(EOSharedEditingContext sharedEC)`

Raises an exception unless _sharedEC_ is null.

---

### setUndoManager

`public void setUndoManager(NSUndoManager undoManager)`

Raises an exception unless _undoManager_ is null.

---

### sharedEditingContext

`public EOSharedEditingContext sharedEditingContext()`

Returns null.

---

### __suspendReaderLocks__

`public void suspendReaderLocks()`

Description forthcoming.

---

### tryLock

`public boolean tryLock()`

Description forthcoming.

---

### tryLockForReading

`public boolean tryLockForReading()`

Tries to lock the receiver for reading. Returns true if the receiver is successfully locked, false otherwise.

---

### __unlock__

`public void unlock()`

Description forthcoming.

---

### unlockForReading

`public void unlockForReading()`

Unlocks the receiver for reading.

---

### updatedObjects

`public NSArray updatedObjects()`

Returns an empty array. You can't modify objects that are in a shared editing context.

---

### validateChangesForSave

`public void validateChangesForSave()`

Overrides the superclass implementation to do nothing.

---

## Notifications

---

### DefaultSharedEditingContextWasInitializedNotification

`public static final String DefaultSharedEditingContextWasInitializedNotification`

Posted when an EOSharedEditingContext is created and assigned as the [defaultSharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3imfzgkzcfmruxi2lom5bw63tumv4hil3emvtgc5lmorjwqylsmvsekzdjoruw4z2dn5xhizlyoq).

|  |  |
| --- | --- |
| Notification Object | None |
| userInfo Dictionary | None |

### SharedEditingContextInitializedObjectsNotification

`public static final String SharedEditingContextInitializedObjectsNotification`

Posted when new objects are added to a shared editing context (by fetching or fault firing).

|  |  |
| --- | --- |
| Notification Object | The shared editing context |
| userInfo Dictionary | NSArray of global IDs of the initialized objects |

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
