---
title: NSPersistentStoreCoordinator
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstorecoordinator
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator.json'
content_hash: 'sha256:ece5f86c7dac6ab9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreCoordinator

<sub>Class</sub>

An object that enables an app’s contexts and the underlying persistent stores to work together.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPersistentStoreCoordinator
```

## Overview

A managed object context uses a coordinator to facilitate the persistence of its entities in the coordinator’s registered stores. A context can’t function without a coordinator because it relies on the coordinator’s access to the managed object model. The coordinator presents its registered stores as an aggregate, allowing a context to operate on the union of those stores instead of on each individually. A coordinator performs its work on a private queue and executes that work serially. You can use multiple coordinators if the work requires separate queues.

Use a coordinator to add or remove persistent stores, change the type or location on-disk of those stores, query the metadata of a specific store, defer a store’s migrations, determine whether two objects originate from the same store, and so on.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSLocking](../foundation/nslocking.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a persistent store coordinator

- [- initWithManagedObjectModel:](<nspersistentstorecoordinator/init(managedobjectmodel_).md>) — Creates a persistent store coordinator with the specified managed object model.
- [Store options](store-options.md) — The options keys that configure the behavior and characteristics of a persistent store.
- [Migration options](migration-options.md) — The options keys that configure the migration behavior of a persistent store.
- [Store versions](store-versions.md) — The metadata keys you use when comparing store versions.

### Managing configuration

- [name](nspersistentstorecoordinator/name.md) — The coordinator’s name.
- [managedObjectModel](nspersistentstorecoordinator/managedobjectmodel.md) — The coordinator’s managed object model.
- [persistentStores](nspersistentstorecoordinator/persistentstores.md) — The coordinator’s persistent stores.

### Registering store types

- [registerStoreClass(_:type:)](<nspersistentstorecoordinator/registerstoreclass(__type_).md>) — Registers a persistent store subclass using the specified store type.
- [+ registerStoreClass:forStoreType:](<nspersistentstorecoordinator/registerstoreclass(__forstoretype_).md>) — Registers a persistent store subclass using the specified store type identifier. _(deprecated)_
- [registeredStoreTypes](nspersistentstorecoordinator/registeredstoretypes.md) — The coordinator’s registered store types.

### Adding or removing a store

- [addPersistentStore(type:configuration:at:options:)](<nspersistentstorecoordinator/addpersistentstore(type_configuration_at_options_).md>) — Adds a specific type of persistent store at the provided location.
- [- addPersistentStoreWithType:configuration:URL:options:error:](<nspersistentstorecoordinator/addpersistentstore(oftype_configurationname_at_options_).md>) — Adds a specific type of persistent store at the provided location. _(deprecated)_
- [- addPersistentStoreWithDescription:completionHandler:](<nspersistentstorecoordinator/addpersistentstore(with_completionhandler_).md>) — Adds a persistent store using the provided description.
- [- removePersistentStore:error:](<nspersistentstorecoordinator/remove(__).md>) — Removes the specified persistent store from the coordinator.

### Modifying a store

- [destroyPersistentStore(at:type:options:)](<nspersistentstorecoordinator/destroypersistentstore(at_type_options_).md>) — Deletes a specific type of persistent store at the provided location.
- [migratePersistentStore(_:to:options:type:)](<nspersistentstorecoordinator/migratepersistentstore(__to_options_type_).md>) — Changes the location and, if necessary, the store type of the specified persistent store.
- [replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:type:)](<nspersistentstorecoordinator/replacepersistentstore(at_destinationoptions_withpersistentstorefrom_sourceoptions_type_).md>) — Replaces one persistent store with another.
- [- destroyPersistentStoreAtURL:withType:options:error:](<nspersistentstorecoordinator/destroypersistentstore(at_oftype_options_).md>) — Deletes a specific type of persistent store at the provided location. _(deprecated)_
- [- migratePersistentStore:toURL:options:withType:error:](<nspersistentstorecoordinator/migratepersistentstore(__to_options_withtype_).md>) — Changes the location and, if necessary, the store type of the specified persistent store. _(deprecated)_
- [- replacePersistentStoreAtURL:destinationOptions:withPersistentStoreFromURL:sourceOptions:storeType:error:](<nspersistentstorecoordinator/replacepersistentstore(at_destinationoptions_withpersistentstorefrom_sourceoptions_oftype_).md>) — Replaces one persistent store with another. _(deprecated)_

### Managing a store’s location

- [- setURL:forPersistentStore:](<nspersistentstorecoordinator/seturl(__for_).md>) — Changes the location of the specified persistent store.
- [- persistentStoreForURL:](<nspersistentstorecoordinator/persistentstore(for_).md>) — Returns the persistent store for the specified file URL.
- [- URLForPersistentStore:](<nspersistentstorecoordinator/url(for_).md>) — Returns the location of the provided persistent store.

### Managing a store’s metadata

- [setMetadata(_:type:at:options:)](<nspersistentstorecoordinator/setmetadata(__type_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location.
- [metadataForPersistentStore(type:at:options:)](<nspersistentstorecoordinator/metadataforpersistentstore(type_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location.
- [+ setMetadata:forPersistentStoreOfType:URL:options:error:](<nspersistentstorecoordinator/setmetadata(__forpersistentstoreoftype_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:options:error:](<nspersistentstorecoordinator/metadataforpersistentstore(oftype_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [- metadataForPersistentStore:](<nspersistentstorecoordinator/metadata(for_).md>) — Returns the metadata of the specified persistent store.
- [- setMetadata:forPersistentStore:](<nspersistentstorecoordinator/setmetadata(__for_).md>) — Updates the metadata for the specified persistent store.
- [NSStoreTypeKey](nsstoretypekey.md) — A key that identifies the store type.
- [NSStoreUUIDKey](nsstoreuuidkey.md) — A key that provides the store’s UUID.

### Deferring a store’s migrations

- [NSPersistentStoreDeferredLightweightMigrationOptionKey](nspersistentstoredeferredlightweightmigrationoptionkey.md) — The key for enabling deferred lightweight migrations.
- [- finishDeferredLightweightMigrationTask:](<nspersistentstorecoordinator/finishdeferredlightweightmigrationtask().md>) — Executes a single pending task of a deferred lightweight migration.
- [- finishDeferredLightweightMigration:](<nspersistentstorecoordinator/finishdeferredlightweightmigration().md>) — Executes all remaining tasks of a deferred lightweight migration.

### Performing tasks

- [perform(_:)](<nspersistentstorecoordinator/perform(__)-74udx.md>) — Executes the provided closure asynchronously on the coordinator’s queue and awaits the result.
- [performAndWait(_:)](<nspersistentstorecoordinator/performandwait(__)-15ude.md>) — Executes the provided closure on the coordinator’s queue and waits for it to finish.
- [- performBlock:](<nspersistentstorecoordinator/perform(__)-7jqb.md>) — Executes the provided closure asynchronously on the coordinator’s queue. _(deprecated)_
- [- performBlockAndWait:](<nspersistentstorecoordinator/performandwait(__)-d3kq.md>) — Executes the provided closure on the coordinator’s queue and waits for it to finish. _(deprecated)_
- [- executeRequest:withContext:error:](<nspersistentstorecoordinator/execute(__with_).md>) — Executes the specified request on each of the coordinator’s persistent stores.

### Maintaining a record of changes

- [NSPersistentHistoryTrackingKey](nspersistenthistorytrackingkey.md) — The key you use to enable persistent history tracking.
- [- currentPersistentHistoryTokenFromStores:](<nspersistentstorecoordinator/currentpersistenthistorytoken(fromstores_).md>) — Returns a single persistent history token representing all of the specified stores.

### Integrating with Spotlight

- [NSCoreDataCoreSpotlightExporter](nscoredatacorespotlightexporter.md) — The key you use to specify your Core Spotlight delegate.
- [NSCoreDataCoreSpotlightDelegate](nscoredatacorespotlightdelegate.md) — A set of methods that enable integration with Core Spotlight.
- [Spotlight record keys](spotlight-record-keys.md) — The keys for the values that exist in Spotlight’s external record files.
- [Showcase App Data in Spotlight](showcase-app-data-in-spotlight.md) — Index app data so users can find it by using Spotlight search.

### Getting individual object identifiers

- [- managedObjectIDForURIRepresentation:](<nspersistentstorecoordinator/managedobjectid(forurirepresentation_).md>) — Returns the object identifier for the specified URI representation.

### Responding to changes of the coordinator’s registered stores

- [NSPersistentStoreCoordinatorStoresWillChange](../foundation/nsnotification/name-swift.struct/nspersistentstorecoordinatorstoreswillchange.md) — A notification that posts before a coordinator changes its registered stores.
- [NSPersistentStoreCoordinatorStoresDidChange](../foundation/nsnotification/name-swift.struct/nspersistentstorecoordinatorstoresdidchange.md) — A notification that the coordinator posts after its registered stores change.
- [NSPersistentStoreCoordinatorWillRemoveStore](../foundation/nsnotification/name-swift.struct/nspersistentstorecoordinatorwillremovestore.md) — A notification that posts before a coordinator removes a store.
- [Notification keys](notification-keys.md) — The keys you use to retrieve values from a notification’s user info dictionary.

### Deprecated

- [Deprecated Symbols](nspersistentstorecoordinator-deprecated-symbols.md) — Review unsupported symbols and their replacements.

### Instance Methods

- [managedObjectID(for:)](<nspersistentstorecoordinator/managedobjectid(for_).md>)

### Structures

- [RemoteChangeMessage](nspersistentstorecoordinator/remotechangemessage.md) — Posted when a store receives a remote change notification from another process.
- [StoresDidChangeAsyncMessage](nspersistentstorecoordinator/storesdidchangeasyncmessage.md) — Posted when stores are added to or removed from the persistent store coordinator on a background queue.
- [StoresDidChangeMessage](nspersistentstorecoordinator/storesdidchangemessage.md) — Posted when stores are added to or removed from the persistent store coordinator on the main queue.

### Type Methods

- [+ cachedModelForPersistentStoreAtURL:options:error:](<nspersistentstorecoordinator/cachedmodelforpersistentstore(at_options_).md>)

## See Also

### Store Coordination

- [NSPersistentStore](nspersistentstore.md) — The abstract base class for all Core Data persistent stores.
- [NSPersistentStoreDescription](nspersistentstoredescription.md) — A description object used to create and load a persistent store.
- [NSPersistentStoreRequest](nspersistentstorerequest.md) — Criteria used to retrieve data from or save data to a persistent store.
- [NSPersistentStoreResult](nspersistentstoreresult.md) — The abstract base class for results returned from a persistent store coordinator.
- [NSPersistentStoreAsynchronousResult](nspersistentstoreasynchronousresult.md) — A concrete class used to represent the results of an asynchronous request.
- [NSSaveChangesRequest](nssavechangesrequest.md) — An encapsulation of a collection of changes to be made by an object store in response to a save operation on a managed object context.
- [NSAtomicStore](nsatomicstore.md) — An abstract superclass that you subclass to create a Core Data atomic store.
- [NSAtomicStoreCacheNode](nsatomicstorecachenode.md) — A concrete class that you use to represent basic nodes in a Core Data atomic store.
- [NSIncrementalStore](nsincrementalstore.md) — An abstract superclass defining the API through which Core Data communicates with a store.
- [NSIncrementalStoreNode](nsincrementalstorenode.md) — A concrete class used to represent basic nodes in a Core Data incremental store.
