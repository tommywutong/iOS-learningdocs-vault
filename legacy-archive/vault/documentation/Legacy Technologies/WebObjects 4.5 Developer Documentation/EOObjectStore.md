---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOObjectStore.html
archived_at: '2026-07-15T08:11:37.809053Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOObjectStore

> **__Inherits from:__**
> : (com.apple.client.eocontrol) Object
>
> (com.apple.yellow.eocontrol) NSObject

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Class Description

---

EOObjectStore is the abstract class that defines the API for
an "intelligent" repository of objects, the control layer's
object storage abstraction. An object store is responsible for constructing
and registering objects, servicing object faults, and saving changes
made to objects. For more information on the object storage abstraction,
see ["Object Storage Abstraction"](The%20EOControl%20Framework.md#apple-ijeucq2bjffek) in the introduction to
the EOControl Framework.

EOEditingContext is the principal EOObjectStore subclass and
is used for managing objects in memory-in fact, the primary purpose
of the EOObjectStore class is to define an API for servicing editing
contexts, not to define a completely general API. Other subclasses
of EOObjectStore are:

- [EOCooperatingObjectStore](EOCooperatingObjectStore.md#apple-ivhug33pobsxeylunfxgot3cnjswg5ctorxxezi)
- [EOObjectStoreCoordinator](EOObjectStoreCoordinator.md#apple-ivhu6ytkmvrxiu3un5zgkq3pn5zgi2lomf2g64q)
- EODatabaseContext (EOAccess)

A subclass of EOObjectStore must implement all of its methods.
The default implementations simply throw exceptions.

## Constants

---

EOObjectStore defines the following String constants to be
used as keys in the notifications it posts:

- DeletedKey
- InsertedKey
- InvalidatedKey
- UpdatedKey

Additionally, EOObjectStore defines String constants for the
names of the notifications it posts. See the section ["Notifications"](#apple-infeiq2jifces) for more information on the notifications.

## Method Types

---

> **Initializing objects**
> : [initializeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxws3tjoruwc3djpjsu6ytkmvrxi)
>
> **Getting objects**
> : [objectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxw6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny)
> : [objectsForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxw6ytkmvrxi42gn5zfg33vojrwkr3mn5rgc3cjiq)
>
> **Getting faults**
> : [faultForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxwmylvnr2em33si5wg6ytbnreui)
> : [arrayFaultWithSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxwc4tsmf4umylvnr2fo2lunbjw65lsmnsuo3dpmjqwyske)
> : [refaultObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxxezlgmf2wy5cpmjvgky3u)
> : [faultForRawRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxwmylvnr2em33skjqxoutpo4)
>
> **Locking objects**
> : [lockObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxwy33dnnhwe2tfmn2fo2lunbdwy33cmfwesra)
> : [isObjectLockedWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxws42pmjvgky3ujrxwg23fmrlws5dii5wg6ytbnreui)
>
> **Saving changes to objects**
> : [saveChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxxgylwmvbwqylom5sxgsloivsgs5djnztug33oorsxq5a)
>
> **Invalidating and forgetting
> objects**
> : [invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxws3twmfwgszdborsuc3dmj5rguzldorzq)
> : [invalidateObjectsWithGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxws3twmfwgszdborsu6ytkmvrxi42xnf2gqr3mn5rgc3cjirzq)
> : [editingContextDidForgetObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxwkzdjoruw4z2dn5xhizlyorcgszcgn5zgozluj5rguzldorlws5dii5wg6ytbnreui)
>
> **Interacting with the
> server**
> : [invokeRemoteMethod](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxws3twn5vwkutfnvxxizknmv2gq33e) (com.apple.client.eocontrol only)

## Instance Methods

---

### arrayFaultWithSourceGlobalID

`public abstract NSArray arrayFaultWithSourceGlobalID(
EOGlobalID globalID,
String relationshipName,
EOEditingContext anEditingContext)`

Implemented by subclasses to return the destination
objects for a to-many relationship, whether as real instances or
as faults (empty enterprise objects). _globalID_ identifies
the source object for the relationship (which doesn't necessarily
exist in memory yet), and _relationshipName_ is
the name of the relationship. The object identified by _globalID_ and
the destination objects for the relationship all belong to _anEditingContext._

If
you implement this method to return a fault, you must define an
EOFaultHandler subclass that stores _globalID_ and _relationshipName,_
using them to fetch the objects in a later [objectsForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxw6ytkmvrxi42gn5zfg33vojrwkr3mn5rgc3cjiq) message
and that turns the fault into an array containing those objects.
See the [EOFaultHandler](EOFaultHandler.md#apple-ivhumylvnr2eqylomrwgk4q) class specification for
more information on faults.

See the [EOEditingContext](EOEditingContext.md#apple-ivhukzdjoruw4z2dn5xhizlyoq) and EODatabaseContext
(EOAccess) class specifications for more information on how this
method works in concrete subclasses.

__See
Also:__  [faultForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxwmylvnr2em33si5wg6ytbnreui)

---

### editingContextDidForgetObjectWithGlobalID

`public void editingContextDidForgetObjectWithGlobalID(
EOEditingContext context,
EOGlobalID gid)`

Invoked to inform the object store that it can
stop keeping data about an object it passed to a child. Don't invoke
this method; it is invoked automatically by the Framework.

---

### faultForGlobalID

`public abstract EOEnterpriseObject faultForGlobalID(
EOGlobalID globalID,
EOEditingContext anEditingContext)`

If the receiver is _anEditingContext_ and
the object associated with _globalID_ is
already registered in _anEditingContext,_
this method returns that object. Otherwise it creates a to-one fault,
registers it in _anEditingContext,_
and returns the fault. This method is always directed first at _anEditingContext,_ which
forwards the message to its parent object store if needed to create
a fault.

If you implement this method to return a fault (an empty
enterprise object), you must define an EOFaultHandler subclass that
stores _globalID,_ uses it to fetch
the object's data, and initializes the object with EOObjectStore's [initializeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxws3tjoruwc3djpjsu6ytkmvrxi). See the [EOFaultHandler](EOFaultHandler.md#apple-ivhumylvnr2eqylomrwgk4q) class specification for
more information on faults.

See the [EOEditingContext](EOEditingContext.md#apple-ivhukzdjoruw4z2dn5xhizlyoq) and EODatabaseContext
(EOAccess) class specifications for more information on how this
method works in concrete subclasses.

__See
Also:__  [arrayFaultWithSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxwc4tsmf4umylvnr2fo2lunbjw65lsmnsuo3dpmjqwyske), [recordObject](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojswg33smrhwe2tfmn2a) ( [EOEditingContext](EOEditingContext.md#apple-ivhukzdjoruw4z2dn5xhizlyoq))

---

### faultForRawRow

`public abstract EOEnterpriseObject faultForRawRow(
NSDictionary row,
String entityName,
EOEditingContext anEOEditingContext)`

Returns a fault for the enterprise object
corresponding to _row,_ which is a
dictionary of values containing at least the primary key of the
corresponding enterprise object. This is especially useful if you
have fetched raw rows and now want a unique enterprise object.

---

### initializeObject

`public abstract void initializeObject(
EOEnterpriseObject anObject,
EOGlobalID globalID,
EOEditingContext anEditingContext)`

Implemented by subclasses to set _anObject_'s
properties, as obtained for _globalID._
This method is typically invoked after _anObject_ has
been created using EOClassDescription's [createInstanceWithEditingContext](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwg4tfmf2gksloon2gc3tdmvlws5diivsgs5djnztug33oorsxq5a) or
using EOGenericRecord's or EOCustomObject's constructors. This
method is also invoked after a fault has been fired.

__See
Also:__  [awakeFromInsertion](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc53bnnsum4tpnvew443foj2gs33o) ( [EOEnterpriseObject](EOEnterpriseObject.md#apple-ijaueqsdjbfeq)), [awakeFromFetch](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc53bnnsum4tpnvdgk5ddna) ( [EOEnterpriseObject](EOEnterpriseObject.md#apple-ijaueqsdjbfeq))

---

### invalidateAllObjects

`public abstract void invalidateAllObjects()`

Discards the values of all objects held by the
receiver and turns them into faults (empty enterprise objects).
This causes all locks to be dropped and any transaction to be rolled
back. The next time any object is accessed, its data is fetched
anew. Any child object stores are also notified that the objects
are no longer valid. See the [EOEditingContext](EOEditingContext.md#apple-ivhukzdjoruw4z2dn5xhizlyoq) class specification
for more information on how this method works in concrete subclasses.

This
method should also post an [InvalidatedAllObjectsInStoreNotification](#apple-infeirkdjbdue).

__See
Also:__  [invalidateObjectsWithGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxws3twmfwgszdborsu6ytkmvrxi42xnf2gqr3mn5rgc3cjirzq), [refaultObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxxezlgmf2wy5cpmjvgky3u)

---

### invalidateObjectsWithGlobalIDs

`public abstract void invalidateObjectsWithGlobalIDs(NSArray globalIDs)`

Signals that the objects identified by the EOGlobalIDs
in _globalIDs_ should no longer be
considered valid and that they should be turned into faults (empty
enterprise objects). This causes data for each object to be refetched
the next time it's accessed. Any child object stores are also
notified that the objects are no longer valid.

__See
Also:__  [invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxws3twmfwgszdborsuc3dmj5rguzldorzq), [refaultObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxxezlgmf2wy5cpmjvgky3u)

---

### invokeRemoteMethod

`public abstract void invokeRemoteMethod(
EOEditingContext anEditingContext,
EOGlobalID receiverGID,
String methodName,
Object[] arguments)`

(com.apple.client.eocontrol only) Invokes _methodName_ on
the enterprise object identified by _receiverGID_ in _anEditingContext,_ using _arguments._
To pass an enterprise object as an argument, use its global ID. This
method has the side effect of saving all the changes from the editing
context all the way down to the editing context in the server session.

---

### isObjectLockedWithGlobalID

`public abstract boolean isObjectLockedWithGlobalID(
EOGlobalID globalID,
EOEditingContext anEditingContext)`

Returns true if the object identified by _globalID_ is
locked, false if it isn't. See the EODatabaseContext (EOAccess)
class specification for more information on how this method works
in concrete subclasses.

---

### lockObjectWithGlobalID

`public abstract void lockObjectWithGlobalID(
EOGlobalID globalID,
EOEditingContext anEditingContext)`

Locks the object identified by _globalID._
See the EODatabaseContext (EOAccess) class specification for more
information on how this method works in concrete subclasses.

---

### objectsForSourceGlobalID

`public abstract NSArray objectsForSourceGlobalID(
EOGlobalID globalID,
String relationshipName,
EOEditingContext anEditingContext)`

Returns the destination objects for a to-many
relationship. This method is used by an array fault previously constructed
using [arrayFaultWithSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxwc4tsmf4umylvnr2fo2lunbjw65lsmnsuo3dpmjqwyske). _globalID_ identifies
the source object for the relationship (which doesn't necessarily
exist in memory yet), and _relationshipName_ is
the name of the relationship. The object identified by _globalID_ and
the destination objects for the relationship all belong to _anEditingContext._

See
the [EOEditingContext](EOEditingContext.md#apple-ivhukzdjoruw4z2dn5xhizlyoq) and EODatabaseContext
(EOAccess) class specifications for more information on how this
method works in concrete subclasses.

---

### objectsWithFetchSpecification

`public abstract NSArray objectsWithFetchSpecification(
EOFetchSpecification aFetchSpecification,
EOEditingContext anEditingContext)`

Fetches objects from an external store according
to the criteria specified by _fetchSpecification_ and returns
them in an array for inclusion in _anEditingContext._
If one of these objects is already present in memory, this method
doesn't overwrite its values with the new values from the database. Throws an exception
if an error occurs.

See the [EOEditingContext](EOEditingContext.md#apple-ivhukzdjoruw4z2dn5xhizlyoq) and EODatabaseContext
(EOAccess) class specifications for more information on how this
method works in concrete subclasses.

---

### refaultObject

`public abstract void refaultObject(
EOEnterpriseObject anObject,
EOGlobalID globalID,
EOEditingContext anEditingContext)`

Turns _anObject_ into
a fault (an empty enterprise object), identified by _globalID_ in _anEditingContext._ Objects
that have been inserted but not saved, or that have been deleted,
shouldn't be refaulted. When using com.apple.yellow.eocontrol,
use this method with caution since refaulting an object doesn't remove
the object snapshot from the undo stack.

---

### saveChangesInEditingContext

`public abstract void saveChangesInEditingContext(EOEditingContext anEditingContext)`

Saves any changes in _anEditingContext_ to
the receiver's repository. Sends [insertedObjects](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhgzlsorswit3cnjswg5dt), [deletedObjects](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmrswyzlumvse6ytkmvrxi4y), and [updatedObjects](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpovygiylumvse6ytkmvrxi4y) messages to _anEditingContext_ and
applies the changes to the receiver's data repository as appropriate.
For example, EODatabaseContext (EOAccess) implements this method
to send operations to an EOAdaptor (EOAccess) for making the changes
in a database.

---

## Notifications

---

### InvalidatedAllObjectsInStoreNotification

`public static final String InvalidatedAllObjectsInStoreNotification`

Posted whenever an EOObjectStore receives
an [invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxws3twmfwgszdborsuc3dmj5rguzldorzq) message.
The notification contains:

|  |  |
| --- | --- |
| Notification Object | The EOObjectStore that received the [invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxws3twmfwgszdborsuc3dmj5rguzldorzq) message. |
| Userinfo | None |

### ObjectsChangedInStoreNotification

`public static final String ObjectsChangedInStoreNotification`

Posted whenever an EOObjectStore observes
changes to its objects. The notification contains:

**Notification Object**
: The EOObjectStore that observed the change

**userInfo**
: A dictionary containing the following keys and values:

|  |  |
| --- | --- |
| __Key__ | __Value__ |
| [UpdatedKey](#apple-inbeuqskizceu) | An NSArray of EOGlobalIDs for objects whose properties have changed. A receiving EOEditingContext typically responds by refaulting its corresponding objects. |
| [InsertedKey](#apple-inbeuscfivces) | An NSArray of EOGlobalIDs for objects that have been inserted into the EOObjectStore. |
| [DeletedKey](#apple-inbeursgjbdee) | An NSArray of EOGlobalIDs for objects that have been deleted from the EOObjectStore. |
| [InvalidatedKey](#apple-inbeuskfizcuk) | An NSArray of EOGlobalIDs for objects that have been turned into faults. |

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
