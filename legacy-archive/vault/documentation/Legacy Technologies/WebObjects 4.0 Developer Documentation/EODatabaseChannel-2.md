---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EODatabaseChannel.html
archived_at: '2026-07-18T01:28:15.999781Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](More%20about%20EODatabase.md)
[!](EODatabaseContext-3.md)

---

# EODatabaseChannel

__Inherits From:__
NSObject

__Declared in:__
EOAccess/EODatabaseChannel.h

---

## Class Description

An EODatabaseChannel represents an independent communication channel to the database server. It's associated with an EODatabaseContext and an EODatabase, which, together with the EODatabaseChannel, form the _database level_ of Enterprise Objects Framework's access layer. See the [EODatabase](EODatabase-3.md) class specification for more information.

An EODatabaseChannel has an [EOAdaptorChannel](EOAdaptorChannel-2.md) that it uses to connect to the database server its EODatabase object represents. An EODatabaseChannel fetches database records as instances of enterprise object classes that are specified in its EODatabase's EOModel objects. An EODatabaseChannel also has an [EODatabaseContext](EODatabaseContext-3.md), which uses the channel to perform fetches and to lock rows in the database. All of the database level objects are used automatically by EOEditingContexts and other components of Enterprise Objects Framework. You rarely need to interact with them directly. In particular, you wouldn't ordinarily use an EODatabaseChannel to fetch objects. Rather, you'd use an EOEditingContext.

---

## Method Types

