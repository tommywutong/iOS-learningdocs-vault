---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EODatabaseChannel.html
archived_at: '2026-07-15T08:13:41.423524Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EODatabaseChannel

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.eoaccess

---

## Class Description

---

An EODatabaseChannel represents an independent communication channel to the database server. It's associated with an EODatabaseContext and an EODatabase, which, together with the EODatabaseChannel, form the __database level__ of Enterprise Objects Framework's access layer. See the EODatabase class specification for more information.

An EODatabaseChannel has an EOAdaptorChannel that it uses to connect to the database server its EODatabase object represents. An EODatabaseChannel fetches database records as instances of enterprise object classes that are specified in its EODatabase's EOModel objects. An EODatabaseChannel also has an EODatabaseContext, which uses the channel to perform fetches and to lock rows in the database. All of the database level objects are used automatically by EOEditingContexts and other components of Enterprise Objects Framework. You rarely need to interact with them directly. In particular, you wouldn't ordinarily use an EODatabaseChannel to fetch objects. Rather, you'd use an EOEditingContext.

## Method Types

---

> **Constructors**
> : [EODatabaseChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5cu6rdborqweyltmvbwqylonzswy)
>
> **Accessing cooperating objects**
> : [adaptorChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5qwiylqorxxeq3imfxg4zlm): [databaseContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5sgc5dbmjqxgzkdn5xhizlyoq)
>
> **Fetching objects**
> : [selectObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny): [isFetchInProgress](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5uxgrtforrwqslokbzg6z3smvzxg): [fetchObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5tgk5ddnbhwe2tfmn2a): [cancelFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5rwc3tdmvwemzlumnua)
>
> **Accessing internal fetch state**
> : [setCurrentEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk5cdovzhezloorcw45djor4q): [setCurrentEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk5cdovzhezloorcwi2lunfxgoq3pnz2gk6du): [setIsLocking](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk5cjongg6y3lnfxgo): [isLocking](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5uxgtdpmnvws3th): [setIsRefreshingObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk5cjonjgkztsmvzwq2lom5hwe2tfmn2hg): [isRefreshingObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5uxgutfmzzgk43infxgot3cnjswg5dt)

## Constructors

---

### EODatabaseChannel

`public EODatabaseChannel(EODatabaseContext aDatabaseContext)`

Creates and returns a new EODatabaseChannel. Typically, you don't need to programmatically create EODatabaseChannel objects. Rather, they are created automatically by the control layer. See the EODatabase class description for more information.

_aDatabaseContext_ is assigned to the new EODatabaseChannel as the DatabaseContext in which the channel works. The new EODatabaseChannel creates an AdaptorChannel with which to communicate with the database server. The constructor throws an exception if the underlying adaptor context can't create a corresponding adaptor channel.

__See Also:__ [databaseContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5sgc5dbmjqxgzkdn5xhizlyoq), [adaptorChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5qwiylqorxxeq3imfxg4zlm)

---

## Instance Methods

---

### adaptorChannel

`public EOAdaptorChannel adaptorChannel()`

Returns the EOAdaptorChannel used by the receiver for communication with the database server.

__See Also:__ [EODatabaseChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5cu6rdborqweyltmvbwqylonzswy) constructor

---

### cancelFetch

`public void cancelFetch()`

Cancels any fetch in progress.

__See Also:__ [isFetchInProgress](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5uxgrtforrwqslokbzg6z3smvzxg), [selectObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny), [fetchObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5tgk5ddnbhwe2tfmn2a)

---

### databaseContext

`public EODatabaseContext databaseContext()`

Returns the EODatabaseContext that controls transactions for the receiver.

__See Also:__ [EODatabaseChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5cu6rdborqweyltmvbwqylonzswy) constructor

---

### fetchObject

`public Object fetchObject()`

Fetches and returns the next object in the result set produced by a [selectObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny) message; returns null if there are no more objects in the current result set or if an error occurs. This method uses the receiver's EOAdaptorChannel to fetch a row, records a snapshot with the EODatabaseContext if necessary, and creates an enterprise object from the row if a corresponding object doesn't already exist. The new object is sent an __awakeFromFetch__ message to allow it to finish setting up its state.

If no snapshot exists for the fetched object, the receiver sends its EODatabase a recordSnapshotForGlobalID message to record one. If a snapshot already exists (because the object was previously fetched), the receiver checks whether it should overwrite the old snapshot with the new one. It does so by asking the delegate with a databaseContextShouldUpdateCurrentSnapshot method. If the delegate doesn't respond to this method, the EODatabaseChannel overwrites the snapshot if it's locking or refreshing fetched objects. Further, if the EODatabaseChannel is refreshing fetched objects, it posts an ObjectsChangedInStoreNotification on behalf of its EODatabaseContext (which causes any EOEditingContext using that EODatabaseContext to update its enterprise object with the values recorded in the new snapshot).

For information on locking and update strategies, see the EODatabaseContext class specification. For information on refreshing fetched objects, see the EOFetchSpecification class specification.

Ordinarily, you don't directly use an EODatabaseChannel to fetch objects. Rather, you use an EOEditingContext, which uses an underlying EODatabaseChannel to do its work.

