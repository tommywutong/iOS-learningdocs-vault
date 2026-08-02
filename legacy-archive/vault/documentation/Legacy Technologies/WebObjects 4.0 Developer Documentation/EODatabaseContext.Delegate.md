---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EODatabaseContextDelegate.html
archived_at: '2026-07-18T01:28:14.616545Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOAdaptor.Delegate.md)
[!](EOUtilities.md)

---

# EODatabaseContext.Delegate

__Inherits From:__
com.apple.yellow.eoaccess

An EODatabaseContext shares its delegate with its EODatabaseChannels. These delegate methods are actually sent from EODatabaseChannel, but they're defined in EODatabaseContext for ease of access:

[databaseContextDidSelectObjects](#apple-geydioi)

[databaseContextShouldSelectObjects](#apple-geydooa)

[databaseContextShouldUpdateCurrentSnapshot](#apple-geydqmi)

[databaseContextShouldUsePessimisticLockWithFetchSpecification](#apple-geydqna)

You can use the EODatabaseContext delegate methods to intervene when objects are created and when they're fetched from the database. This gives you more fine-grained control over such issues as how an object's primary key is generated ([`databaseContextNewPrimaryKeyForObject`](#apple-geydkni)), how and if objects are locked ([`databaseContextShouldLockObjectWithGlobalID`](#apple-geydomq)), what fetch specification is used to fetch objects ([`databaseContextShouldSelectObjects`](#apple-geydooa)), how batch faulting is performed ([`databaseContextShouldFetchArrayFault`](#apple-geydkoa) and [`databaseContextShouldFetchObjectFault`](#apple-geydmmq)), and so on. For more information, see the individual delegate method descriptions.

---

## Instance Methods

---

### databaseContextDidFetchObjects

public abstract void `databaseContextDidFetchObjects`(
EODatabaseContext _aDatabaseContext_,
NSArray _objects_,
com.apple.yellow.eocontrol.EOFetchSpecification _fetchSpecification_,
com.apple.yellow.eocontrol.EOEditingContext _anEditingContext_)

Invoked from [`objectsWithFetchSpecification`](../Classes/EODatabaseContext.md#apple-he2tm) after _aDatabaseContext_ fetches _objects_ using the criteria defined in _fetchSpecification_ on behalf of _anEditingContext_.

__See also:__
[`databaseContextShouldFetchObjectFault`](#apple-geydmmq)

---

### databaseContextDidSelectObjects

public abstract void `databaseContextDidSelectObjects`(
EODatabaseContext _aDatabaseContext_,
com.apple.yellow.eocontrol.EOFetchSpecification _fetchSpecification_,
EODatabaseChannel _channel_)

Invoked from the EODatabaseChannel method [`selectObjectsWithFetchSpecification`](../Classes/EODatabaseChannel.md#apple-gi3te) to tell the delegate that _channel_ selected the objects on behalf of _aDatabaseContext_ as specified by _fetchSpecification_.

__See also:__
[`databaseContextShouldSelectObjects`](#apple-geydooa)

---

### databaseContextFailedToFetchObject

public abstract boolean `databaseContextFailedToFetchObject`(
EODatabaseContext _aDatabaseContext_,
java.lang.Object _object_,
com.apple.yellow.eocontrol.EOGlobalID _globalID_)

Sent when a to-one fault cannot find its data in the database. The _object_ is a cleared fault identified by _globalID_. If this method returns `true`, _aDatabaseContext_ assumes that the delegate has handled the situation to its satisfaction, in whatever way it deemed appropriate (for example, by displaying an alert panel or initializing a fault object with new values). If it returns `false` or if the delegate method is not implemented, _aDatabaseContext_ throws an exception.

---

### databaseContextNewPrimaryKeyForObject

public abstract NSDictionary `databaseContextNewPrimaryKeyForObject`(
EODatabaseContext _aDatabaseContext_,
java.lang.Object _object_,
EOEntity _anEntity_)

Sent when a newly inserted enterprise _object_ doesn't already have a primary key set. This delegate method can be used to implement custom primary key generation. If the delegate is not implemented or returns __null__ , then _aDatabaseContext_ will send an EOAdaptorChannel a [`primaryKeyForNewRowWithEntity`](../Classes/EOAdaptorChannel.md#apple-geydqna) message in an attempt to generate the key.

The dictionary you return from this delegate method contains the attribute or attributes (if _object_ has a compound primary key) that make up _object_'s primary key.

---

### databaseContextShouldFetchArrayFault

public abstract boolean `databaseContextShouldFetchArrayFault`(
EODatabaseContext _databaseContext_,
java.lang.Object _anObject_)

Invoked when a fault is fired, this delegate method lets you fine-tune the behavior of batch faulting. Delegates can fetch the array themselves (for example, by using the EODatabaseContext method [`batchFetchRelationship`](../Classes/EODatabaseContext.md#apple-ha4dq)) and return `false`, or return `true` to allow the _databaseContext_ to do the fetch itself. If _databaseContext_ performs the fetch it will batch fault according to the batch count on the relationship being fetched.

__See also:__
[`databaseContextShouldFetchObjectFault`](#apple-geydmmq)

---

### databaseContextShouldFetchObjectFault

public abstract boolean `databaseContextShouldFetchObjectFault`(
EODatabaseContext _databaseContext_,
java.lang.Object _anObject_)

Invoked when a fault is fired, this delegate method lets you fine-tune the behavior of batch faulting. Delegates can fetch the fault themselves (for example, by using the EODatabaseContext method[`objectsWithFetchSpecification`](../Classes/EODatabaseContext.md#apple-he2tm)) and return `false`, or return `true` to allow _databaseContext_ to perform the fetch. If _databaseContext_ performs the fetch, it will batch fault according to the batch count on the entity being fetched.

__See also:__
[`databaseContextShouldFetchArrayFault`](#apple-geydkoa)

---

### databaseContextShouldFetchObjects

public abstract NSArray `databaseContextShouldFetchObjects`(
EODatabaseContext _aDatabaseContext_,
com.apple.yellow.eocontrol.EOFetchSpecification _fetchSpecification_,
com.apple.yellow.eocontrol.EOEditingContext _anEditingContext_)

Invoked from [`objectsWithFetchSpecification`](../Classes/EODatabaseContext.md#apple-he2tm) to give the delegate the opportunity to satisfy _anEditingContext_'s fetch request (using the criteria specified in _fetchSpecification_) from a local cache. If the delegate returns __null__ , _aDatabaseContext_ performs the fetch. Otherwise, the returned array is returned as the fetch result.

__See also:__
[`databaseContextDidFetchObjects`](#apple-gmydemjr)

---

### databaseContextShouldInvalidateObjectWithGlobalID

public abstract boolean `databaseContextShouldInvalidateObjectWithGlobalID`(
EODatabaseContext _aDatabaseContext_,
com.apple.yellow.eocontrol.EOGlobalID _globalID_,
NSDictionary _snapshot_)

Invoked from [`invalidateObjectsWithGlobalIDs`](../Classes/EODatabaseContext.md#apple-hezti). Delegate can cause _aDatabaseContext_'s object as identified by _globalID_ to not be invalidated and that object's _snapshot_ to not be cleared by returning `false`.

---

### databaseContextShouldLockObjectWithGlobalID

public abstract boolean `databaseContextShouldLockObjectWithGlobalID`(
EODatabaseContext _aDatabaseContext_,
com.apple.yellow.eocontrol.EOGlobalID _globalID_,
NSDictionary _snapshot_)

Invoked from [`lockObjectWithGlobalID`](../Classes/EODatabaseContext.md#apple-geytgmy). The delegate should return `true` if it wants the operation to proceed or `false` if it doesn't. Values from _snapshot_ are used to create a qualifier from the attributes used for locking specified for the object's entity (that is, the object identified by _globalID_). Delegates can override the locking mechanism by implementing their own locking procedure and returning `false`. Methods that override the locking mechanism should throw an exception on the failure to lock exactly one object.

---

### databaseContextShouldRaiseExceptionForLockFailure

public abstract boolean `databaseContextShouldRaiseExceptionForLockFailure`(
EODatabaseContext _aDatabaseContext_,
java.lang.Throwable _exception_)

Invoked from [`lockObjectWithGlobalID`](../Classes/EODatabaseContext.md#apple-geytgmy). This method allows the delegate to suppress an _exception_ that has occurred during _aDatabaseContext_'s attempt to lock the object.

---

### databaseContextShouldSelectObjects

public abstract boolean `databaseContextShouldSelectObjects`(
EODatabaseContext _aDatabaseContext_,
com.apple.yellow.eocontrol.EOFetchSpecification _fetchSpecification_,
EODatabaseChannel _channel_)

Invoked from the EODatabaseChannel method [`selectObjectsWithFetchSpecification`](../Classes/EODatabaseChannel.md#apple-gi3te) to tell the delegate that _channel_ will select objects on behalf of _aDatabaseContext_ as specified by _fetchSpecification_. The delegate should not modify _fetchSpecification_'s qualifier or fetch order. If the delegate returns `true` the channel will go ahead and select the object; if the delegate returns `false` (possibly after issuing custom SQL against the adaptor) the _channel_ will skip the select and return.

---

### databaseContextShouldUpdateCurrentSnapshot

public abstract NSDictionary `databaseContextShouldUpdateCurrentSnapshot`(
EODatabaseContext _aDatabaseContext_,
NSDictionary _currentSnapshot_,
NSDictionary _newSnapshot_,
com.apple.yellow.eocontrol.EOGlobalID _globalID_,
EODatabaseChannel _channel_)

Invoked from the EODatabaseChannel method [`fetchObject`](../Classes/EODatabaseChannel.md#apple-gi3tmnq) when _aDatabaseContext_ already has a snapshot (_currentSnapshot_) for a row fetched from the database. This method is invoked without first checking whether the snapshots are equivalent (the check would be too expensive to do in the common case), so the receiver may be passed equivalent snapshots. The default behavior is to not update an older snapshot with _newSnapshot_. The delegate can override this behavior by returning a dictionary (possibly _newSnapshot_) that will be recorded as the updated snapshot. This will result in _aDatabaseContext_ broadcasting an EOObjectsChangedInStoreNotification, causing the object store hierarchy to invalidate existing objects (as identified by _globalID_) built from the obsolete snapshot. Returning __null__  throws an exception. You can use this method to achieve the same effect as using a com.apple.yellow.eocontrol.EOFetchSpecification with `setRefreshesRefetchedObjects:` set to `true`-that is, it allows you to overwrite in-memory object values with values from the database that may have been changed by someone else.

Returning _currentSnapshot_ causes the _aDatabaseContext_ to perform the default behavior (that is, not updating the older snapshot).

---

### databaseContextShouldUsePessimisticLockWithFetchSpecification

public abstract boolean `databaseContextShouldUsePessimisticLockWithFetchSpecification`(
EODatabaseContext _databaseContext_,
com.apple.yellow.eocontrol.EOFetchSpecification _fetchSpecification_,
EODatabaseChannel _channel_)

Invoked from the EODatabaseChannel method [`selectObjectsWithFetchSpecification`](../Classes/EODatabaseChannel.md#apple-gi3te) regardless of the update strategy specified on _channel_'s _databaseContext_. The delegate should not modify the qualifier or fetch order contained in _fetchSpecification_. If the delegate returns `true` the channel locks the rows being selected; if the delegate returns `false` the channel selects the rows without locking.

---

### databaseContextWillOrderAdaptorOperationsFromDatabaseOperations

public abstract NSArray `databaseContextWillOrderAdaptorOperationsFromDatabaseOperations`(
EODatabaseContext _aDatabaseContext_,
NSArray _databaseOperations_)

Sent from [`performChanges`](../Classes/EODatabaseContext.md#apple-he3tc). If the delegate responds to this message, it must return an array of EOAdaptorOperations that _aDatabaseContext_ can then submit to an EOAdaptorChannel for execution. The delegate can fabricate its own array by asking each of the _databaseOperations_ for its list of EOAdaptorOperations, and adding them to the array which will eventually be returned by this method. The delegate is free to optimize, order, or transform the list in whatever way it deems necessary. This method is useful for applications that need a special ordering of the EOAdaptorOperations so as not to violate any database referential integrity constraints.

---

### databaseContextWillPerformAdaptorOperations

public abstract NSArray `databaseContextWillPerformAdaptorOperations`(
EODatabaseContext _aDatabaseContext_,
NSArray _adaptorOperations_,
EOAdaptorChannel _adaptorChannel_)

Sent from __performChanges__ . The delegate can return a new _adaptorOperations_ array which _aDatabaseContext_ will hand to _adaptorChannel_ for execution in place of the old array of EOAdaptorOperations. This method is useful for applications that need a special ordering of the EOAdaptorOperations so as not to violate any database referential integrity constraints.

---

[!](EOAdaptor.Delegate.md)
[!](EOUtilities.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