**Creating instances [- initWithDatabaseContext:](#apple-g4zdony)

**Accessing cooperating objects [- adaptorChannel](#apple-giztq)****

**[- databaseContext](#apple-gi2dk)**

**Fetching objects [- selectObjectsWithFetchSpecification:editingContext:](#apple-gi3te)**

**[- isFetchInProgress](#apple-gi3dc)

**[- fetchObject](#apple-gi3tmnq)

**[- cancelFetch](#apple-gi2dc)******

**Accessing internal fetch state [- setCurrentEntity:](#apple-gi4dm)**

**[- setCurrentEditingContext:](#apple-gi4de)

**[- setIsLocking:](#apple-gi4tima)

**[- isLocking](#apple-gi3di)

**[- setIsRefreshingObjects:](#apple-gi4ts)

**[- isRefreshingObjects](#apple-gi3dq)**********

**Accessing the delegate [- setDelegate:](#apple-gi4ta)**

**[- delegate](#apple-gi2dq)**

---

## Instance Methods

---

### adaptorChannel

- (EOAdaptorChannel \*)`adaptorChannel`

Returns the EOAdaptorChannel used by the receiver for communication with the database server.

---

### cancelFetch

- (void)`cancelFetch`

Cancels any fetch in progress.

__See also:__
[- `isFetchInProgress`](#apple-gi3dc), [- `selectObjectsWithFetchSpecification:editingContext:`](#apple-gi3te), [- `fetchObject`](#apple-gi3tmnq)

---

### databaseContext

- (EODatabaseContext \*)`databaseContext`

Returns the EODatabaseContext that controls transactions for the receiver.

---

### delegate

- (id)`delegate`

Returns the receiver's delegate. An EODatabaseChannel shares the delegate of its EODatabaseContext. See the EODatabaseContext class specification for the delegate methods you can implement.

__See also:__
[- `setDelegate:`](#apple-gi4ta)

---

### fetchObject

- (id)`fetchObject`

Fetches and returns the next object in the result set produced by a `[selectObjectsWithFetchSpecification:editingContext:](#apple-gi3te)` message; returns `nil` if there are no more objects in the current result set or if an error occurs. This method uses the receiver's EOAdaptorChannel to fetch a row, records a snapshot with the EODatabaseContext if necessary, and creates an enterprise object from the row if a corresponding object doesn't already exist. The new object is sent an `awakeFromFetchInEditingContext:` message to allow it to finish setting up its state.

If no snapshot exists for the fetched object, the receiver sends its EODatabase a [`recordSnapshot:forGlobalID:`](EODatabase.md#apple-gq4tioi) message to record one. If a snapshot already exists (because the object was previously fetched), the receiver checks whether it should overwrite the old snapshot with the new one. It does so by asking the delegate with a [`databaseContext:shouldUpdateCurrentSnapshot:newSnapshot:globalID:databaseChannel:`](../Protocols/EODatabaseContextDelegate.md#apple-geydqmi) method. If the delegate doesn't respond to this method, the EODatabaseChannel overwrites the snapshot if it's locking or refreshing fetched objects. Further, if the EODatabaseChannel is refreshing fetched objects, it posts an EOObjectsChangedInStoreNotification on behalf of its EODatabaseContext (which causes any EOEditingContext using that EODatabaseContext to update its enterprise object with the values recorded in the new snapshot).

For information on locking and update strategies, see the EODatabaseContext class specification. For information on refreshing fetched objects, see the EOFetchSpecification class specification.

Ordinarily, you don't directly use an EODatabaseChannel to fetch objects. Rather, you use an EOEditingContext, which uses an underlying EODatabaseChannel to do its work.

__See also:__
[- `cancelFetch`](#apple-gi2dc), [- `isFetchInProgress`](#apple-gi3dc), [- `isLocking`](#apple-gi3di), [- `isRefreshingObjects`](#apple-gi3dq)

---

### initWithDatabaseContext:

- `initWithDatabaseContext:`(EODatabaseContext \*)_aDatabaseContext_

The designated initializer, this method initializes a newly allocated EODatabaseChannel with _aDatabaseContext_ as the EODatabaseContext in which it works. The new EODatabaseChannel retains _aDatabaseContext_, and creates an EOAdaptorChannel to communicate with the database server. Returns `self`. Raises if the underlying adaptor context can't create a corresponding adaptor channel.

Typically, you don't need to programmatically create EODatabaseChannel objects. Rather, they are created automatically by the control layer. See the EODatabase class description for more information.

---

### isFetchInProgress

- (BOOL)`isFetchInProgress`

Returns YES if the receiver is fetching, NO otherwise. An EODatabaseChannel is fetching if it's been sent a successful `[selectObjectsWithFetchSpecification:editingContext:](#apple-gi3te)` message. An EODatabaseChannel stops fetching when there are no more objects to fetch or when it is sent a `[cancelFetch](#apple-gi2dc)` message.

---

### isLocking

- (BOOL)`isLocking`

Returns YES if the receiver is locking the objects selected, as determined by its EODatabaseContext's update strategy or the EOFetchSpecification used to perform the select. Returns NO otherwise. This method always returns NO when no fetch is in progress.

__See also:__
- `locksObjects` (EOFetchSpecification), [- `setIsLocking:`](#apple-gi4tima)

---

### isRefreshingObjects

- (BOOL)`isRefreshingObjects`

Returns YES if the receiver overwrites existing snapshots with fetched values and causes the current EOEditingContext to overwrite existing enterprise objects with those values as well. Returns NO otherwise. This behavior is controlled by the EOFetchSpecification used in a [`selectObjectsWithFetchSpecification:editingContext:`](#apple-gi3te) message.

__See also:__
- `refreshesRefetchedObjects` (EOFetchSpecification), [- `fetchObject`](#apple-gi3tmnq),
[- `setIsRefreshingObjects:`](#apple-gi4ts)

---

### selectObjectsWithFetchSpecification:editingContext:

- (void)`selectObjectsWithFetchSpecification:`(EOFetchSpecification \*)_fetchSpecification_`editingContext:`(EOEditingContext \*)_anEditingContext_

Selects objects described by _fetchSpecification_ so that they'll be fetched into _anEditingContext_. The selected objects compose one or more result sets, each object of which will be returned by subsequent `[fetchObject](#apple-gi3tmnq)` messages in the order prescribed by _fetchSpecification_'s EOSortOrderings.

Raises an exception if an error occurs; the particular exception depends on the specific error, and is indicated in the exception's description. Some possible reasons for failure are:

- _fetchSpecification_ is invalid.
- The receiver's EODatabaseContext has no transaction in progress.
- The delegate disallows the select operation.
- The receiver's EOAdaptorChannel fails to perform the select operation.

This method invokes the delegate methods [`databaseContext:shouldSelectObjectsWithFetchSpecification:databaseChannel:`](../Protocols/EODatabaseContextDelegate.md#apple-geydooa), [`databaseContext:shouldUsePessimisticLockWithFetchSpecification: databaseChannel:`](../Protocols/EODatabaseContextDelegate.md#apple-geydqna), and [`databaseContext:didSelectObjectsWithFetchSpecification:databaseChannel:`](../Protocols/EODatabaseContextDelegate.md#apple-geydioi). See their descriptions in the EODatabaseContext class specification for more information.

You wouldn't ordinarily invoke this method directly; rather, you'd use an EOEditingContext to select and fetch enterprise objects.

__See also:__
[- `fetchObject`](#apple-gi3tmnq)

---

### setCurrentEditingContext:

- (void)`setCurrentEditingContext:`(EOEditingContext \*)_anEditingContext_

Sets the EOEditingContext that's made the owner of fetched objects to _anEditingContext_. This method is automatically invoked by [`selectObjectsWithFetchSpecification:editingContext:`](#apple-gi3te). You should never invoke it directly.

__See also:__
[- `setCurrentEntity:`](#apple-gi4dm)

---

### setCurrentEntity:

- (void)`setCurrentEntity:`(EOEntity \*)_anEntity_

Sets the EOEntity used when fetching enterprise objects to _anEntity_. Subsequent `[fetchObject](#apple-gi3tmnq)` messages during a fetch operation create an object of the class associated with _anEntity_. This method is invoked automatically by `[selectObjectsWithFetchSpecification:editingContext:](#apple-gi3te)`.You should never need to invoke it directly.

__See also:__
[- `setCurrentEditingContext:`](#apple-gi4de)

---

### setDelegate:

- (void)`setDelegate:`(id)_anObject_

Sets the receiver's delegate to _anObject_. An EODatabaseChannel shares the delegate of its EODatabaseContext; you should never invoke this method directly. See the EODatabaseContext class specification for the delegate methods you can implement.

__See also:__
[`delegate`](#apple-gi2dq)

---

### setIsLocking:

- (void)`setIsLocking:`(BOOL)_flag_

Records whether the receiver locks the records it selects. A EODatabaseChannel modifies its interaction with the database server and its snapshotting behavior based on this setting. If _flag_ is YES the EODatabaseChannel modifies its fetching behavior to lock objects; if _flag_ is NO it simply fetches them.

An EODatabaseChannel automatically sets this flag according to the fetch specification used in a [`selectObjectsWithFetchSpecification:editingContext:`](#apple-gi3te) message. You might invoke this method directly if evaluating SQL directly with EOAdaptorChannel's method.

__See also:__
- `locksObjects` (EOFetchSpecification), [- `setIsLocking:`](#apple-gi4tima)

---

### setIsRefreshingObjects:

- (void)`setIsRefreshingObjects:`(BOOL)_flag_

Records whether the receiver causes existing snapshots and enterprise objects to be overwritten with fetched values. If _flag_ is YES the receiver overwrites existing snapshots with fetched values and posts an EOObjectsChangedInStoreNotification on behalf of its EODatabaseContext (which typically causes the an existing object's EOEditingContext to replace its values with the new ones). If _flag_ is NO, the receiver relies on the delegate to determine whether snapshots should be overwritten, and doesn't cause enterprise objects to be overwritten.

An EODatabaseChannel automatically sets this flag according to the fetch specification used in a [`selectObjectsWithFetchSpecification:editingContext:`](#apple-gi3te) message. You might invoke this method directly if evaluating SQL directly with EOAdaptorChannel's `evaluateExpression:` method.

__See also:__
- `refreshesRefetchedObjects` (EOFetchSpecification)

---

### 

---

[!](More%20about%20EODatabase.md)
[!](EODatabaseContext-3.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