__See Also:__ [cancelFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5rwc3tdmvwemzlumnua), [isFetchInProgress](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5uxgrtforrwqslokbzg6z3smvzxg), [isLocking](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5uxgtdpmnvws3th), [isRefreshingObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5uxgutfmzzgk43infxgot3cnjswg5dt)

---

### isFetchInProgress

`public boolean isFetchInProgress()`

Returns true if the receiver is fetching, false otherwise. An EODatabaseChannel is fetching if it's been sent a successful [selectObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny) message. An EODatabaseChannel stops fetching when there are no more objects to fetch or when it is sent a [cancelFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5rwc3tdmvwemzlumnua) message.

---

### isLocking

`public boolean isLocking()`

Returns true if the receiver is locking the objects selected, as determined by its EODatabaseContext's update strategy or the EOFetchSpecification used to perform the select. Returns false otherwise. This method always returns false when no fetch is in progress.

__See Also:__ __locksObjects__ (EOFetchSpecification)

---

### isRefreshingObjects

`public boolean isRefreshingObjects()`

Returns true if the receiver overwrites existing snapshots with fetched values and causes the current EOEditingContext to overwrite existing enterprise objects with those values as well. Returns false otherwise. This behavior is controlled by the EOFetchSpecification used in a [selectObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny) message.

__See Also:__ __refreshesRefetchedObjects__ (EOFetchSpecification), [fetchObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5tgk5ddnbhwe2tfmn2a)

---

### selectObjectsWithFetchSpecification

`public void selectObjectsWithFetchSpecification( com.webobjects.eocontrol.EOFetchSpecification fetchSpecification, com.webobjects.eocontrol.EOEditingContext anEditingContext)`

Selects objects described by _fetchSpecification_ so that they'll be fetched into _anEditingContext_. The selected objects compose one or more result sets, each object of which will be returned by subsequent [fetchObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5tgk5ddnbhwe2tfmn2a) messages in the order prescribed by _fetchSpecification_'s EOSortOrderings.

Throws an exception if an error occurs; the particular exception depends on the specific error, and is indicated in the exception's description. Some possible reasons for failure are:

- _fetchSpecification_ is invalid.
- The receiver's EODatabaseContext has no transaction in progress.
- The delegate disallows the select operation.
- The receiver's EOAdaptorChannel fails to perform the select operation.

This method invokes the delegate methods databaseContextShouldSelectObjects, databaseContextShouldUsePessimisticLock, and databaseContextDidSelectObjects. See their descriptions in the EODatabaseContext class specification for more information.

You wouldn't ordinarily invoke this method directly; rather, you'd use an EOEditingContext to select and fetch enterprise objects.

__See Also:__ [fetchObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5tgk5ddnbhwe2tfmn2a)

---

### setCurrentEditingContext

`public void setCurrentEditingContext(com.webobjects.eocontrol.EOEditingContext anEditingContext)`

Sets the EOEditingContext that's made the owner of fetched objects to _anEditingContext_. This method is automatically invoked by [selectObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny). You should never invoke it directly.

__See Also:__ [setCurrentEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk5cdovzhezloorcw45djor4q)

---

### setCurrentEntity

`public void setCurrentEntity(EOEntity anEntity)`

Sets the EOEntity used when fetching enterprise objects to _anEntity_. Subsequent [fetchObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5tgk5ddnbhwe2tfmn2a) messages during a fetch operation create an object of the class associated with _anEntity_. This method is invoked automatically by [selectObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny).You should never need to invoke it directly.

__See Also:__ [setCurrentEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk5cdovzhezloorcwi2lunfxgoq3pnz2gk6du)

---

### setIsLocking

`public void setIsLocking(boolean flag)`

Records whether the receiver locks the records it selects. A EODatabaseChannel modifies its interaction with the database server and its snapshotting behavior based on this setting. If _flag_ is true the EODatabaseChannel modifies its fetching behavior to lock objects; if _flag_ is false it simply fetches them.

An EODatabaseChannel automatically sets this flag according to the fetch specification used in a [selectObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny) message. You might invoke this method directly if evaluating SQL directly with EOAdaptorChannel's evaluateExpression method.

__See Also:__ __locksObjects__ (EOFetchSpecification)

---

### setIsRefreshingObjects

`public void setIsRefreshingObjects(boolean flag)`

Records whether the receiver causes existing snapshots and enterprise objects to be overwritten with fetched values. If _flag_ is true the receiver overwrites existing snapshots with fetched values and posts an ObjectsChangedInStoreNotification on behalf of its EODatabaseContext (which typically causes the an existing object's EOEditingContext to replace its values with the new ones). If _flag_ is false, the receiver relies on the delegate to determine whether snapshots should be overwritten, and doesn't cause enterprise objects to be overwritten.

An EODatabaseChannel automatically sets this flag according to the fetch specification used in a [selectObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3imfxg4zlmf5zwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny) message. You might invoke this method directly if evaluating SQL directly with EOAdaptorChannel's __evaluateExpression:__ method.

__See Also:__ __refreshesRefetchedObjects__ (EOFetchSpecification)

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
