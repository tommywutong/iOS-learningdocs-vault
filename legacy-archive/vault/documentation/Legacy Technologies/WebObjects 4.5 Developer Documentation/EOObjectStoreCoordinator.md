---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOObjectStoreCoordinator.html
archived_at: '2026-07-15T08:11:37.830249Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOObjectStoreCoordinator

> **__Inherits
> from:__**
> : [EOObjectStore](EOObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhu6ytkmvrxiu3un5zgk) : NSObject

> **__Package:__**
> : com.apple.yellow.eocontrol

---

## Class Description

---

EOObjectStoreCoordinator is a part of the
control layer's object storage abstraction. An EOObjectStoreCoordinator
object acts as a single object store by directing one or more EOCooperatingObjectStores
in managing objects from distinct data repositories.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.client.eocontrol package. |

For more general information on the object storage abstraction,
see ["Object Storage Abstraction"](The%20EOControl%20Framework.md#apple-ijeucq2bjffek) in the introduction to
the EOControl Framework.

## EOObjectStore Methods

EOObjectStoreCoordinator overrides the following EOObjectStore
methods:

- [objectsWithFetchSpecification](EOObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxw6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny)
- [objectsForSourceGlobalID](EOObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxw6ytkmvrxi42gn5zfg33vojrwkr3mn5rgc3cjiq)
- [faultForGlobalID](EOObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxwmylvnr2em33si5wg6ytbnreui)
- [arrayFaultWithSourceGlobalID](EOObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxwc4tsmf4umylvnr2fo2lunbjw65lsmnsuo3dpmjqwyske)
- [refaultObject](EOObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxxezlgmf2wy5cpmjvgky3u)
- [saveChangesInEditingContext](EOObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxxgylwmvbwqylom5sxgsloivsgs5djnztug33oorsxq5a)
- [invalidateAllObjects](EOObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxws3twmfwgszdborsuc3dmj5rguzldorzq)
- [invalidateObjectsWithGlobalIDs](EOObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smuxws3twmfwgszdborsu6ytkmvrxi42xnf2gqr3mn5rgc3cjirzq)

With the exception of `saveChangesInEditingContext`,
EOObjectStoreCoordinator's implementation of these methods simply
forwards the message to an EOCooperatingObjectStore or stores. The
message `invalidateAllObjects` is forwarded
to all of a coordinator's cooperating stores. The rest of the
messages are forwarded to the appropriate store based on which store
responds true to the messages [ownsGlobalID](EOCooperatingObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64dfojtg64tninugc3thmvzq), [ownsObject](EOCooperatingObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss633xnzzu6ytkmvrxi), and [handlesFetchSpecification](EOCooperatingObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss62dbnzsgyzltizsxiy3iknygky3jmzuwgylunfxw4) (which
message is used depends on the context). The EOObjectStore methods
listed above aren't documented in this class specification (except for `saveChangesInEditingContext`)-for
descriptions of them, see the [EOObjectStore](EOObjectStore.md#apple-ivhu6ytkmvrxiu3un5zgk) and EODatabaseContext
(EOAccess) class specifications

For the method [saveChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc643bozsug2dbnztwk42jnzcwi2lunfxgoq3pnz2gk6du),
the coordinator guides its cooperating stores through a multi-pass
save protocol in which each cooperating store saves its own changes
and forwards remaining changes to the other of the coordinator's
stores. For example, if in its [recordChangesInEditingContext](EOCooperatingObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64tfmnxxezcdnbqw4z3fonew4rlenf2gs3thinxw45dfpb2a) method
one cooperating store notices the removal of an object from an "owning"
relationship but that object belongs to another cooperating store,
it informs the other store by sending the coordinator a [forwardUpdateForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6ztpoj3wc4tekvygiylumvdg64spmjvgky3u) message. For
a more details, see the method description for [saveChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc643bozsug2dbnztwk42jnzcwi2lunfxgoq3pnz2gk6du).

Although it manages objects from multiple repositories, EOObjectStoreCoordinator
doesn't absolutely guarantee consistent updates when saving changes
across object stores. If your application requires guaranteed distributed
transactions, you can either provide your own solution by creating
a subclass of EOObjectStoreCoordinator that integrates with a TP
monitor, use a database server with built-in distributed transaction
support, or design your application to write to only one object
store per save operation (though it may read from multiple object
stores). For more discussion of this subject, see the method description
for `saveChangesInEditingContext`.

## Constants

---

EOObjectStoreCoordinator defines String constants for the
notifications it posts. For more information, see the section ["Notifications"](#apple-ijeugrcdivduk).

## Method Types

---

> **Constructors**
> : [EOObjectStoreCoordinator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6rkpj5rguzldorjxi33smvbw633smruw4ylun5za)
>
> **Setting the default coordinator**
> : [setDefaultCoordinator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3cnjswg5ctorxxezkdn5xxezdjnzqxi33sf5zwk5cemvtgc5lmorbw633smruw4ylun5za)
> : [defaultCoordinator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3cnjswg5ctorxxezkdn5xxezdjnzqxi33sf5sgkztbovwhiq3pn5zgi2lomf2g64q)
>
> **Managing EOCooperatingObjectStores**
> : [addCooperatingObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6ylemrbw633qmvzgc5djnztu6ytkmvrxiu3un5zgk)
> : [removeCooperatingObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc64tfnvxxmzkdn5xxazlsmf2gs3thj5rguzldorjxi33smu)
> : [cooperatingObjectStores](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6y3pn5ygk4tboruw4z2pmjvgky3ukn2g64tfom)
>
> **Saving changes**
> : [saveChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc643bozsug2dbnztwk42jnzcwi2lunfxgoq3pnz2gk6du)
>
> **Communication between
> EOCooperatingObjectStores**
> : [forwardUpdateForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6ztpoj3wc4tekvygiylumvdg64spmjvgky3u)
> : [valuesForKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc65tbnr2wk42gn5zewzlzom)
>
> **Returning EOCooperatingObjectStores**
> : [objectStoreForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5zeo3dpmjqwyske)
> : [objectStoreForFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5zemzlumnufg4dfmnuwm2ldmf2gs33o)
> : [objectStoreForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5ze6ytkmvrxi)
>
> **Getting the userInfo
> dictionary**
> : [userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc65ltmvzes3tgn4)
> : [setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc643forkxgzlsjfxgm3y)

## Constructors

---

### EOObjectStoreCoordinator

`public EOObjectStoreCoordinator()`

Creates and returns an EOObjectStoreCoordinator.

---

## Static Methods

---

### defaultCoordinator

`public static Object defaultCoordinator()`

Returns a shared instance of EOObjectStoreCoordinator.

---

### setDefaultCoordinator

`public static void setDefaultCoordinator(EOObjectStoreCoordinator coordinator)`

Sets a shared instance EOObjectStoreCoordinator.

---

## Instance Methods

---

### addCooperatingObjectStore

`public void addCooperatingObjectStore(EOCooperatingObjectStore store)`

Adds _store_ to
the list of EOCooperatingObjectStores that need to be queried and
notified about changes to enterprise objects. The receiver reuses
its stores: they don't go away until the EOObjectStoreCoordinator
is destroyed or until the stores are explicitly removed. Posts the
notification [CooperatingObjectStoreWasAdded](#apple-ijeugqsjivauo).

__See
Also:__  [removeCooperatingObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc64tfnvxxmzkdn5xxazlsmf2gs3thj5rguzldorjxi33smu), [cooperatingObjectStores](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6y3pn5ygk4tboruw4z2pmjvgky3ukn2g64tfom)

---

### cooperatingObjectStores

`public NSArray cooperatingObjectStores()`

Returns the receiver's EOCooperatingObjectStores.

__See
Also:__  [addCooperatingObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6ylemrbw633qmvzgc5djnztu6ytkmvrxiu3un5zgk), [removeCooperatingObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc64tfnvxxmzkdn5xxazlsmf2gs3thj5rguzldorjxi33smu)

---

### forwardUpdateForObject

`public void forwardUpdateForObject(
Object object,
NSDictionary changes)`

Tells the receiver to forward a message from
an EOCooperatingObjectStore to another store, informing it that _changes_ need
to be made to _object._ For example,
inserting an object in a relationship property of one EOCooperatingObjectStore
might require changing a foreign key property in an object owned
by another EOCooperatingObjectStore.

This method first locates
the EOCooperatingObjectStore that's responsible for applying _changes,_
and then it sends the store the message [recordUpdateForObject](EOCooperatingObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64tfmnxxezcvobsgc5dfizxxet3cnjswg5a).

---

### objectStoreForFetchSpecification

`public EOCooperatingObjectStore objectStoreForFetchSpecification(EOFetchSpecification fetchSpecification)`

Returns the EOCooperatingObjectStore responsible
for fetching objects with _fetchSpecification._ Returns null if
no EOCooperatingObjectStore can be found that responds true to [handlesFetchSpecification](EOCooperatingObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss62dbnzsgyzltizsxiy3iknygky3jmzuwgylunfxw4).

__See
Also:__  [objectStoreForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5zeo3dpmjqwyske), [objectStoreForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5ze6ytkmvrxi)

---

### objectStoreForGlobalID

`public EOCooperatingObjectStore objectStoreForGlobalID(EOGlobalID globalID)`

Returns the EOCooperatingObjectStore for the
object identified by _globalID._ Returns null if
no EOCooperatingObjectStore can be found that responds true to [ownsGlobalID](EOCooperatingObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64dfojtg64tninugc3thmvzq).

__See
Also:__  [objectStoreForFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5zemzlumnufg4dfmnuwm2ldmf2gs33o), [objectStoreForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5ze6ytkmvrxi)

---

### objectStoreForObject

`public EOCooperatingObjectStore objectStoreForObject(Object object)`

Returns the EOCooperatingObjectStore that owns _object._
Returns null if no EOCooperatingObjectStore can be found that responds true to [ownsObject](EOCooperatingObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss633xnzzu6ytkmvrxi).

__See
Also:__  [objectStoreForFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5zemzlumnufg4dfmnuwm2ldmf2gs33o), [objectStoreForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5zeo3dpmjqwyske)

---

### removeCooperatingObjectStore

`public void removeCooperatingObjectStore(EOCooperatingObjectStore store)`

Removes _store_ from
the list of EOCooperatingObjectStores that need to be queried and
notified about changes to enterprise objects. Posts the notification [CooperatingObjectStoreWasRemoved](#apple-ijeugqsbjjauu).

__See
Also:__  [addCooperatingObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6ylemrbw633qmvzgc5djnztu6ytkmvrxiu3un5zgk), [cooperatingObjectStores](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6y3pn5ygk4tboruw4z2pmjvgky3ukn2g64tfom)

---

### saveChangesInEditingContext

`public void saveChangesInEditingContext(EOEditingContext anEditingContext)`

Overrides the EOObjectStore implementation to
save the changes made in _anEditingContext._
This message is sent by an EOEditingContext to an EOObjectStoreCoordinator
to commit changes. When an EOObjectStoreCoordinator receives this
message, it guides its EOCooperatingObjectStores through a multi-pass
save protocol in which each EOCooperatingObjectStore saves its own
changes and forwards remaining changes to other EOCooperatingObjectStores.
When this method is invoked, the following sequence of events occurs:

1. The receiver sends each of its EOCooperatingObjectStores the
   message [prepareForSaveWithCoordinator](EOCooperatingObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64dsmvygc4tfizxxeu3bozsvo2lunbbw633smruw4ylun5za),
   which informs them that a multi-pass save operation is beginning. When
   the EOCooperatingObjectStore is an EODatabaseContext (EOAccess),
   it takes this opportunity to generate primary keys for any new objects
   in the EOEditingContext.
2. The receiver sends each of its EOCooperatingObjectStores the
   message [recordChangesInEditingContext](EOCooperatingObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64tfmnxxezcdnbqw4z3fonew4rlenf2gs3thinxw45dfpb2a),
   which prompts them to examine the changed objects in the editing context,
   record operations that need to be performed, and notify the receiver
   of any changes that need to be forwarded to other stores. For example,
   if in its `recordChangesInEditingContext` method one
   EOCooperatingObjectStore notices the removal of an object from an
   "owning" relationship but that object belongs to another EOCooperatingObjectStore,
   it informs the other store by sending the coordinator a [forwardUpdateForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6ztpoj3wc4tekvygiylumvdg64spmjvgky3u) message.
3. The receiver sends each of its EOCooperatingObjectStores the
   message [ownsGlobalID](EOCooperatingObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64dfojtg64tninugc3thmvzq). This tells the stores
   to transmit their changes to their underlying databases. When the
   EOCooperatingObjectStore is an EODatabaseContext, it responds to
   this message by taking the EODatabaseOperations (EOAccess) that
   were constructed in the previous step, constructing EOAdaptorOperations (EOAccess)
   from them, and giving the EOAdaptorOperations to an available EOAdaptorChannel (EOAccess)
   for execution.
4. If `ownsGlobalID` fails for any of
   the EOCooperatingObjectStores, all stores are sent the message [rollbackChanges](EOCooperatingObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64tpnrwgeyldnnbwqylom5sxg).
5. If `ownsGlobalID` succeeds for all
   EOCooperatingObjectStores, the receiver sends them the message [commitChanges](EOCooperatingObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss6y3pnvwws5cdnbqw4z3fom), which has the effect
   of telling the adaptor to commit the changes.
6. If `commitChanges` fails for a particular
   EOCooperatingObjectStore, that store and all subsequent ones are
   sent the message [rollbackChanges](EOCooperatingObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw64dfojqxi2lom5hwe2tfmn2fg5dpojss64tpnrwgeyldnnbwqylom5sxg). However, the stores
   that have already committed their changes do not roll back. In other
   words, the coordinator doesn't perform the two-phase commit protocol
   necessary to guarantee consistent distributed update.

This
method raises an exception if an error occurs.

---

### setUserInfo

`public void setUserInfo(NSDictionary dictionary)`

Sets the _dictionary_ of
auxiliary data, which your application can use for whatever it needs.

__See
Also:__  [userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc65ltmvzes3tgn4)

---

### userInfo

`public NSDictionary userInfo()`

Returns a dictionary of user data. Your application
can use this to store any auxiliary information it needs.

__See
Also:__  [setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc643forkxgzlsjfxgm3y)

---

### valuesForKeys

`public NSDictionary valuesForKeys(
NSArray keys,
Object object)`

Communicates with the appropriate EOCooperatingObjectStore
to get the values identified by _keys_ for _object,_
so that it can then forward them on to another EOCooperatingObjectStore. EOCooperatingObjectStores
can hold values for an object that augment the properties in the
object. For instance, an EODatabaseContext (EOAccess) stores foreign
key information for the objects it owns. These foreign keys may
well not be defined as properties of the object. Other EODatabaseContexts
can find out the object's foreign keys by sending the EODatabaseContext
that owns the object a `valuesForKeys` message (through
the coordinator).

---

## Notifications

---

The following notifications are declared and posted by EOObjectStoreCoordinator.

### CooperatingObjectStoreWasAdded

`public static final String CooperatingObjectStoreWasAdded`

When an EOObjectStoreCoordinator
receives an [addCooperatingObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6ylemrbw633qmvzgc5djnztu6ytkmvrxiu3un5zgk) message
and adds an EOCooperatingObjectStore to its list, it posts `CooperatingObjectStoreWasAdded` to
notify observers.

|  |  |
| --- | --- |
| Notification Object | The EOObjectStoreCoordinator |
| userInfo Dictionary | None |

### CooperatingObjectStoreWasRemoved

`public static final String CooperatingObjectStoreWasRemoved`

When an EOObjectStoreCoordinator receives
a [removeCooperatingObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc64tfnvxxmzkdn5xxazlsmf2gs3thj5rguzldorjxi33smu) message
and removes an EOCooperatingObjectStore from its list, it posts `CooperatingObjectStoreWasRemoved` to
notify observers.

|  |  |
| --- | --- |
| Notification Object | The EOObjectStoreCoordinator |
| userInfo Dictionary | None |

### CooperatingObjectStoreNeeded

`public static final String CooperatingObjectStoreNeeded`

Posted when an EOObjectStoreCoordinator
receives a request that it can't service with any of its currently
registered EOCooperatingObjectStores. The observer can call back
to the coordinator to register an appropriate EOCooperatingObjectStore
based on the information in the userInfo dictionary.

**Notification Object**
: The EOObjectStoreCoordinator

**userInfo Dictionary**
: Contains the following keys and values:

|  |  |
| --- | --- |
| __Key__ | __Value__ |
| globalID | globalID for the operation |
| fetchSpecification | fetch specification for the operation |
| object | object for the operation |

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
