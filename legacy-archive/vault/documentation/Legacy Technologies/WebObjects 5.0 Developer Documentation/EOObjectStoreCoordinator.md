---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOObjectStoreCoordinator.html
archived_at: '2026-07-15T08:13:47.127375Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOObjectStoreCoordinator

> **__Inherits from:__**
> : [EOObjectStore](EOObjectStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhu6ytkmvrxiu3un5zgk)

> **__Implements:__**
> : NSDisposable

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

EOObjectStoreCoordinator is a part of the control layer's object storage abstraction. An EOObjectStoreCoordinator object acts as a single object store by directing one or more EOCooperatingObjectStores in managing objects from distinct data repositories.

For more general information on the object storage abstraction, see "Object Storage Abstraction" (page 23) in the introduction to the EOControl Framework.

## EOObjectStore Methods

EOObjectStoreCoordinator overrides the following EOObjectStore methods:

- objectsWithFetchSpecification
- objectsForSourceGlobalID
- faultForGlobalID
- arrayFaultWithSourceGlobalID
- refaultObject
- [saveChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc643bozsug2dbnztwk42jnzcwi2lunfxgoq3pnz2gk6du)
- invalidateAllObjects
- invalidateObjectsWithGlobalIDs:

With the exception of __saveChangesInEditingContext__, EOObjectStoreCoordinator's implementation of these methods simply forwards the message to an EOCooperatingObjectStore or stores. The message __invalidateAllObjects__ is forwarded to all of a coordinator's cooperating stores. The rest of the messages are forwarded to the appropriate store based on which store responds true to the messages ownsGlobalID, ownsObject, and handlesFetchSpecification (which message is used depends on the context). The EOObjectStore methods listed above aren't documented in this class specification (except for __saveChangesInEditingContext__)-for descriptions of them, see the EOObjectStore and EODatabaseContext (EOAccess) class specifications

For the method [saveChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc643bozsug2dbnztwk42jnzcwi2lunfxgoq3pnz2gk6du), the coordinator guides its cooperating stores through a multi-pass save protocol in which each cooperating store saves its own changes and forwards remaining changes to the other of the coordinator's stores. For example, if in its recordChangesInEditingContext method one cooperating store notices the removal of an object from an "owning" relationship but that object belongs to another cooperating store, it informs the other store by sending the coordinator a [forwardUpdateForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6ztpoj3wc4tekvygiylumvdg64spmjvgky3u) message. For a more details, see the method description for [saveChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc643bozsug2dbnztwk42jnzcwi2lunfxgoq3pnz2gk6du).

Although it manages objects from multiple repositories, EOObjectStoreCoordinator doesn't absolutely guarantee consistent updates when saving changes across object stores. If your application requires guaranteed distributed transactions, you can either provide your own solution by creating a subclass of EOObjectStoreCoordinator that integrates with a TP monitor, use a database server with built-in distributed transaction support, or design your application to write to only one object store per save operation (though it may read from multiple object stores). For more discussion of this subject, see the method description for __saveChangesInEditingContext__.

## Constants

---

