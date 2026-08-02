---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EODatabaseContextDelegate.html
archived_at: '2026-07-18T01:28:24.006934Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOCustomClassArchiving.md)
[!](EOEditingContext%20Additions-2.md)

---

# EODatabaseContextDelegation

__Declared in:__
EOAccess/EODatabaseContext.h

# Protocol Description

An EODatabaseContext shares its delegate with its EODatabaseChannels. These delegate methods are actually sent from EODatabaseChannel, but they're defined in EODatabaseContext for ease of access:

[- databaseContext:didSelectObjectsWithFetchSpecification:databaseChannel:](#apple-geydioi)

[- databaseContext:shouldSelectObjectsWithFetchSpecification:databaseChannel:](#apple-geydooa)

[- databaseContext:shouldUpdateCurrentSnapshot:newSnapshot:globalID:databaseChannel:](#apple-geydqmi)

[- databaseContext:shouldUsePessimisticLockWithFetchSpecification: databaseChannel:](#apple-geydqna)

You can use the EODatabaseContext delegate methods to intervene when objects are created and when they're fetched from the database. This gives you more fine-grained control over such issues as how an object's primary key is generated (`databaseContextNewPrimaryKeyForObjectdatabaseContext:newPrimaryKeyForObject:entity:`), how and if objects are locked (`databaseContextShouldLockObjectWithGlobalIDdatabaseContext:shouldLockObjectWithGlobalID:snapshot:`), what fetch specification is used to fetch objects ([`databaseContext:shouldSelectObjectsWithFetchSpecification:databaseChannel:`](#apple-geydooa)), how batch faulting is performed ([`databaseContext:shouldFetchArrayFault:`](#apple-geydkoa) and [`databaseContext:shouldFetchObjectFault:`](#apple-geydmmq)), and so on. For more information, see the individual delegate method descriptions.

---

## Instance Methods

---

### databaseContext:didFetchObjects:fetchSpecification:editingContext:

- (void)__databaseContext:__ (EODatabaseContext \*)_aDatabaseContext_
__didFetchObjects:__ (NSArray \*)_objects_
__fetchSpecification:__ (EOFetchSpecification \*)_fetchSpecification_ __editingContext:__ (EOEditingContext \*)_anEditingContext_

Invoked from [`objectsWithFetchSpecification:editingContext:`](../Classes/EODatabaseContext.md#apple-he2tm) after _aDatabaseContext_ fetches _objects_ using the criteria defined in _fetchSpecification_ on behalf of _anEditingContext_.

__See also:__
[- `databaseContext:shouldFetchObjectFault:`](#apple-geydmmq)

---

### databaseContext:didSelectObjectsWithFetchSpecification:databaseChannel:

- (void)__databaseContext:__ (EODatabaseContext \*)_aDatabaseContext_ __didSelectObjectsWithFetchSpecification:__ (EOFetchSpecification \*)_fetchSpecification_ __databaseChannel:__ (EODatabaseChannel \*)_channel_

Invoked from the EODatabaseChannel method [`selectObjectsWithFetchSpecification:editingContext:`](../Classes/EODatabaseChannel.md#apple-gi3te) to tell the delegate that _channel_ selected the objects on behalf of _aDatabaseContext_ as specified by _fetchSpecification_.

__See also:__
[- `databaseContext:shouldSelectObjectsWithFetchSpecification:databaseChannel:`](#apple-geydooa)

---

### databaseContext:failedToFetchObject:globalID:

- (BOOL)__databaseContext:__ (EODatabaseContext \*)_aDatabaseContext_
__failedToFetchObject:__ (id)_object_
__globalID:__ (EOGlobalID \*)_globalID_

Sent when a to-one fault cannot find its data in the database. The _object_ is a cleared fault identified by _globalID_. If this method returns YES, _aDatabaseContext_ assumes that the delegate has handled the situation to its satisfaction, in whatever way it deemed appropriate (for example, by displaying an alert panel or initializing a fault object with new values). If it returns NO or if the delegate method is not implemented, _aDatabaseContext_ raises an NSObjectNotAvailableException.

---

### databaseContext:newPrimaryKeyForObject:entity:

- (NSDictionary \*)__databaseContext:__ (EODatabaseContext \*)_aDatabaseContext_ __newPrimaryKeyForObject:__ (id)_object_
__entity:__ (EOEntity \*)_entity_

Sent when a newly inserted enterprise _object_ doesn't already have a primary key set. This delegate method can be used to implement custom primary key generation. If the delegate is not implemented or returns __nil__ , then _aDatabaseContext_ will send an EOAdaptorChannel a [`primaryKeyForNewRowWithEntity:`](../Classes/EOAdaptorChannel.md#apple-geydqna) message in an attempt to generate the key.

The dictionary you return from this delegate method contains the attribute or attributes (if _object_ has a compound primary key) that make up _object_'s primary key.

---

### databaseContext:shouldFetchArrayFault:

- (BOOL)__databaseContext:__ (EODatabaseContext \*)_databaseContext_ __shouldFetchArrayFault:__ (id)_fault_

Invoked when a fault is fired, this delegate method lets you fine-tune the behavior of batch faulting. Delegates can fetch the array themselves (for example, by using the EODatabaseContext method [`batchFetchRelationship:forSourceObjects:editingContext:`](../Classes/EODatabaseContext.md#apple-ha4dq)) and return NO, or return YES to allow the _databaseContext_ to do the fetch itself. If _databaseContext_ performs the fetch it will batch fault according to the batch count on the relationship being fetched.

__See also:__
[- `databaseContext:shouldFetchObjectFault:`](#apple-geydmmq)

---

### databaseContext:shouldFetchObjectFault:

- (BOOL)__databaseContext:__ (EODatabaseContext \*)_databaseContext_ __shouldFetchObjectFault:__ (id)_fault_

Invoked when a fault is fired, this delegate method lets you fine-tune the behavior of batch faulting. Delegates can fetch the fault themselves (for example, by using the EODatabaseContext method[`objectsWithFetchSpecification:editingContext:`](../Classes/EODatabaseContext.md#apple-he2tm)) and return NO, or return YES to allow _databaseContext_ to perform the fetch. If _databaseContext_ performs the fetch, it will batch fault according to the batch count on the entity being fetched.

__See also:__
[- `databaseContext:shouldFetchArrayFault:`](#apple-geydkoa)

---

### databaseContext:shouldFetchObjectsWithFetchSpecification:editingContext:

- (NSArray \*)__databaseContext:__ (EODatabaseContext \*)_aDatabaseContext_ __shouldFetchObjectsWithFetchSpecification:__ (EOFetchSpecification \*)_fetchSpecification_ __editingContext:__ (EOEditingContext \*)_anEditingContext_

Invoked from [`objectsWithFetchSpecification:editingContext:`](../Classes/EODatabaseContext.md#apple-he2tm) to give the delegate the opportunity to satisfy _anEditingContext_'s fetch request (using the criteria specified in _fetchSpecification_) from a local cache. If the delegate returns __nil__ , _aDatabaseContext_ performs the fetch. Otherwise, the returned array is returned as the fetch result.

__See also:__
`databaseContextDidFetchObjectsdatabaseContext:didFetchObjects:fetchSpecification:
editingContext:`

---

### databaseContext:shouldInvalidateObjectWithGlobalID:snapshot:

- (BOOL)__databaseContext:__ (EODatabaseContext \*)_aDatabaseContext_ __shouldInvalidateObjectWithGlobalID:__ (EOGlobalID \*)_globalId_
__snapshot:__ (NSDictionary \*)_snapshot_

Invoked from [`invalidateObjectsWithGlobalIDs:`](../Classes/EODatabaseContext.md#apple-hezti). Delegate can cause _aDatabaseContext_'s object as identified by _globalID_ to not be invalidated and that object's _snapshot_ to not be cleared by returning NO.

---

### databaseContext:shouldLockObjectWithGlobalID:snapshot:

- (BOOL)__databaseContext:__ (EODatabaseContext \*)_aDatabaseContext_ __shouldLockObjectWithGlobalID:__ (EOGlobalID \*)_globalID_
__snapshot:__ (NSDictionary \*)_snapshot_

Invoked from [`lockObjectWithGlobalID:editingContext:`](../Classes/EODatabaseContext.md#apple-geytgmy). The delegate should return YES if it wants the operation to proceed or NO if it doesn't. Values from _snapshot_ are used to create a qualifier from the attributes used for locking specified for the object's entity (that is, the object identified by _globalID_). Delegates can override the locking mechanism by implementing their own locking procedure and returning NO. Methods that override the locking mechanism should raise an exception on the failure to lock exactly one object.

---

### databaseContext:shouldRaiseExceptionForLockFailure:

- (BOOL)__databaseContext:__ (EODatabaseContext \*)_aDatabaseContext_ __shouldRaiseExceptionForLockFailure:__ (NSException \*)_exception_

Invoked from [`lockObjectWithGlobalID:editingContext:`](../Classes/EODatabaseContext.md#apple-geytgmy). This method allows the delegate to suppress an _exception_ that has occurred during _aDatabaseContext_'s attempt to lock the object.

---

### databaseContext:shouldSelectObjectsWithFetchSpecification:databaseChannel:

- (BOOL)__databaseContext:__ (EODatabaseContext \*)_aDatabaseContext_ __shouldSelectObjectsWithFetchSpecification:__ (EOFetchSpecification \*)_fetchSpecification_ __databaseChannel:__ (EODatabaseChannel \*)_channel_

Invoked from the EODatabaseChannel method [`selectObjectsWithFetchSpecification:editingContext:`](../Classes/EODatabaseChannel.md#apple-gi3te) to tell the delegate that _channel_ will select objects on behalf of _aDatabaseContext_ as specified by _fetchSpecification_. The delegate should not modify _fetchSpecification_'s qualifier or fetch order. If the delegate returns YES the channel will go ahead and select the object; if the delegate returns NO (possibly after issuing custom SQL against the adaptor) the _channel_ will skip the select and return.

---

### databaseContext:shouldUpdateCurrentSnapshot:newSnapshot:globalID:databaseChannel:

- (NSDictionary \*)__databaseContext:__ (EODatabaseContext \*)_aDatabaseContext___shouldUpdateCurrentSnapshot:__ (NSDictionary \*)_currentSnapshot_
__newSnapshot:__ (NSDictionary \*)_newSnapshot_
__globalID:__ (EOGlobalID \*)_globalID_
__databaseChannel:__ (EODatabaseChannel \*)_channel_

Invoked from the EODatabaseChannel method [`fetchObject`](../Classes/EODatabaseChannel.md#apple-gi3tmnq) when _aDatabaseContext_ already has a snapshot (_currentSnapshot_) for a row fetched from the database. This method is invoked without first checking whether the snapshots are equivalent (the check would be too expensive to do in the common case), so the receiver may be passed equivalent snapshots. The default behavior is to not update an older snapshot with _newSnapshot_. The delegate can override this behavior by returning a dictionary (possibly _newSnapshot_) that will be recorded as the updated snapshot. This will result in _aDatabaseContext_ broadcasting an EOObjectsChangedInStoreNotification, causing the object store hierarchy to invalidate existing objects (as identified by _globalID_) built from the obsolete snapshot. Returning __nil__  raises an exception. You can use this method to achieve the same effect as using an EOFetchSpecification with `setRefreshesRefetchedObjects:` set to YES-that is, it allows you to overwrite in-memory object values with values from the database that may have been changed by someone else.

Returning _currentSnapshot_ causes the _aDatabaseContext_ to perform the default behavior (that is, not updating the older snapshot).

---

### databaseContext:shouldUsePessimisticLockWithFetchSpecification: databaseChannel:

- (BOOL)__databaseContext:__ (EODatabaseContext \*)_databaseContext_ __shouldUsePessimisticLockWithFetchSpecification:__ (EOFetchSpecification \*)_fetchSpecification_ __databaseChannel:__ (EODatabaseChannel \*)_channel_

Invoked from the EODatabaseChannel method [`selectObjectsWithFetchSpecification:editingContext:`](../Classes/EODatabaseChannel.md#apple-gi3te) regardless of the update strategy specified on _channel_'s _databaseContext_. The delegate should not modify the qualifier or fetch order contained in _fetchSpecification_. If the delegate returns YES the channel locks the rows being selected; if the delegate returns NO the channel selects the rows without locking.

---

### databaseContext:willOrderAdaptorOperationsFromDatabaseOperations:

- (NSArray \*)__databaseContext:__ (EODatabaseContext \*)_aDatabaseContext_ __willOrderAdaptorOperationsFromDatabaseOperations:__ (NSArray \*)_databaseOperations_

Sent from [`performChanges`](../Classes/EODatabaseContext.md#apple-he3tc). If the delegate responds to this message, it must return an array of EOAdaptorOperations that _aDatabaseContext_ can then submit to an EOAdaptorChannel for execution. The delegate can fabricate its own array by asking each of the _databaseOperations_ for its list of EOAdaptorOperations, and adding them to the array which will eventually be returned by this method. The delegate is free to optimize, order, or transform the list in whatever way it deems necessary. This method is useful for applications that need a special ordering of the EOAdaptorOperations so as not to violate any database referential integrity constraints.

---

### databaseContext:willPerformAdaptorOperations:adaptorChannel:

- (NSArray \*)__databaseContext:__ (EODatabaseContext \*)_aDatabaseContext_ __willPerformAdaptorOperations:__ (NSArray \*)_adaptorOperations_
__adaptorChannel:__ (EOAdaptorChannel \*)_adaptorChannel_

Sent from __performChanges__ . The delegate can return a new _adaptorOperations_ array which _aDatabaseContext_ will hand to _adaptorChannel_ for execution in place of the old array of EOAdaptorOperations. This method is useful for applications that need a special ordering of the EOAdaptorOperations so as not to violate any database referential integrity constraints.

---

### databaseContext:willRunLoginPanelToOpenDatabaseChannel:

- (BOOL)__databaseContext:__ (EODatabaseContext \*)_aDatabaseContext_ __willRunLoginPanelToOpenDatabaseChannel:__ (EODatabaseChannel \*)_channel_

When _aDatabaseContext_ is about to use a _channel_, it checks to see if the _channel_'s corresponding EOAdaptorChannel is open. If it isn't, it attempts to open the EOAdaptorChannel by sending it an __openChannel__  message. If that doesn't succeed, _aDatabaseContext_ will ask the EOAdaptorChannel's adaptor to run the login panel and open the channel. _aDatabaseContext_ gives the delegate a chance to intervene in this by invoking this delegate method. The delegate can return NO to stop _aDatabaseContext_ from running the login panel. In this case, the delegate is responsible for opening the channel. If the delegate returns YES, _aDatabaseContext_ runs the login panel.

---

[!](EOCustomClassArchiving.md)
[!](EOEditingContext%20Additions-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
