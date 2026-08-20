---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EODatabaseContext.html
archived_at: '2026-07-18T01:28:09.403310Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EODatabaseChannel.md)
[!](EODatabaseContext-2.md)

---

# EODatabaseContext

__Inherits From:__
com.apple.yellow.eocontrol.EOCooperatingObjectStore :
com.apple.yellow.eocontrol.EOObjectStore :
NSObject

__Inherits From:__
com.apple.yellow.eoaccess

---

## Class Description

An EODatabaseContext object is a com.apple.yellow.eocontrol.EOObjectStore (com.apple.client.eocontrol if you're using Siva) for accessing relational databases, creating and saving objects based on EOEntity definitions in an EOModel.

An EODatabaseContext represents a single connection to a database server, and it determines the updating and locking strategy used by its EODatabaseChannel objects. An EODatabaseContext has a corresponding EODatabase object. If the server supports multiple concurrent transactions, the EODatabase object may have several database contexts. If the server and adaptor support it, a database context may in turn have several database channels, which handle access to the data on the server.

For a more information, see ["More about EODatabaseContext"](EODatabaseContext-2.md).

---

## Method Types

**Constructors**

**[EODatabaseContext](#apple-guztcmrs)**

**Fetching objects**

**[objectsWithFetchSpecification](#apple-he2tm)

**[objectsForSourceGlobalID](#apple-he2tg)

**[arrayFaultWithSourceGlobalID](#apple-ha4da)

**[faultForGlobalID](#apple-heydk)

**[faultForRawRow](#apple-gq3tsmbz)

**[batchFetchRelationship](#apple-ha4dq)************

**Accessing the adaptor context**

**[adaptorContext](#apple-ha3to)**

**Accessing the database object**

**[database](#apple-ha4tq)**

**Accessing the coordinator**

**[coordinator](#apple-ha4tk)**

**Managing channels**

**[availableChannel](#apple-ha4di)

**[registerChannel](#apple-giztgmjr)

**[registeredChannels](#apple-gq4dqnrt)

**[unregisterChannel](#apple-geytenq)********

**Accessing the delegate**

**[setDelegate](#apple-geydemq)

**[delegate](#apple-heydc)****

**Committing or discarding changes**

**[invalidateAllObjects](#apple-heztc)

**[invalidateObjectsWithGlobalIDs](#apple-hezti)

**[rollbackChanges](#apple-geydcni)

**[saveChangesInEditingContext](#apple-geydcoi)

**[commitChanges](#apple-ha4tc)

**[performChanges](#apple-he3tc)

**[prepareForSaveWithCoordinator](#apple-he4dg)

**[recordUpdateForObject](#apple-geytgni)

**[recordChangesInEditingContext](#apple-he4dm)

**[refaultObject](#apple-giztgnbw)********************

**Determining if the EODatabaseContext is responsible for a particular operation**

**[ownsObject](#apple-he3do)

**[ownsGlobalID](#apple-he3dg)

**[handlesFetchSpecification](#apple-hezdk)******

**Managing Snapshots**

**[forgetSnapshotForGlobalID](#apple-heyto)

**[forgetSnapshotsForGlobalIDs](#apple-hezdc)

**[localSnapshotForGlobalID](#apple-he2dk)

**[recordSnapshotForGlobalID](#apple-he4ds)

**[recordSnapshots](#apple-geytemq)

**[snapshotForGlobalID](#apple-gq3tomzw)

**[recordSnapshotForSourceGlobalID](#apple-ojswg33smrjw4ylqonug65cgn5zfg33vojrwkr3mn5rgc3cjiq)

**[snapshotForSourceGlobalID](#apple-onxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyske)

**[localSnapshotForSourceGlobalID](#apple-nrxwgylmknxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyske)

**[recordToManySnapshots](#apple-gq3tmmjy)********************

**Initializing objects**

**[initializeObject](#apple-geytaoi)**

**Obtaining an EODatabaseContext**

**[registeredDatabaseContextForModel](#apple-g42tc)**

**Locking objects**

**[setUpdateStrategy](#apple-geydenq)

**[updateStrategy](#apple-geydgoa)

**[registerLockedObjectWithGlobalID](#apple-geydcmi)

**[isObjectLockedWithGlobalID](#apple-hezto)

**[forgetAllLocks](#apple-heyds)

**[forgetLocksForObjectsWithGlobalIDs](#apple-heytg)

**[lockObjectWithGlobalID](#apple-geytgmy)**************

**Returning information about objects**

**[valuesForKeys](#apple-geydimq)**

**Setting the context class**

**[contextClassToRegister](#apple-gq3tcmry)

**[setContextClassToRegister](#apple-gq3tcnrs)****

**Checking connection status**

**[hasBusyChannels](#apple-gi2dcmrr)**

**Other**

**[forceConnectionWithModel](#apple-gq3tqnjq)

**[lock](#apple-gq3tqnzq)

**[unlock](#apple-gq3tqnzz)******

---

## Constructors

---

### EODatabaseContext

public `EODatabaseContext`()

public `EODatabaseContext`(EODatabase _aDatabase_)

Creates and returns a new EODatabaseContext. Typically, you don't need to programmatically create database contexts. Rather, they are created automatically by the control layer. See "Creating and Using an EODatabaseContext" for more information.

_aDatabase_ is assigned to the new database as the EODatabase object with which the new context works. The new database context creates an EOAdaptorContext with which to communicate with the database server. Throws an exception if the underlying adaptor context can't create a corresponding adaptor channel.

__See also:__
[`database`](#apple-ha4tq)

#

---

### contextClassToRegister

public static java.lang.Class `contextClassToRegister`()

Returns the class that is registered with an EOObjectStoreCoordinator when the coordinator broadcasts an EOCooperatingObjectStoreNeeded notification. By default this is EODatabaseContext, but you can use [`setContextClassToRegister`](#apple-gq3tcnrs) to specify your own subclass of EODatabaseContext.

When an EOObjectStoreCoordinator sends an EOCooperatingObjectStoreNeeded notification for an EOEntity in the default model group, if `contextClassToRegister` is non-`null` (and it should be-it makes no sense to set `contextClassToRegister` to `null`), an instance of the that class is created, the EOModel for the EOEntity is registered, and the context class is registered with the requesting EOObjectStoreCoordinator.

---

### forceConnectionWithModel

public static EODatabaseContext `forceConnectionWithModel`(EOModel _aModel_,
NSDictionary _overrides_,
com.apple.yellow.eocontrol.EOEditingContext _anEditingContext_)

Forces the stack of objects in the EOAccess layer to be instantiated, if necessary, and then makes a connection to the database. If there is an existing connection for _amodel_, it is first closed and then reconnected. The new connection dictionary is effectively made up of the model's connection dictionary, overlaid with _overrides_. All compatible models in the model's group also are associated with the new connection (so they share the same adaptor). Returns the EODatabaseContext associated with the model for _anEditingContext_.

---

### registeredDatabaseContextForModel

public static EODatabaseContext `registeredDatabaseContextForModel`(EOModel _aModel_, com.apple.yellow.eocontrol.EOEditingContext _anEditingContext_)

Finds the com.apple.yellow.eocontrol.EOObjectStoreCoordinator for _anEditingContext_ and checks to see if it already contains an EODatabaseContext cooperating store for _aModel_. If it does, it returns that EODatabaseContext. Otherwise it instantiates a new EODatabaseContext, adds it to the EOObjectStoreCoordinator, and returns the EODatabaseContext.

---

### setContextClassToRegister

public static void `setContextClassToRegister`(java.lang.Class _contextClass_)

Sets to _contextClass_ the "contextClassToRegister." For more discussion of this topic, see the method description for [`contextClassToRegister`](#apple-gq3tcmry).

---

## Instance Methods

---

### adaptorContext

public EOAdaptorContext `adaptorContext`()

Returns the EOAdaptorContext used by the EODatabaseContext for communication with the database server.

---

### arrayFaultWithSourceGlobalID

public NSArray `arrayFaultWithSourceGlobalID`(com.apple.yellow.eocontrol.EOGlobalID _globalID_, java.lang.String _name_, com.apple.yellow.eocontrol.EOEditingContext _anEditingContext_);

Overrides the inherited implementation to create a to-many fault for _anEditingContext_. _name_ must correspond to an EORelationship in the EOEntity for the specified _globalID_.

__See also:__
[`faultForGlobalID`](#apple-heydk)

---

### availableChannel

public EODatabaseChannel `availableChannel`()

Returns an EODatabaseChannel that's registered with the receiver and that isn't busy. If the method can't find a channel that meets these criteria, it posts an EODatabaseChannelNeededNotification in the hopes that someone will provide a new channel. After posting the notification, the receiver checks its list of channels again. If there are still no available channels, the receiver creates an EODatabaseChannel itself. However, if the list is not empty and there are no available channels, the method returns `null`.

__See also:__
[`registerChannel`](#apple-giztgmjr), [`registeredChannels`](#apple-gq4dqnrt), [`unregisterChannel`](#apple-geytenq)

---

### batchFetchRelationship

public void `batchFetchRelationship`(EORelationship _relationship_, NSArray _objects_, com.apple.yellow.eocontrol.EOEditingContext _anEditingContext_)

Clear all the faults for the _relationship_ of _anEditingContext_'s _objects_ and performs a single, efficient, fetch (at most two fetches, if the relationship is many-to-many). This method provides a way to fetch the same relationship for multiple objects. For example, given an array of Employee objects, this method can fetch all of their departments with one round trip to the server, rather than asking the server for each of the employee's departments individually.

---

### commitChanges

public void `commitChanges()`

Overrides the inherited implementation to instruct the adaptor to commit the transaction. If the commit is successful, any primary and foreign key changes are written back to the saved objects, database locks are released, and an EOObjectsChangedInStoreNotification (defined in com.apple.yellow.eocontrol.EOObjectStore) is posted describing the committed changes. Raises an exception if the adaptor is unable to commit the transaction; the error message indicates the nature of the problem. You should never need to invoke this method directly.

__See also:__
[`performChanges`](#apple-he3tc), [`rollbackChanges`](#apple-geydcni)

---

### coordinator

public com.apple.yellow.eocontrol.EOObjectStoreCoordinator `coordinator`()

Returns the receiver's com.apple.yellow.eocontrol.EOObjectStoreCoordinator or `null` if there is none.This method is only valid during a save operation.

---

### database

public EODatabase `database`()

Returns the receiver's EODatabase.

__See also:__
"Constructors"

---

### delegate

public java.lang.Object `delegate`()

Returns the receiver's delegate.

__See also:__
[`setDelegate`](#apple-geydemq)

---

### faultForGlobalID

public java.lang.Object `faultForGlobalID`(com.apple.yellow.eocontrol.EOGlobalID _globalID_, com.apple.yellow.eocontrol.EOEditingContext _anEditingContext_)

Overrides the inherited implementationto create a to-one fault for the object identified by _globalID_ and register it in _anEditingContext._

__See also:__
[`arrayFaultWithSourceGlobalID`](#apple-ha4da)

---

### faultForRawRow

public java.lang.Object `faultForRawRow`(java.lang.Object _row_,
java.lang.String _entityName_,
com.apple.yellow.eocontrol.EOEditingContext _editingContext_)

Returns a fault for a raw row. _row_ is the raw data, typically in the form of an NSDictionary. _entityName_ is the name of the appropriate entity for the EO you want to create (as a fault). _editingContext_ is the EOEditingContext in which to create the fault

---

### forgetAllLocks

public void `forgetAllLocks()`

Clears all of the receiver's locks. Doesn't cause the locks to be forgotten in the server, only in the receiver. This method is useful when something has happened to cause the server to forget the locks and the receiver needs to be synced up. This method is invoked whenever a transaction is committed or rolled back.

__See also:__
[`registerLockedObjectWithGlobalID`](#apple-geydcmi), [`isObjectLockedWithGlobalID`](#apple-hezto),
[`forgetLocksForObjectsWithGlobalIDs`](#apple-heytg), [`lockObjectWithGlobalID`](#apple-geytgmy),
`lockObject` (com.apple.yellow.eocontrol.EOEditingContext)

---

### forgetLocksForObjectsWithGlobalIDs

public void `forgetLocksForObjectsWithGlobalIDs`(NSArray _anImmutableVector_)

Clears the locks made for the enterprise objects identified by each of the com.apple.yellow.eocontrol.EOGlobalIDs in _globalIDs_. Doesn't cause the locks to be forgotten in the server, only in the receiver.

__See also:__
[`registerLockedObjectWithGlobalID`](#apple-geydcmi), [`isObjectLockedWithGlobalID`](#apple-hezto),
[`forgetAllLocks`](#apple-heyds),
[`lockObjectWithGlobalID`](#apple-geytgmy), `lockObject` (com.apple.yellow.eocontrol.EOEditingContext)

---

### forgetSnapshotForGlobalID

public void `forgetSnapshotForGlobalID`(com.apple.yellow.eocontrol.EOGlobalID _globalID_)

Deletes the snapshot made for the enterprise object identified by _globalID_.

__See also:__
[`recordSnapshotForGlobalID`](#apple-he4ds), [`localSnapshotForGlobalID`](#apple-he2dk), [`recordSnapshots`](#apple-geytemq),
[`snapshotForGlobalID`](#apple-gq3tomzw), [`forgetSnapshotsForGlobalIDs`](#apple-hezdc)

---

### forgetSnapshotsForGlobalIDs

public void `forgetSnapshotsForGlobalIDs`(NSArray _globalIDs_)

Deletes the snapshots made for the enterprise objects identified by _globalIDs_, an array of com.apple.yellow.eocontrol.EOGlobalID objects.

__See also:__
[`recordSnapshotForGlobalID`](#apple-he4ds), [`localSnapshotForGlobalID`](#apple-he2dk), [`recordSnapshots`](#apple-geytemq),
[`snapshotForGlobalID`](#apple-gq3tomzw)

---

### handlesFetchSpecification

public boolean `handlesFetchSpecification`(
com.apple.yellow.eocontrol.EOFetchSpecification _fetchSpecification_)

Overrides the inherited implementation to return `true` if the receiver is responsible for fetching the objects described by the entity name in _fetchSpecification_.

__See also:__
[`ownsObject`](#apple-he3do), [`ownsGlobalID`](#apple-he3dg)

---

### hasBusyChannels

public boolean `hasBusyChannels()`

Returns `true` if the receiver's EOAdaptorContext has channels that have outstanding operations (that is, have a fetch in progress), `false` otherwise.

---

### initializeObject

public void `initializeObject`(java.lang.Object _object_, com.apple.yellow.eocontrol.EOGlobalID _globalID_, com.apple.yellow.eocontrol.EOEditingContext _anEditingContext_);

Overrides the inherited implementation initialize _object_ for _anEditingContext_ by filling it with properties based on row data fetched from the adaptor. The snapshot for _globalID_ is looked up and those attributes in the snapshot that are marked as class properties in the EOEntity are assigned to _object_. For relationship class properties, faults are constructed and assigned to the object.

---

### invalidateAllObjects

public void `invalidateAllObjects`();

Overrides the inherited implementation to discard all snapshots in the receiver's EODatabase, forget all locks, and post an EOInvalidatedAllObjectsInStoreNotification, as well as an EOObjectsChangedInStoreNotification with the invalidated global IDs in the `userInfo` dictionary. Both of these notifications are defined in com.apple.yellow.eocontrol.EOObjectStore. This method works by invoking [`invalidateObjectsWithGlobalIDs`](#apple-hezti) for all of the snapshots in the receiver's EODatabase.

---

### invalidateObjectsWithGlobalIDs

public void `invalidateObjectsWithGlobalIDs`(NSArray _globalIDs_)

Overrides the inherited implementation to discard the snapshots for the objects identified by the com.apple.yellow.eocontrol.EOGlobalIDs in _globalIDs_ and broadcasts an EOObjectsChangedInStoreNotification (defined in com.apple.yellow.eocontrol.EOObjectStore), which causes the com.apple.yellow.eocontrol.EOEditingContext containing objects fetched from the receiver to refault those objects. The result is that these objects will be refetched from the database the next time they're accessed.

---

### isObjectLockedWithGlobalID

public boolean `isObjectLockedWithGlobalID`(com.apple.yellow.eocontrol.EOGlobalID _globalID_)

Returns `true` if the enterprise object identified by _globalID_ is locked, `false` otherwise.

__See also:__
[`registerLockedObjectWithGlobalID`](#apple-geydcmi), [`forgetAllLocks`](#apple-heyds),
[`forgetLocksForObjectsWithGlobalIDs`](#apple-heytg), [`lockObjectWithGlobalID`](#apple-geytgmy), `lockObject`
(com.apple.yellow.eocontrol.EOEditingContext)

__isObjectLockedWithGlobalID__ public boolean `isObjectLockedWithGlobalID`(com.apple.yellow.eocontrol.EOGlobalID _globalID,_com.apple.yellow.eocontrol.EOEditingContext _anEditingContext_)

Overrides the EOObjectStore method `isObjectLockedWithGlobalID:editingContext:` to return true if the database row corresponding to _globalID_ has been locked in an open transaction held by the receiver.

__See also:__
[`registerLockedObjectWithGlobalID`](#apple-geydcmi), [`isObjectLockedWithGlobalID`](#apple-hezto), [`forgetAllLocks`](#apple-heyds),
[`forgetLocksForObjectsWithGlobalIDs`](#apple-heytg), [`lockObjectWithGlobalID`](#apple-geytgmy),
`lockObject` (EOEditingContext)

---

### localSnapshotForGlobalID

public NSDictionary `localSnapshotForGlobalID`(com.apple.yellow.eocontrol.EOGlobalID _globalID_)

Returns the snapshot for the object identified by _globalID_, if there is one; else returns `null`. Only searches locally (in the transaction scope), not in the EODatabase.

__See also:__
[`recordSnapshotForGlobalID`](#apple-he4ds), [`forgetSnapshotForGlobalID`](#apple-heyto), [`recordSnapshots`](#apple-geytemq),
[`snapshotForGlobalID`](#apple-gq3tomzw)

---

### localSnapshotForSourceGlobalID

public NSArray `localSnapshotForSourceGlobalID`(
com.apple.yellow.eocontrol.EOGlobalID _globalID_,
java.lang.String _name_)

Returns an array that is the snapshot for the objects at the destination of the to-many relationship named _name_, which is a property of the object identified by _globalID_. The returned array contains the globalIDs of the destination objects. If there is no snapshot, returns `null`. Only searches locally (in the transaction scope), not in the EODatabase.

__See also:__
[`recordSnapshotForSourceGlobalID`](#apple-ojswg33smrjw4ylqonug65cgn5zfg33vojrwkr3mn5rgc3cjiq),
[`snapshotForSourceGlobalID`](#apple-onxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyske)

---

### lock

public void `lock`()

Used internally to protect access to the receiver in a multi-threaded environment. Do not confuse this with any methods which work with the database locking mechanism.

__See also:__
[`unlock`](#apple-gq3tqnzz)

---

### lockObjectWithGlobalID

public void `lockObjectWithGlobalID`(com.apple.yellow.eocontrol.EOGlobalID _globalID_, com.apple.yellow.eocontrol.EOEditingContext _anEditingContext_);

Overrides the inherited implementation to attempt to lock the database row corresponding to _globalID_ in the underlying database server, on behalf of _anEditingContext_. If a transaction is not already open at the time of the lock request, the transaction is begun and is held open until either `commitChanges` or `invalidateAllObjects` is invoked. At that point all locks are released. Raises an exception if unable to obtain the lock.

__See also:__
[`registerLockedObjectWithGlobalID`](#apple-geydcmi), [`isObjectLockedWithGlobalID`](#apple-hezto), [`forgetAllLocks`](#apple-heyds),
[`forgetLocksForObjectsWithGlobalIDs`](#apple-heytg), `lockObject`
(com.apple.yellow.eocontrol.EOEditingContext)

---

### objectsForSourceGlobalID

public NSArray `objectsForSourceGlobalID`(com.apple.yellow.eocontrol.EOGlobalID _globalID_, java.lang.String _name_, com.apple.yellow.eocontrol.EOEditingContext _anEditingContext_);

Overrides the inherited implementation to service a to-many fault. The snapshot for the source object identified by _globalID_ is located and the EORelationship named _name_ is used to construct a qualifier from that snapshot. This qualifier is then used to fetch the requested objects into _anEditingContext_ using the method [`objectsWithFetchSpecification`](#apple-he2tm).

---

### objectsWithFetchSpecification

public NSArray `objectsWithFetchSpecification`(com.apple.yellow.eocontrol.EOFetchSpecification _fetchSpecification_, com.apple.yellow.eocontrol.EOEditingContext _anEditingContext_);

Overrides the inherited implementation to fetch objects from an external store into _anEditingContext_. The receiver obtains an available EODatabaseChannel and issues a fetch with _fetchSpecification_. If one of these objects is already present in memory, by default this method doesn't overwrite its values with the new values from the database (you can change this behavior; see the `setRefreshesRefetchedObjects` method in the com.apple.yellow.eocontrol.EOFetchSpecification class specification).

You can fine-tune the fetching behavior by adding hints to _fetchSpecification_'s `hints` dictionary. For this purpose, EODatabaseContext defines the following keys (java.lang.Strings):

| __Constant__ | __Corresponding value in the hints dictionary__ |
| EOCustomQueryExpressionHintKey | A java.lang.String specifying raw SQL with which to perform the fetch. There is no way to pass down parameters with this hint. |
| EOStoredProcedureNameHintKey | A java.lang.String specifying a name for a stored procedure in the model that should be used rather than building the SQL statement. The stored procedure must query the the exact same attributes in the same order as EOF would query if generating the SELECT expression dynamically. If this key is supplied, other aspects of the EOFetchSpecification such as `isDeep`, `qualifier`, and `sortOrderings` are ignored (in that sense, this key is more of a directive than a hint). There is no way to pass down parameters with this hint. |

```
```

The class description contains additional information on using these hints. See "Using a Custom Query."

You can also use this method to implement "on-demand" locking by using a _fetchSpecification_ that includes locking. For more discussion of this subject, see "Updating And Locking Strategies" in the class description.

Raises an exception if an error occurs; the error message indicates the nature of the problem.

__See also:__
`objectsWithFetchSpecification` (com.apple.yellow.eocontrol.EOEditingContext)

---

### ownsGlobalID

public boolean `ownsGlobalID`(com.apple.yellow.eocontrol.EOGlobalID _globalID_)

Overrides the inherited implementation to return `true` if the receiver is responsible for fetching and saving the object identified by _globalID_, `false` otherwise. The receiver is determined to be responsible if _globalID_ is a subclass of com.apple.yellow.eocontrol.EOKeyGlobalID and _globalID_ has an entity from one of the receiver's EODatabase's EOModels.

__See also:__
[`handlesFetchSpecification`](#apple-hezdk), [`ownsObject`](#apple-he3do)

---

### ownsObject

public boolean `ownsObject`(java.lang.Object _object_)

Overrides the inherited implementation to return `true` if the receiver is responsible for fetching and saving _object_, `false` otherwise. The receiver is determined to be responsible if the entity corresponding to _object_ is in one of the receiver's EODatabase's EOModels.

__See also:__
[`ownsGlobalID`](#apple-he3dg), [`handlesFetchSpecification`](#apple-hezdk)

---

### performChanges

public void `performChanges()`

Overrides the inherited implementation to construct EOAdaptorOperations from the EODatabaseOperations produced during [`recordChangesInEditingContext`](#apple-he4dm) and [`recordUpdateForObject`](#apple-geytgni). Invokes the delegate method `databaseContextWillOrderAdaptorOperationsFromDatabaseOperations` to give the delegate an opportunity to construct alternative EOAdaptorOperations from the EODatabaseOperations. Then invokes the delegate method `databaseContext:willPerformAdaptorOperations:adaptorChannel:` to let the delegate substitute its own array of EOAdaptorOperations. Gives the EOAdaptorOperations to an available EOAdaptorChannel for execution. If the save succeeds, updates the snapshots in the receiver to reflect the new state of the server. You should never need to invoke this method directly.

This method raises an exception if the adaptor is unable to perform the operations.

__See also:__
[`commitChanges`](#apple-ha4tc), [`rollbackChanges`](#apple-geydcni)

---

### prepareForSaveWithCoordinator

public void `prepareForSaveWithCoordinator`(com.apple.yellow.eocontrol.EOObjectStoreCoordinator _anObjectStoreCoordinator_, com.apple.yellow.eocontrol.EOEditingContext _anEditingContext_)

Overrides the inherited implementation to do whatever is necessary to prepare to save changes. If needed, generates primary keys for any new objects in _anEditingContext_ that are owned by the receiver. This method is invoked before the object graph is analyzed and foreign key assignments are performed. You should never need to invoke this method directly.

---

### recordChangesInEditingContext

public void `recordChangesInEditingContext()`

Overrides the inherited implementation to construct a list of EODatabaseOperations for all changes to objects in the com.apple.yellow.eocontrol.EOEditingContext that are owned by the receiver. Forwards any relationship changes discovered but not owned by the receiver to the com.apple.yellow.eocontrol.EOObjectStoreCoordinator. This method is typically invoked in the course of an com.apple.yellow.eocontrol.EOObjectStoreCoordinator saving changes through its `saveChangesInEditingContext` method. It's invoked after [`prepareForSaveWithCoordinator`](#apple-he4dg) and before [`performChanges`](#apple-he3tc). You should never need to invoke this method directly.

---

### recordSnapshotForGlobalID

public void `recordSnapshotForGlobalID`(NSDictionary _aSnapshot_, com.apple.yellow.eocontrol.EOGlobalID _aGlobalID_)

Records _aSnapshot_ under _globalID_. This method only records snapshots locally (in the transaction scope). If you want to record snapshots globally, use the corresponding EODatabase method.

__See also:__
[`forgetSnapshotForGlobalID`](#apple-heyto), [`localSnapshotForGlobalID`](#apple-he2dk), [`recordSnapshots`](#apple-geytemq),
[`snapshotForGlobalID`](#apple-gq3tomzw)

---

### recordSnapshotForSourceGlobalID

public void `recordSnapshotForSourceGlobalID`(NSArray _globalIDs_,
com.apple.yellow.eocontrol.EOGlobalID _globalID_,
java.lang.String _name_)

For the object identified by _globalID_, records an NSArray of _globalIDs_ for the to-many relationship named _name_. These _globalIDs_ identify the objects at the destination of the relationship. This method only records snapshots locally (in the transaction scope). If you want to record snapshots globally, use the corresponding EODatabase method.

__See also:__
[`snapshotForSourceGlobalID`](#apple-onxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyske),
[`localSnapshotForSourceGlobalID`](#apple-nrxwgylmknxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyske),
[`recordToManySnapshots`](#apple-gq3tmmjy)

---

### recordSnapshots

public void `recordSnapshots`(NSDictionary _snapshots_)

Records the objects in _snapshots_, a dictionary of snapshots. The _snapshots; keys_ are GlobalIDs and its values are the corresponding snapshots represented as NSDicationaries. This method only records snapshots locally (in the transaction scope). If you want to record snapshots globally, use the corresponding EODatabase method.

__See also:__
[`recordSnapshotForGlobalID`](#apple-he4ds), [`localSnapshotForGlobalID`](#apple-he2dk), [`forgetSnapshotForGlobalID`](#apple-heyto),
[`snapshotForGlobalID`](#apple-gq3tomzw)

---

### recordToManySnapshots

public void `recordToManySnapshots`(NSDictionary _snapshots_)

Records the objects in _snapshots_. _snapshots_ should be an NSDictionary of NSDictionaries, in which the top-level dictionary has as its key the globaID of the enterprise object for which to-many relationships are being recorded. The key's value is a dictionary whose keys are the names of the Enterprise Object's to-many relationships. Each of these keys in turn has as its value an array of globalIDs that identify the objects at the destination of the relationship.

This method only records snapshots locally (in the transaction scope). If you want to record snapshots globally, use the corresponding EODatabase method.

__See also:__
[`recordSnapshotForSourceGlobalID`](#apple-ojswg33smrjw4ylqonug65cgn5zfg33vojrwkr3mn5rgc3cjiq),
[`snapshotForSourceGlobalID`](#apple-onxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyske),
[`localSnapshotForSourceGlobalID`](#apple-nrxwgylmknxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyske)

---

### recordUpdateForObject

public void `recordUpdateForObject`(java.lang.Object _object_, NSDictionary _changes_)

Overrides the inherited implementation to communicate to the receiver that _changes_ from another com.apple.yellow.eocontrol.EOCooperatingObjectStore (through the com.apple.yellow.eocontrol.EOObjectStoreCoordinator) need to be made to an _object_ in the receiver. For example, an insert of an object in a relationship property might require changing a foreign key property in an object owned by another cooperating store. This method can be invoked any time after [`prepareForSaveWithCoordinator`](#apple-he4dg) and before [`performChanges`](#apple-he3tc).

---

### refaultObject

public void `refaultObject`(java.lang.Object _object_, com.apple.yellow.eocontrol.EOGlobalID _globalID_, com.apple.yellow.eocontrol.EOEditingContext _anEditingContext_);

Overrides the inherited implementation to refault the enterprise object object identified by _globalID_ in _anEditingContext_. Newly-inserted objects should not be refaulted, since they can't be refetched from the external store. If you attempt to do this, an exception will be raised. Don't refault to-many relationship arrays, just recreate them.

This method should be used with caution since refaulting an object doesn't remove the object snapshot from the undo stack, after which the object snapshot may not refer to the proper object..

---

### registerChannel

public void `registerChannel`(EODatabaseChannel _channel_)

Registers _channel_, which means that it adds it to the pool of available channels used to service fetch and fault requests. You use this method if you need to perform more than one fetch simultaneously.

__See also:__
[`availableChannel`](#apple-ha4di), [`registeredChannels`](#apple-gq4dqnrt), [`unregisterChannel`](#apple-geytenq)

---

### registeredChannels

public NSArray `registeredChannels`()

Returns all of the EODatabaseChannels that have been registered for use with the receiver.

__See also:__
[`registerChannel`](#apple-giztgmjr), [`availableChannel`](#apple-ha4di), [`unregisterChannel`](#apple-geytenq)

---

### registerLockedObjectWithGlobalID

public void `registerLockedObjectWithGlobalID`(com.apple.yellow.eocontrol.EOGlobalID _globalID_)

Registers as a locked object the enterprise object identified by _globalID_. This method is used internally to keep track of objects corresponding to rows that are locked in the database.

__See also:__
[`forgetAllLocks`](#apple-heyds), [`isObjectLockedWithGlobalID`](#apple-hezto), [`forgetLocksForObjectsWithGlobalIDs`](#apple-heytg),
[`lockObjectWithGlobalID`](#apple-geytgmy), `lockObject` (com.apple.yellow.eocontrol.EOEditingContext)

---

### rollbackChanges

public void `rollbackChanges()`

Overrides the inherited implementation to instruct the adaptor to roll back the transaction. Rolls back any changed snapshots, and releases all locks.

__See also:__
[`performChanges`](#apple-he3tc), [`commitChanges`](#apple-ha4tc)

---

### saveChangesInEditingContext

public void `saveChangesInEditingContext`(com.apple.yellow.eocontrol.EOEditingContext _anEditingContext_);

Overrides the inherited implementation to save the changes made in _anEditingContext_. This message is sent by an com.apple.yellow.eocontrol.EOEditingContext to its com.apple.yellow.eocontrol.EOObjectStore to commit changes. Normally an editing context doesn't send this message to an EODatabaseContext, but to an com.apple.yellow.eocontrol.EOObjectStoreCoordinator. Raises an exception if an error occurs; the error message indicates the nature of the problem.

---

### setDelegate

public void `setDelegate`(java.lang.Object _delegate_)

Sets the receiver's delegate to _delegate_, and propagates the delegate to all of the receiver's EODatabaseChannels. EODatabaseChannels share the delegate of their EODatabaseContext.

__See also:__
[`delegate`](#apple-heydc)

---

### setUpdateStrategy

public void `setUpdateStrategy`(int _strategy_)

Sets the update strategy used by the EODatabaseContext to _strategy_. See "Updating And Locking Strategies" in the class description for information on the update strategies:

- EOUpdateWithOptimisticLocking
- EOUpdateWithPessimisticLocking

Raises an exception if the receiver has any transactions in progress or if you try to set _strategy_ to EOUpdateWithPessimisticLocking and the receiver's EODatabase already has snapshots.

__See also:__
[`updateStrategy`](#apple-geydgoa)

---

### snapshotForGlobalID

public NSDictionary `snapshotForGlobalID`(com.apple.yellow.eocontrol.EOGlobalID _globalID_)

Returns the snapshot for the object identified by _globalID_, if there is one; else returns `null`. Searches first locally (in the transaction scope) and then in the EODatabase.

__See also:__
[`recordSnapshotForGlobalID`](#apple-he4ds), [`localSnapshotForGlobalID`](#apple-he2dk), [`forgetSnapshotForGlobalID`](#apple-heyto),
[`recordSnapshots`](#apple-geytemq)

---

### snapshotForSourceGlobalID

public NSArray `snapshotForSourceGlobalID`(
com.apple.yellow.eocontrol.EOGlobalID _globalID_,
java.lang.String _name_)

Returns a snapshot that consists of an array of global IDs. These global IDs identify the objects at the destination of the to-many relationship named _name_, which is a property of the object identified by _globalID_. If there is no snapshot, returns `null`.

__See also:__
[`recordSnapshotForSourceGlobalID`](#apple-ojswg33smrjw4ylqonug65cgn5zfg33vojrwkr3mn5rgc3cjiq),
[`localSnapshotForSourceGlobalID`](#apple-nrxwgylmknxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyske),
[`recordToManySnapshots`](#apple-gq3tmmjy)

---

### unlock

public void `unlock`()

Used internally to release the lock that protects access to the receiver in a multi-threaded environment.

__See also:__
[`lock`](#apple-gq3tqnzq)

---

### unregisterChannel

public void `unregisterChannel`(EODatabaseChannel _channel_)

Unregisters the EODatabaseChannel _channel_, which means that it removes it from the pool of available channels used for database communication (for example, to service fetch and fault requests).

__See also:__
[`registerChannel`](#apple-giztgmjr), [`registeredChannels`](#apple-gq4dqnrt), [`availableChannel`](#apple-ha4di)

---

### updateStrategy

public int `updateStrategy()`

Returns the update strategy used by the receiver, one of:

- EOUpdateWithOptimisticLocking
- EOUpdateWithPessimisticLocking

The default strategy is EOUpdateWithOptimisticLocking. See the class description for information on update strategies.

__See also:__
[`setUpdateStrategy`](#apple-geydenq)

---

### valuesForKeys

public NSDictionary `valuesForKeys`(NSArray _keys_, java.lang.Object _object_)

Overrides the inherited implementation to return values for the specified _keys_ from the snapshot of _object_. The returned values are used primarily by another EODatabaseContext to extract foreign key properties for objects owned by the receiver.

---

# Notifications

---

### EODatabaseChannelNeededNotification

This notification is broadcast whenever an EODatabaseContext is asked to perform an object store operation and it doesn't have an available EODatabaseChannel. Subscribers can create a new channel and add it to the EODatabaseContext at this time.

| `Notification Object` | The EODatabaseContext. |
| `userInfo Dictionary` | None. |

```
```

---

[!](EODatabaseChannel.md)
[!](EODatabaseContext-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
