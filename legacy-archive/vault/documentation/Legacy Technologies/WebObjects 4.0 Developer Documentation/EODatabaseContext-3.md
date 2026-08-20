---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EODatabaseContext.html
archived_at: '2026-07-18T01:28:16.082616Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EODatabaseChannel-2.md)
[!](More%20about%20EODatabaseContext.md)

---

# EODatabaseContext

__Inherits From:__
EOCooperatingObjectStore : EOObjectStore : NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
EOAccess/EODatabaseContext.h

---

## Class Description

An EODatabaseContext object is an EOObjectStore for accessing relational databases, creating and saving objects based on EOEntity definitions in an EOModel.

An EODatabaseContext represents a single connection to a database server, and it determines the updating and locking strategy used by its EODatabaseChannel objects. An EODatabaseContext has a corresponding EODatabase object. If the server supports multiple concurrent transactions, the EODatabase object may have several database contexts. If the server and adaptor support it, a database context may in turn have several database channels, which handle access to the data on the server.

For a more information, see ["More about EODatabaseContext"](More%20about%20EODatabaseContext.md).

---

## Method Types

**Initializing instances**

**[- initWithDatabase:](#apple-guztonzz)**

**Fetching objects**

**[- objectsWithFetchSpecification:editingContext:](#apple-he2tm)

**[- objectsForSourceGlobalID:relationshipName:editingContext:](#apple-he2tg)

**[- arrayFaultWithSourceGlobalID:relationshipName:editingContext:](#apple-ha4da)

**[- batchFetchRelationship:forSourceObjects:editingContext:](#apple-ha4dq)********

**Accessing the adaptor context**

**[- adaptorContext](#apple-ha3to)**

**Accessing the database object**

**[- database](#apple-ha4tq)**

**Accessing the coordinator**

**[- coordinator](#apple-ha4tk)**

**Managing channels**

**[- availableChannel](#apple-ha4di)

**[- registerChannel:](#apple-giztgmjr)

**[- registeredChannels](#apple-gq4dqnrt)

**[- unregisterChannel:](#apple-geytenq)********

**Accessing the delegate**

**[- setDelegate:](#apple-geydemq)

**[- delegate](#apple-heydc)****

**Committing or discarding changes**

**[- invalidateAllObjects](#apple-heztc)

**[- invalidateObjectsWithGlobalIDs:](#apple-hezti)

**[- rollbackChanges](#apple-geydcni)

**[- saveChangesInEditingContext:](#apple-geydcoi)

**[- commitChanges](#apple-ha4tc)

**[- performChanges](#apple-he3tc)

**[- prepareForSaveWithCoordinator:editingContext:](#apple-he4dg)

**[- recordUpdateForObject:changes:](#apple-geytgni)

**[- recordChangesInEditingContext](#apple-he4dm)

**[- refaultObject:withGlobalID:editingContext:](#apple-giztgnbw)********************

**Determining if the EODatabaseContext is responsible for a particular operation**

**[- ownsObject:](#apple-he3do)

**[- ownsGlobalID:](#apple-he3dg)

**[- handlesFetchSpecification:](#apple-hezdk)******

**Managing Snapshots**

**[- forgetSnapshotForGlobalID:](#apple-heyto)

**[- forgetSnapshotsForGlobalIDs:](#apple-hezdc)

**[- localSnapshotForGlobalID:](#apple-he2dk)

**[- recordSnapshot:forGlobalID:](#apple-he4ds)

**[- recordSnapshots:](#apple-geytemq)

**[- snapshotForGlobalID:](#apple-gq3tomzw)

**[- recordSnapshot:forSourceGlobalID:relationshipName:](#apple-gu2dinrw)

**[- snapshotForSourceGlobalID:relationshipName:](#apple-gu2dqmrz)

**[- localSnapshotForSourceGlobalID:relationshipName:](#apple-guztsojt)

**[- recordToManySnapshots:](#apple-gq3tmmjy)********************

**Initializing objects**

**[- initializeObject:withGlobalID:editingContext:](#apple-geytaoi)**

**Obtaining an EODatabaseContext**

**[+ registeredDatabaseContextForModel:editingContext:](#apple-g42tc)**

**Locking objects**

**[- setUpdateStrategy:](#apple-geydenq)

**[- updateStrategy](#apple-geydgoa)

**[- registerLockedObjectWithGlobalID:](#apple-geydcmi)

**[- isObjectLockedWithGlobalID:](#apple-hezto)

**[- isObjectLockedWithGlobalID:editingContext:](#apple-guztqojz)

**[- forgetAllLocks](#apple-heyds)

**[- forgetLocksForObjectsWithGlobalIDs:](#apple-heytg)

**[- lockObjectWithGlobalID:editingContext:](#apple-geytgmy)****************

**Returning information about objects**

**[- valuesForKeys:object:](#apple-geydimq)**

**Setting the context class**

**[+ contextClassToRegister](#apple-gq3tcmry)

**[+ setContextClassToRegister:](#apple-gq3tcnrs)****

**Checking connection status**

**[- hasBusyChannels](#apple-gi2dcmrr)**

**Other**

**[+ forceConnectionWithModel:connectionDictionaryOverrides:
editingContext:](#apple-gq3tqnjq)

**[- lock](#apple-gq3tqnzq)

**[- unlock](#apple-gq3tqnzz)******

---

## Class Methods

---

### contextClassToRegister

+ (Class)`contextClassToRegister`

Returns the class that is registered with an EOObjectStoreCoordinator when the coordinator broadcasts an EOCooperatingObjectStoreNeeded notification. By default this is EODatabaseContext, but you can use [`setContextClassToRegister:`](#apple-gq3tcnrs) to specify your own subclass of EODatabaseContext.

When an EOObjectStoreCoordinator sends an EOCooperatingObjectStoreNeeded notification for an EOEntity in the default model group, if `contextClassToRegister` is non-`nil` (and it should be-it makes no sense to set `contextClassToRegister` to `nil`), an instance of the that class is created, the EOModel for the EOEntity is registered, and the context class is registered with the requesting EOObjectStoreCoordinator.

---

### forceConnectionWithModel:connectionDictionaryOverrides:editingContext:

+ (EODatabaseContext \*)`forceConnectionWithModel:`(EOModel \*)_amodel_`connectionDictionaryOverrides:`(NSDictionary \*)_overrides_
`editingContext:`(EOEditingContext \*)_anEditingContext_

Forces the stack of objects in the EOAccess layer to be instantiated, if necessary, and then makes a connection to the database. If there is an existing connection for _amodel_, it is first closed and then reconnected. The new connection dictionary is effectively made up of the model's connection dictionary, overlaid with _overrides_. All compatible models in the model's group also are associated with the new connection (so they share the same adaptor). Returns the EODatabaseContext associated with the model for _anEditingContext_.

---

### registeredDatabaseContextForModel:editingContext:

+ (EODatabaseContext \*)`registeredDatabaseContextForModel:`(EOModel \*)_aModel_ `editingContext:`(EOEditingContext \*)_anEditingContext_

Finds the EOObjectStoreCoordinator for _anEditingContext_ and checks to see if it already contains an EODatabaseContext cooperating store for _aModel_. If it does, it returns that EODatabaseContext. Otherwise it instantiates a new EODatabaseContext, adds it to the EOObjectStoreCoordinator, and returns the EODatabaseContext.

---

### setContextClassToRegister:

+ (void)`setContextClassToRegister:`(Class)_contextClass_

Sets to _contextClass_ the "contextClassToRegister." For more discussion of this topic, see the method description for [`contextClassToRegister`](#apple-gq3tcmry).

---

## Instance Methods

---

### adaptorContext

- (EOAdaptorContext \*)`adaptorContext`

Returns the EOAdaptorContext used by the EODatabaseContext for communication with the database server.

---

### arrayFaultWithSourceGlobalID:relationshipName:editingContext:

- (NSArray \*)`arrayFaultWithSourceGlobalID:`(EOGlobalID \*)_globalID_`relationshipName:`(NSString \*)_name_`editingContext:`(EOEditingContext \*)_anEditingContext_

Overrides the inherited implementation to create a to-many fault for _anEditingContext_. _name_ must correspond to an EORelationship in the EOEntity for the specified _globalID_.

__See also:__
[- `faultForGlobalID:editingContext:`](#apple-heydk)

---

### availableChannel

- (EODatabaseChannel \*)`availableChannel`

Returns an EODatabaseChannel that's registered with the receiver and that isn't busy. If the method can't find a channel that meets these criteria, it posts an EODatabaseChannelNeededNotification in the hopes that someone will provide a new channel. After posting the notification, the receiver checks its list of channels again. If there are still no available channels, the receiver creates an EODatabaseChannel itself. However, if the list is not empty and there are no available channels, the method returns `nil`.

__See also:__
[- `registerChannel:`](#apple-giztgmjr), [- `registeredChannels`](#apple-gq4dqnrt), [- `unregisterChannel:`](#apple-geytenq)

---

### batchFetchRelationship:forSourceObjects:editingContext:

- (void)`batchFetchRelationship:`(EORelationship \*)_relationship_
`forSourceObjects:`(NSArray \*)_objects_
`editingContext:`(EOEditingContext \*)_anEditingContext_

Clear all the faults for the _relationship_ of _anEditingContext_'s _objects_ and performs a single, efficient, fetch (at most two fetches, if the relationship is many-to-many). This method provides a way to fetch the same relationship for multiple objects. For example, given an array of Employee objects, this method can fetch all of their departments with one round trip to the server, rather than asking the server for each of the employee's departments individually.

---

### commitChanges

- (void)`commitChanges`

Overrides the inherited implementation to instruct the adaptor to commit the transaction. If the commit is successful, any primary and foreign key changes are written back to the saved objects, database locks are released, and an EOObjectsChangedInStoreNotification (defined in EOObjectStore) is posted describing the committed changes. Raises an exception if the adaptor is unable to commit the transaction; the error message indicates the nature of the problem. You should never need to invoke this method directly.

__See also:__
[- `performChanges`](#apple-he3tc), [- `rollbackChanges`](#apple-geydcni)

---

### coordinator

- (EOObjectStoreCoordinator \*)`coordinator`

Returns the receiver's EOObjectStoreCoordinator or `nil` if there is none.This method is only valid during a save operation.

---

### database

- (EODatabase \*)`database`

Returns the receiver's EODatabase.

__See also:__
[- `initWithDatabase:`](#apple-guztonzz)

---

### delegate

- (id)`delegate`

Returns the receiver's delegate.

__See also:__
[- `setDelegate:`](#apple-geydemq)

---

### faultForGlobalID:editingContext:

- (id)`faultForGlobalID:`(EOGlobalID \*)_globalID_ `editingContext:`(EOEditingContext \*)_anEditingContext_

Overrides the inherited implementationto create a to-one fault for the object identified by _globalID_ and register it in _anEditingContext._

__See also:__
[- `arrayFaultWithSourceGlobalID:relationshipName:editingContext:`](#apple-ha4da)

---

### faultForRawRow:entityNamed:editingContext:

- (id <EOEnterpriseObject>)`faultForRawRow:`(id)_row_ `entityNamed:`(NSString \*)_entityName_ `editingContext:`(EOEditingContext \*)_context_

Returns a fault for a raw row. _row_ is the raw data, typically in the form of an NSDictionary. _entityName_ is the name of the appropriate entity for the EO you want to create (as a fault). _editingContext_ is the EOEditingContext in which to create the fault

---

### forgetAllLocks

- (void)`forgetAllLocks`

Clears all of the receiver's locks. Doesn't cause the locks to be forgotten in the server, only in the receiver. This method is useful when something has happened to cause the server to forget the locks and the receiver needs to be synced up. This method is invoked whenever a transaction is committed or rolled back.

__See also:__
[- `registerLockedObjectWithGlobalID:`](#apple-geydcmi), [- `isObjectLockedWithGlobalID:`](#apple-hezto),
[- `isObjectLockedWithGlobalID:editingContext:`](#apple-guztqojz), [- `forgetLocksForObjectsWithGlobalIDs:`](#apple-heytg),
[- `lockObjectWithGlobalID:editingContext:`](#apple-geytgmy), - `lockObject:` (EOEditingContext)

---

### forgetLocksForObjectsWithGlobalIDs:

- (void)`forgetLocksForObjectsWithGlobalIDs:`(NSArray \*)_globalIDs_

Clears the locks made for the enterprise objects identified by each of the EOGlobalIDs in _globalIDs_. Doesn't cause the locks to be forgotten in the server, only in the receiver.

__See also:__
[- `registerLockedObjectWithGlobalID:`](#apple-geydcmi), [- `isObjectLockedWithGlobalID:`](#apple-hezto),
[- `isObjectLockedWithGlobalID:editingContext:`](#apple-guztqojz), [- `forgetAllLocks`](#apple-heyds),
[- `lockObjectWithGlobalID:editingContext:`](#apple-geytgmy), - `lockObject:` (EOEditingContext)

---

### forgetSnapshotForGlobalID:

- (void)`forgetSnapshotForGlobalID:`(EOGlobalID \*)_globalID_

Deletes the snapshot made for the enterprise object identified by _globalID_.

__See also:__
[- `recordSnapshot:forGlobalID:`](#apple-he4ds), [- `localSnapshotForGlobalID:`](#apple-he2dk), [- `recordSnapshots:`](#apple-geytemq),
[- `snapshotForGlobalID:`](#apple-gq3tomzw), [- `forgetSnapshotsForGlobalIDs:`](#apple-hezdc)

---

### forgetSnapshotsForGlobalIDs:

- (void)`forgetSnapshotsForGlobalIDs:`(NSArray \*)_globalIDs_

Deletes the snapshots made for the enterprise objects identified by _globalIDs_, an array of EOGlobalID objects.

__See also:__
[- `recordSnapshot:forGlobalID:`](#apple-he4ds), [- `localSnapshotForGlobalID:`](#apple-he2dk), [- `recordSnapshots:`](#apple-geytemq),
[- `snapshotForGlobalID:`](#apple-gq3tomzw)

---

### handlesFetchSpecification:

- (BOOL)`handlesFetchSpecification:`(EOFetchSpecification \*)_fetchSpecification_

Overrides the inherited implementation to return YES if the receiver is responsible for fetching the objects described by the entity name in _fetchSpecification_.

__See also:__
[- `ownsObject:`](#apple-he3do), [- `ownsGlobalID:`](#apple-he3dg)

---

### hasBusyChannels

- (BOOL)`hasBusyChannels`

Returns YES if the receiver's EOAdaptorContext has channels that have outstanding operations (that is, have a fetch in progress), NO otherwise.

---

### initializeObject:withGlobalID:editingContext:

- (void)`initializeObject:`(id)_object_
`withGlobalID:`(EOGlobalID \*)_globalID_
`editingContext:`(EOEditingContext \*)_anEditingContext_

Overrides the inherited implementation initialize _object_ for _anEditingContext_ by filling it with properties based on row data fetched from the adaptor. The snapshot for _globalID_ is looked up and those attributes in the snapshot that are marked as class properties in the EOEntity are assigned to _object_. For relationship class properties, faults are constructed and assigned to the object.

---

### initWithDatabase:

- `initWithDatabase:`(EODatabase \*)_aDatabase_

Initializes a newly allocated EODatabaseContext with _aDatabase_ as the EODatabase object it works with. The new EODatabaseContext retains _aDatabase_. Returns `self`, or `nil` if unable to create another EOAdaptorContext for the EOAdaptor of _aDatabase_. This is the designated initializer for the EODatabaseContext class.

---

### invalidateAllObjects

- (void)`invalidateAllObjects`

Overrides the inherited implementation to discard all snapshots in the receiver's EODatabase, forget all locks, and post an EOInvalidatedAllObjectsInStoreNotification, as well as an EOObjectsChangedInStoreNotification with the invalidated global IDs in the `userInfo` dictionary. Both of these notifications are defined in EOObjectStore. This method works by invoking [- `invalidateObjectsWithGlobalIDs:`](#apple-hezti) for all of the snapshots in the receiver's EODatabase.

---

### invalidateObjectsWithGlobalIDs:

- (void)`invalidateObjectsWithGlobalIDs:`(NSArray \*)_globalIDs_

Overrides the inherited implementation to discard the snapshots for the objects identified by the EOGlobalIDs in _globalIDs_ and broadcasts an EOObjectsChangedInStoreNotification (defined in EOObjectStore), which causes the EOEditingContext containing objects fetched from the receiver to refault those objects. The result is that these objects will be refetched from the database the next time they're accessed.

---

### isObjectLockedWithGlobalID:

- (BOOL)`isObjectLockedWithGlobalID:`(EOGlobalID \*)_globalID_

Returns YES if the enterprise object identified by _globalID_ is locked, NO otherwise.

__See also:__
[- `registerLockedObjectWithGlobalID:`](#apple-geydcmi), [- `forgetAllLocks`](#apple-heyds), `[- isObjectLockedWithGlobalID:
editingContext:](#apple-guztqojz)`, [- `forgetLocksForObjectsWithGlobalIDs:`](#apple-heytg), [- `lockObjectWithGlobalID:
editingContext:`](#apple-geytgmy), - `lockObject:` (EOEditingContext)

---

### isObjectLockedWithGlobalID:editingContext:

- (BOOL)`isObjectLockedWithGlobalID:`(EOGlobalID \*)_globalID_ `editingContext:`(EOEditingContext \*)_anEditingContext_

Overrides the EOObjectStore method `isObjectLockedWithGlobalID:editingContext:` to return YES if the database row corresponding to _globalID_ has been locked in an open transaction held by the receiver.

__See also:__
[- `registerLockedObjectWithGlobalID:`](#apple-geydcmi), [- `isObjectLockedWithGlobalID:`](#apple-hezto), [- `forgetAllLocks`](#apple-heyds),
[- `forgetLocksForObjectsWithGlobalIDs:`](#apple-heytg), [- `lockObjectWithGlobalID:editingContext:`](#apple-geytgmy),
- `lockObject:` (EOEditingContext)

---

### localSnapshotForGlobalID:

- (NSDictionary \*)`localSnapshotForGlobalID:`(EOGlobalID \*)_globalID_

Returns the snapshot for the object identified by _globalID_, if there is one; else returns `nil`. Only searches locally (in the transaction scope), not in the EODatabase.

__See also:__
[- `recordSnapshot:forGlobalID:`](#apple-he4ds), [- `forgetSnapshotForGlobalID:`](#apple-heyto), [- `recordSnapshots:`](#apple-geytemq),
[- `snapshotForGlobalID:`](#apple-gq3tomzw)

---

### localSnapshotForSourceGlobalID:relationshipName:

- (NSArray \*)`localSnapshotForSourceGlobalID:`(EOGlobalID \*)_globalID_ `relationshipName:`(NSString \*)_name_

Returns an array that is the snapshot for the objects at the destination of the to-many relationship named _name_, which is a property of the object identified by _globalID_. The returned array contains the globalIDs of the destination objects. If there is no snapshot, returns `nil`. Only searches locally (in the transaction scope), not in the EODatabase.

__See also:__
[- `recordSnapshot:forSourceGlobalID:relationshipName:`](#apple-gu2dinrw), [- `snapshotForSourceGlobalID:
relationshipName:`](#apple-gu2dqmrz)

---

### lock

- (void)`lock`

Used internally to protect access to the receiver in a multi-threaded environment. Do not confuse this with any methods which work with the database locking mechanism.

__See also:__
[- `unlock`](#apple-gq3tqnzz)

---

### lockObjectWithGlobalID:editingContext:

- (void)`lockObjectWithGlobalID:`(EOGlobalID \*)_globalID_
`editingContext:`(EOEditingContext \*)_anEditingContext_

Overrides the inherited implementation to attempt to lock the database row corresponding to _globalID_ in the underlying database server, on behalf of _anEditingContext_. If a transaction is not already open at the time of the lock request, the transaction is begun and is held open until either `commitChanges` or `invalidateAllObjects` is invoked. At that point all locks are released. Raises an NSInternalInconsistencyException if unable to obtain the lock.

__See also:__
[- `registerLockedObjectWithGlobalID:`](#apple-geydcmi), [- `isObjectLockedWithGlobalID:`](#apple-hezto), [- `forgetAllLocks`](#apple-heyds),
[- `forgetLocksForObjectsWithGlobalIDs:`](#apple-heytg), - `lockObject:` (EOEditingContext)

---

### objectsForSourceGlobalID:relationshipName:editingContext:

- (NSArray \*)`objectsForSourceGlobalID:`(EOGlobalID \*)_globalID_`relationshipName:`(NSString \*)_name_`editingContext:`(EOEditingContext \*)_anEditingContext_

Overrides the inherited implementation to service a to-many fault. The snapshot for the source object identified by _globalID_ is located and the EORelationship named _name_ is used to construct a qualifier from that snapshot. This qualifier is then used to fetch the requested objects into _anEditingContext_ using the method [`objectsWithFetchSpecification:editingContext:`](#apple-he2tm).

---

### objectsWithFetchSpecification:editingContext:

- (NSArray \*)`objectsWithFetchSpecification:`(EOFetchSpecification \*)_fetchSpecification_ `editingContext:`(EOEditingContext \*)_anEditingContext_

Overrides the inherited implementation to fetch objects from an external store into _anEditingContext_. The receiver obtains an available EODatabaseChannel and issues a fetch with _fetchSpecification_. If one of these objects is already present in memory, by default this method doesn't overwrite its values with the new values from the database (you can change this behavior; see the `setRefreshesRefetchedObjects:` method in the EOFetchSpecification class specification).

You can fine-tune the fetching behavior by adding hints to _fetchSpecification_'s `hints` dictionary. For this purpose, Enterprise Objects Framework defines the following keys (NSStrings):

| __Constant__ | __Corresponding value in the hints dictionary__ |
| EOCustomQueryExpressionHintKey | An NSString specifying raw SQL with which to perform the fetch. There is no way to pass down parameters with this hint. |
| EOStoredProcedureNameHintKey | An NSString specifying a name for a stored procedure in the model that should be used rather than building the SQL statement. The stored procedure must query the the exact same attributes in the same order as EOF would query if generating the SELECT expression dynamically. If this key is supplied, other aspects of the EOFetchSpecification such as `isDeep`, `qualifier`, and `sortOrderings` are ignored (in that sense, this key is more of a directive than a hint). There is no way to pass down parameters with this hint. |

```
```

The class description contains additional information on using these hints. See "Using a Custom Query."

You can also use this method to implement "on-demand" locking by using a _fetchSpecification_ that includes locking. For more discussion of this subject, see "Updating And Locking Strategies" in the class description.

Raises an exception if an error occurs; the error message indicates the nature of the problem.

__See also:__
- `objectsWithFetchSpecification:` (EOEditingContext)

---

### ownsGlobalID:

- (BOOL)`ownsGlobalID:`(EOGlobalID \*)_globalID_

Overrides the inherited implementation to return YES if the receiver is responsible for fetching and saving the object identified by _globalID_, NO otherwise. The receiver is determined to be responsible if _globalID_ is a subclass of EOKeyGlobalID and _globalID_ has an entity from one of the receiver's EODatabase's EOModels.

__See also:__
[- `handlesFetchSpecification:`](#apple-hezdk), [- `ownsObject:`](#apple-he3do)

---

### ownsObject:

- (BOOL)`ownsObject:`(id)_object_

Overrides the inherited implementation to return YES if the receiver is responsible for fetching and saving _object_, NO otherwise. The receiver is determined to be responsible if the entity corresponding to _object_ is in one of the receiver's EODatabase's EOModels.

__See also:__
[- `ownsGlobalID:`](#apple-he3dg), [- `handlesFetchSpecification:`](#apple-hezdk)

---

### performChanges

- (void)`performChanges`

Overrides the inherited implementation to construct EOAdaptorOperations from the EODatabaseOperations produced during [`recordChangesInEditingContext`](#apple-he4dm) and [`recordUpdateForObject:changes:`](#apple-geytgni). Invokes the delegate method `databaseContext:willOrderAdaptorOperationsFromDatabaseOperations:` to give the delegate an opportunity to construct alternative EOAdaptorOperations from the EODatabaseOperations. Then invokes the delegate method `databaseContext:willPerformAdaptorOperations:adaptorChannel:` to let the delegate substitute its own array of EOAdaptorOperations. Gives the EOAdaptorOperations to an available EOAdaptorChannel for execution. If the save succeeds, updates the snapshots in the receiver to reflect the new state of the server. You should never need to invoke this method directly.

This method raises an exception if the adaptor is unable to perform the operations. The exception's userInfo dictionary contains these keys:

- EODatabaseContextKey
  The EODatabaseContext object that was trying to save to its underlying repository when the exception was raised.
- EODatabaseOperationsKey
  The list of database operations the EODatabaseContext was trying to perform when the failure occurred.
- EOFailedDatabaseOperationKey
  The database operation the EODatabaseContext failed to perform.

The userInfo dictionary may also contain some of the keys listed in the method description for the EOAdaptorChannel method `performAdaptorOperation:`. For more information, see the EOAdaptorChannel class specification.

__See also:__
[- `commitChanges`](#apple-ha4tc), [- `rollbackChanges`](#apple-geydcni)

---

### prepareForSaveWithCoordinator:editingContext:

- (void)`prepareForSaveWithCoordinator:`(EOObjectStoreCoordinator \*)_coordinator_ `editingContext:`(EOEditingContext \*)_anEditingContext_

Overrides the inherited implementation to do whatever is necessary to prepare to save changes. If needed, generates primary keys for any new objects in _anEditingContext_ that are owned by the receiver. This method is invoked before the object graph is analyzed and foreign key assignments are performed. You should never need to invoke this method directly.

---

### recordChangesInEditingContext

- (void)`recordChangesInEditingContext`

Overrides the inherited implementation to construct a list of EODatabaseOperations for all changes to objects in the EOEditingContext that are owned by the receiver. Forwards any relationship changes discovered but not owned by the receiver to the EOObjectStoreCoordinator. This method is typically invoked in the course of an EOObjectStoreCoordinator saving changes through its `saveChangesInEditingContext:` method. It's invoked after [`prepareForSaveWithCoordinator:editingContext:`](#apple-he4dg) and before [`performChanges`](#apple-he3tc). You should never need to invoke this method directly.

---

### recordSnapshot:forGlobalID:

- (void)`recordSnapshot:`(NSDictionary \*)_snapshot_ `forGlobalID:`(EOGlobalID \*)_globalID_

Records _aSnapshot_ under _globalID_. This method only records snapshots locally (in the transaction scope). If you want to record snapshots globally, use the corresponding EODatabase method.

__See also:__
[- `forgetSnapshotForGlobalID:`](#apple-heyto), [- `localSnapshotForGlobalID:`](#apple-he2dk), [- `recordSnapshots:`](#apple-geytemq),
[- `snapshotForGlobalID:`](#apple-gq3tomzw)

---

### recordSnapshot:forSourceGlobalID:relationshipName:

- (void)`recordSnapshot:`(NSArray \*)_globalIDs_ `forSourceGlobalID:`(EOGlobalID \*)_globalID_ `relationshipName:`(NSString \*)_name_

For the object identified by _globalID_, records an NSArray of _globalIDs_ for the to-many relationship named _name_. These _globalIDs_ identify the objects at the destination of the relationship. This method only records snapshots locally (in the transaction scope). If you want to record snapshots globally, use the corresponding EODatabase method.

__See also:__
[- `snapshotForSourceGlobalID:relationshipName:`](#apple-gu2dqmrz), [- `localSnapshotForSourceGlobalID:
relationshipName:`](#apple-guztsojt), [- `recordToManySnapshots:`](#apple-gq3tmmjy)

---

### recordSnapshots:

- (void)`recordSnapshots:`(NSDictionary \*)_snapshots_

Records the objects in _snapshots_, a dictionary of snapshots. The _snapshots; keys_ are GlobalIDs and its values are the corresponding snapshots represented as NSDicationaries. This method only records snapshots locally (in the transaction scope). If you want to record snapshots globally, use the corresponding EODatabase method.

__See also:__
[- `recordSnapshot:forGlobalID:`](#apple-he4ds), [- `localSnapshotForGlobalID:`](#apple-he2dk),
[- `forgetSnapshotForGlobalID:`](#apple-heyto), [- `snapshotForGlobalID:`](#apple-gq3tomzw)

---

### recordToManySnapshots:

- (void)`recordToManySnapshots:`(NSDictionary \*)_snapshots_

Records the objects in _snapshots_. _snapshots_ should be an NSDictionary of NSDictionaries, in which the top-level dictionary has as its key the globaID of the enterprise object for which to-many relationships are being recorded. The key's value is a dictionary whose keys are the names of the Enterprise Object's to-many relationships. Each of these keys in turn has as its value an array of globalIDs that identify the objects at the destination of the relationship.

This method only records snapshots locally (in the transaction scope). If you want to record snapshots globally, use the corresponding EODatabase method.

__See also:__
[- `recordSnapshot:forSourceGlobalID:relationshipName:`](#apple-gu2dinrw), [- `snapshotForSourceGlobalID:
relationshipName:`](#apple-gu2dqmrz), [- `localSnapshotForSourceGlobalID:relationshipName:`](#apple-guztsojt)

---

### recordUpdateForObject:changes:

- (void)`recordUpdateForObject:`(id)_object_ `changes:`(NSDictionary \*)_changes_

Overrides the inherited implementation to communicate to the receiver that _changes_ from another EOCooperatingObjectStore (through the EOObjectStoreCoordinator) need to be made to an _object_ in the receiver. For example, an insert of an object in a relationship property might require changing a foreign key property in an object owned by another cooperating store. This method can be invoked any time after [`prepareForSaveWithCoordinator:editingContext:`](#apple-he4dg) and before [`performChanges`](#apple-he3tc).

---

### refaultObject:withGlobalID:editingContext:

- (void)`refaultObject:`(id)_anObject_`withGlobalID:`(EOGlobalID \*)_globalID_`editingContext:`(EOEditingContext \*)_anEditingContext_

Overrides the inherited implementation to refault the enterprise object object identified by _globalID_ in _anEditingContext_. Newly-inserted objects should not be refaulted, since they can't be refetched from the external store. If you attempt to do this, an exception will be raised. Don't refault to-many relationship arrays, just recreate them.

This method should be used with caution since refaulting an object doesn't remove the object snapshot from the undo stack, after which the object snapshot may not refer to the proper object..

---

### registerChannel:

- (void)`registerChannel:`(EODatabaseChannel \*)_channel_

Registers _channel_, which means that it adds it to the pool of available channels used to service fetch and fault requests. Registered channels are retained by the receiver. You use this method if you need to perform more than one fetch simultaneously.

__See also:__
[- `availableChannel`](#apple-ha4di), [- `registeredChannels`](#apple-gq4dqnrt), [- `unregisterChannel:`](#apple-geytenq)

---

### registeredChannels

- (NSArray \*)`registeredChannels`

Returns all of the EODatabaseChannels that have been registered for use with the receiver.

__See also:__
[- `registerChannel:`](#apple-giztgmjr), [- `availableChannel`](#apple-ha4di), [- `unregisterChannel:`](#apple-geytenq)

---

### registerLockedObjectWithGlobalID:

- (void)`registerLockedObjectWithGlobalID:`(EOGlobalID \*)_globalID_

Registers as a locked object the enterprise object identified by _globalID_. This method is used internally to keep track of objects corresponding to rows that are locked in the database.

__See also:__
[- `forgetAllLocks`](#apple-heyds), [- `isObjectLockedWithGlobalID:`](#apple-hezto),
[- `forgetLocksForObjectsWithGlobalIDs:`](#apple-heytg), [- `lockObjectWithGlobalID:editingContext:`](#apple-geytgmy),
- `lockObject:` (EOEditingContext)

---

### rollbackChanges

- (void)`rollbackChanges`

Overrides the inherited implementation to instruct the adaptor to roll back the transaction. Rolls back any changed snapshots, and releases all locks.

__See also:__
[- `performChanges`](#apple-he3tc), [- `commitChanges`](#apple-ha4tc)

---

### saveChangesInEditingContext:

- (void)`saveChangesInEditingContext:`(EOEditingContext \*)_anEditingContext_

Overrides the inherited implementation to save the changes made in _anEditingContext_. This message is sent by an EOEditingContext to its EOObjectStore to commit changes. Normally an editing context doesn't send this message to an EODatabaseContext, but to an EOObjectStoreCoordinator. Raises an exception if an error occurs; the error message indicates the nature of the problem.

---

### setDelegate:

- (void)`setDelegate:`(id)_delegate_

Sets the receiver's delegate to _delegate_, and propagates the delegate to all of the receiver's EODatabaseChannels. EODatabaseChannels share the delegate of their EODatabaseContext.

__See also:__
[- `delegate`](#apple-heydc)

---

### setUpdateStrategy:

- (void)`setUpdateStrategy:`(EOUpdateStrategy)_strategy_

Sets the update strategy used by the EODatabaseContext to _strategy_. See "Updating And Locking Strategies" in the class description for information on the update strategies:

- EOUpdateWithOptimisticLocking
- EOUpdateWithPessimisticLocking

Raises an NSInvalidArgumentException if the receiver has any transactions in progress or if you try to set _strategy_ to EOUpdateWithPessimisticLocking and the receiver's EODatabase already has snapshots.

__See also:__
[- `updateStrategy`](#apple-geydgoa)

---

### snapshotForGlobalID:

- (NSDictionary \*)`snapshotForGlobalID:`(EOGlobalID \*)_globalID_

Returns the snapshot for the object identified by _globalID_, if there is one; else returns `nil`. Searches first locally (in the transaction scope) and then in the EODatabase.

__See also:__
[- `recordSnapshot:forGlobalID:`](#apple-he4ds), [- `localSnapshotForGlobalID:`](#apple-he2dk),
[- `forgetSnapshotForGlobalID:`](#apple-heyto), [- `recordSnapshots:`](#apple-geytemq)

---

### snapshotForSourceGlobalID:relationshipName:

- (NSArray \*)`snapshotForSourceGlobalID:`(EOGlobalID \*)_globalID_
`relationshipName:`(NSString \*)_name_

Returns a snapshot that consists of an array of global IDs. These global IDs identify the objects at the destination of the to-many relationship named _name_, which is a property of the object identified by _globalID_. If there is no snapshot, returns `nil`.

__See also:__
[- `recordSnapshot:forSourceGlobalID:relationshipName:`](#apple-gu2dinrw),
[- `localSnapshotForSourceGlobalID:relationshipName:`](#apple-guztsojt), [- `recordToManySnapshots:`](#apple-gq3tmmjy)

---

### unlock

- (void)`unlock`

Used internally to release the lock that protects access to the receiver in a multi-threaded environment.

__See also:__
[- `lock`](#apple-gq3tqnzq)

---

### unregisterChannel:

- (void)`unregisterChannel:`(EODatabaseChannel \*)_channel_

Unregisters the EODatabaseChannel _channel_, which means that it removes it from the pool of available channels used for database communication (for example, to service fetch and fault requests).

__See also:__
[- `registerChannel:`](#apple-giztgmjr), [- `registeredChannels`](#apple-gq4dqnrt), [- `availableChannel`](#apple-ha4di)

---

### updateStrategy

- (EOUpdateStrategy)`updateStrategy`

Returns the update strategy used by the receiver, one of:

- EOUpdateWithOptimisticLocking
- EOUpdateWithPessimisticLocking

The default strategy is EOUpdateWithOptimisticLocking. See the class description for information on update strategies.

__See also:__
[- `setUpdateStrategy:`](#apple-geydenq)

---

### valuesForKeys:object:

- (NSDictionary \*)`valuesForKeys:`(NSArray \*)_keys_ `object:`(id)_object_

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

[!](EODatabaseChannel-2.md)
[!](More%20about%20EODatabaseContext.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