EOObjectStoreCoordinator defines String constants for the notifications it posts. For more information, see the section ["Notifications" (page 296)](#apple-ijeugrcdivduk).

## Method Types

---

> **Constructors**
> : [EOObjectStoreCoordinator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6rkpj5rguzldorjxi33smvbw633smruw4ylun5za)
>
> **Setting the default coordinator**
> : [setDefaultCoordinator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3cnjswg5ctorxxezkdn5xxezdjnzqxi33sf5zwk5cemvtgc5lmorbw633smruw4ylun5za): [defaultCoordinator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3cnjswg5ctorxxezkdn5xxezdjnzqxi33sf5sgkztbovwhiq3pn5zgi2lomf2g64q)
>
> **Managing EOCooperatingObjectStores**
> : [addCooperatingObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6ylemrbw633qmvzgc5djnztu6ytkmvrxiu3un5zgk): [removeCooperatingObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc64tfnvxxmzkdn5xxazlsmf2gs3thj5rguzldorjxi33smu): [cooperatingObjectStores](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6y3pn5ygk4tboruw4z2pmjvgky3ukn2g64tfom)
>
> **Saving changes**
> : [saveChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc643bozsug2dbnztwk42jnzcwi2lunfxgoq3pnz2gk6du)
>
> **Communication between EOCooperatingObjectStores**
> : [forwardUpdateForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6ztpoj3wc4tekvygiylumvdg64spmjvgky3u): [valuesForKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc65tbnr2wk42gn5zewzlzom)
>
> **Returning EOCooperatingObjectStores**
> : [objectStoreForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5zeo3dpmjqwyske): [objectStoreForFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5zemzlumnufg4dfmnuwm2ldmf2gs33o): [objectStoreForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5ze6ytkmvrxi)
>
> **Getting the userInfo dictionary**
> : [userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc65ltmvzes3tgn4): [setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc643forkxgzlsjfxgm3y)

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

Adds _store_ to the list of EOCooperatingObjectStores that need to be queried and notified about changes to enterprise objects. The receiver reuses its stores: they don't go away until the EOObjectStoreCoordinator is destroyed or until the stores are explicitly removed. Posts the notification [CooperatingObjectStoreWasAdded](#apple-ijeugqsjivauo).

__See Also:__ [removeCooperatingObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc64tfnvxxmzkdn5xxazlsmf2gs3thj5rguzldorjxi33smu), [cooperatingObjectStores](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6y3pn5ygk4tboruw4z2pmjvgky3ukn2g64tfom)

---

### arrayFaultWithSourceGlobalID

`public NSArray arrayFaultWithSourceGlobalID( EOGlobalID anEOGlobalID, String aString, EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### cooperatingObjectStores

`public NSArray cooperatingObjectStores()`

Returns the receiver's EOCooperatingObjectStores.

__See Also:__ [addCooperatingObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6ylemrbw633qmvzgc5djnztu6ytkmvrxiu3un5zgk), [removeCooperatingObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc64tfnvxxmzkdn5xxazlsmf2gs3thj5rguzldorjxi33smu)

---

### dispose

`public void dispose()`

Conformance to NSDisposable.

---

### editingContextDidForgetObjectWithGlobalID

`public void editingContextDidForgetObjectWithGlobalID( EOEditingContext anEOEditingContext, EOGlobalID anEOGlobalID)`

Description forthcoming.

---

### faultForGlobalID

`public EOEnterpriseObject faultForGlobalID( EOGlobalID anEOGlobalID, EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### faultForRawRow

`public EOEnterpriseObject faultForRawRow( NSDictionary aNSDictionary, String aString, EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### forwardUpdateForObject

`public void forwardUpdateForObject( EOEnterpriseObject object, NSDictionary changes)`

Tells the receiver to forward a message from an EOCooperatingObjectStore to another store, informing it that _changes_ need to be made to _object_. For example, inserting an object in a relationship property of one EOCooperatingObjectStore might require changing a foreign key property in an object owned by another EOCooperatingObjectStore.

This method first locates the EOCooperatingObjectStore that's responsible for applying _changes_, and then it sends the store the message recordUpdateForObject.

---

### initializeObject

`public void initializeObject( EOEnterpriseObject anEOEnterpriseObject, EOGlobalID anEOGlobalID, EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### invalidateAllObjects

`public void invalidateAllObjects()`

Description forthcoming.

---

### invalidateObjectsWithGlobalIDs

`public void invalidateObjectsWithGlobalIDs(NSArray aNSArray)`

Description forthcoming.

---

### isObjectLockedWithGlobalID

`public boolean isObjectLockedWithGlobalID( EOGlobalID anEOGlobalID, EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### lockObjectWithGlobalID

`public void lockObjectWithGlobalID( EOGlobalID anEOGlobalID, EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### objectsForSourceGlobalID

`public NSArray objectsForSourceGlobalID( EOGlobalID anEOGlobalID, String aString, EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### objectsWithFetchSpecification

`public NSArray objectsWithFetchSpecification( EOFetchSpecification anEOFetchSpecification, EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### refaultObject

`public void refaultObject( EOEnterpriseObject anEOEnterpriseObject, EOGlobalID anEOGlobalID, EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### objectStoreForFetchSpecification

`public EOCooperatingObjectStore objectStoreForFetchSpecification(EOFetchSpecification fetchSpecification)`

Returns the EOCooperatingObjectStore responsible for fetching objects with _fetchSpecification_. Returns null if no EOCooperatingObjectStore can be found that responds true to handlesFetchSpecification.

__See Also:__ [objectStoreForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5zeo3dpmjqwyske), [objectStoreForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5ze6ytkmvrxi)

---

### objectStoreForGlobalID

`public EOCooperatingObjectStore objectStoreForGlobalID(EOGlobalID globalID)`

Returns the EOCooperatingObjectStore for the object identified by _globalID_. Returns null if no EOCooperatingObjectStore can be found that responds true to ownsGlobalID.

__See Also:__ [objectStoreForFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5zemzlumnufg4dfmnuwm2ldmf2gs33o), [objectStoreForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5ze6ytkmvrxi)

---

### objectStoreForObject

`public EOCooperatingObjectStore objectStoreForObject(Object object)`

Returns the EOCooperatingObjectStore that owns _object_. Returns null if no EOCooperatingObjectStore can be found that responds true to ownsObject.

__See Also:__ [objectStoreForFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5zemzlumnufg4dfmnuwm2ldmf2gs33o), [objectStoreForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc633cnjswg5ctorxxezkgn5zeo3dpmjqwyske)

---

### objectsForSourceGlobalID

`public NSArray objectsForSourceGlobalID( EOGlobalID anEOGlobalID, String aString, EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### objectsWithFetchSpecification

`public NSArray objectsWithFetchSpecification( EOFetchSpecification anEOFetchSpecification, EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### refaultObject

`public void refaultObject( EOEnterpriseObject anEOEnterpriseObject, EOGlobalID anEOGlobalID, EOEditingContext anEOEditingContext)`

Description forthcoming.

---

### removeCooperatingObjectStore

`public void removeCooperatingObjectStore(EOCooperatingObjectStore store)`

Removes _store_ from the list of EOCooperatingObjectStores that need to be queried and notified about changes to enterprise objects. Posts the notification [CooperatingObjectStoreWasRemoved](#apple-ijeugqsbjjauu).

__See Also:__ [addCooperatingObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6ylemrbw633qmvzgc5djnztu6ytkmvrxiu3un5zgk), [cooperatingObjectStores](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6y3pn5ygk4tboruw4z2pmjvgky3ukn2g64tfom)

---

### saveChangesInEditingContext

`public void saveChangesInEditingContext(EOEditingContext anEditingContext)`

Overrides the EOObjectStore implementation to save the changes made in _anEditingContext_. This message is sent by an EOEditingContext to an EOObjectStoreCoordinator to commit changes. When an EOObjectStoreCoordinator receives this message, it guides its EOCooperatingObjectStores through a multi-pass save protocol in which each EOCooperatingObjectStore saves its own changes and forwards remaining changes to other EOCooperatingObjectStores. When this method is invoked, the following sequence of events occurs:

1. The receiver sends each of its EOCooperatingObjectStores the message prepareForSaveWithCoordinator, which informs them that a multi-pass save operation is beginning. When the EOCooperatingObjectStore is an EODatabaseContext (EOAccess), it takes this opportunity to generate primary keys for any new objects in the EOEditingContext.
2. The receiver sends each of its EOCooperatingObjectStores the message recordChangesInEditingContext, which prompts them to examine the changed objects in the editing context, record operations that need to be performed, and notify the receiver of any changes that need to be forwarded to other stores. For example, if in its __recordChangesInEditingContext__ method one EOCooperatingObjectStore notices the removal of an object from an "owning" relationship but that object belongs to another EOCooperatingObjectStore, it informs the other store by sending the coordinator a [forwardUpdateForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6ztpoj3wc4tekvygiylumvdg64spmjvgky3u) message.
3. The receiver sends each of its EOCooperatingObjectStores the message ownsGlobalID. This tells the stores to transmit their changes to their underlying databases. When the EOCooperatingObjectStore is an EODatabaseContext, it responds to this message by taking the EODatabaseOperations (EOAccess) that were constructed in the previous step, constructing EOAdaptorOperations (EOAccess) from them, and giving the EOAdaptorOperations to an available EOAdaptorChannel (EOAccess) for execution.
4. If __ownsGlobalID__ fails for any of the EOCooperatingObjectStores, all stores are sent the message rollbackChanges.
5. If __ownsGlobalID__ succeeds for all EOCooperatingObjectStores, the receiver sends them the message commitChanges, which has the effect of telling the adaptor to commit the changes.
6. If __commitChanges__ fails for a particular EOCooperatingObjectStore, that store and all subsequent ones are sent the message rollbackChanges. However, the stores that have already committed their changes do not roll back. In other words, the coordinator doesn't perform the two-phase commit protocol necessary to guarantee consistent distributed update.

This method raises an exception if an error occurs.

---

### setUserInfo

`public void setUserInfo(NSDictionary dictionary)`

Sets the _dictionary_ of auxiliary data, which your application can use for whatever it needs.

__See Also:__ [userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc65ltmvzes3tgn4)

---

### userInfo

`public NSDictionary userInfo()`

Returns a dictionary of user data. Your application can use this to store any auxiliary information it needs.

__See Also:__ [setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc643forkxgzlsjfxgm3y)

---

### valuesForKeys

`public NSDictionary valuesForKeys( NSArray keys, Object object)`

Communicates with the appropriate EOCooperatingObjectStore to get the values identified by _keys_ for _object_, so that it can then forward them on to another EOCooperatingObjectStore. EOCooperatingObjectStores can hold values for an object that augment the properties in the object. For instance, an EODatabaseContext (EOAccess) stores foreign key information for the objects it owns. These foreign keys may well not be defined as properties of the object. Other EODatabaseContexts can find out the object's foreign keys by sending the EODatabaseContext that owns the object a __valuesForKeys__ message(through the coordinator).

---

## Notifications

---

The following notifications are declared and posted by EOObjectStoreCoordinator.

### CooperatingObjectStoreWasAdded

`public static final String CooperatingObjectStoreWasAdded`

When an EOObjectStoreCoordinator receives an [addCooperatingObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc6ylemrbw633qmvzgc5djnztu6ytkmvrxiu3un5zgk) message and adds an EOCooperatingObjectStore to its list, it posts `CooperatingObjectStoreWasAdded` to notify observers.

|  |  |
| --- | --- |
| Notification Object | The EOObjectStoreCoordinator |
| userInfo Dictionary | None |

### CooperatingObjectStoreWasRemoved

`public static final String CooperatingObjectStoreWasRemoved`

When an EOObjectStoreCoordinator receives a [removeCooperatingObjectStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5rguzldorjxi33smvbw633smruw4ylun5zc64tfnvxxmzkdn5xxazlsmf2gs3thj5rguzldorjxi33smu) message and removes an EOCooperatingObjectStore from its list, it posts `CooperatingObjectStoreWasRemoved` to notify observers.

|  |  |
| --- | --- |
| Notification Object | The EOObjectStoreCoordinator |
| userInfo Dictionary | None |

### CooperatingObjectStoreNeeded

`public static final String CooperatingObjectStoreNeeded`

Posted when an EOObjectStoreCoordinator receives a request that it can't service with any of its currently registered EOCooperatingObjectStores. The observer can call back to the coordinator to register an appropriate EOCooperatingObjectStore based on the information in the userInfo dictionary.

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

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
