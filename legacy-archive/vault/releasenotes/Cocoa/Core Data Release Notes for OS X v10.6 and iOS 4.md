---
title: Core Data Release Notes for OS X v10.6 and iOS 4
apple_id: TP40009367
resource_type: Release Note
platform: iOS|macOS
topic: Data Management
technology: CoreData
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/releasenotes/Cocoa/RN_CoreData106/index.html
archived_at: '2026-07-18T02:50:22.876728Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Core Data Release Notes for OS X v10.6 and iOS 4

This article summarizes some of the new features and changes in functionality in Core Data in OS X v10.6 and iOS 4.

#### Contents:

- [Lightweight Migration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tgnrxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Improved Fetch Performance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tgnrxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Expanded Predicate Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tgnrxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [Spotlight Integration in OS X](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tgnrxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6na)
- [Other New API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tgnrxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ni)

### Lightweight Migration

The store migration feature has been improved to automatically handle certain deterministic scenarios.

If you just make simple changes to your model (such as adding a new attribute to an entity), Core Data can perform automatic data migration, referred to as lightweight migration. Lightweight migration is fundamentally the same as ordinary migration, except that instead of you providing a mapping model, Core Data infers one from differences between the source and destination managed object models.

Lightweight migration is especially convenient during early stages of application development, when you may be changing your managed object model frequently, but you don’t want to have to keep regenerating test data. You can migrate existing data without having to create a custom mapping model for every model version used to create a store that would need to be migrated.

A further advantage of using lightweight migration—beyond the fact that you don’t need to create the mapping model yourself—is that if you use an inferred model and you use the SQLite store, then Core Data can perform the migration in situ (solely by issuing SQL statements). This can represent a significant performance benefit as Core Data doesn’t have to load any of your data. Because of this, you are encouraged to use inferred migration where possible, even if the mapping model you might create yourself would be trivial.

To lean more, consult Lightweight Migration in _[Core Data Model Versioning and Data Migration Programming Guide](../../documentation/Cocoa/Core%20Data%20Model%20Versioning%20and%20Data%20Migration%20Programming%20Guide/Core%20Data%20Model%20Versioning%20and%20Data%20Migration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojz)_.

### Improved Fetch Performance

A number of new options have been added to `NSFetchRequest` to allow finer control of fetch performance.

- Fetching in Batches

  Fetched results can now be broken up into batches to restrict the working set of data in your application.
- Partial Object Faults

  Fetch requests can now indicate the subset of properties to retrieve from the store. These partial object faults behave similarly to standard faults; the complete object is realized as soon as an unfetched property value is accessed or any property on the object is modified.
- Include Pending Changes

  Fetch requests can now be configured to not include pending changes (state in the context not yet saved to the store).
- Aggregates

  Fetch requests now have an additional result type, [NSDictionaryResultType](https://developer.apple.com/documentation/coredata/nsfetchrequestresulttype/1506237-dictionaryresulttype), that can be used in conjunction with a new class, [NSExpressionDescription](https://developer.apple.com/documentation/coredata/nsexpressiondescription), to specify queries that return aggregate values on SQLite stores.

To learn more, see _[NSFetchRequest Class Reference](https://developer.apple.com/documentation/coredata/nsfetchrequest)_.

### Expanded Predicate Support

Predicates now support:

- Key-value coding aggregate functions:

  `@min`, `@max`, `@sum`, `@count`
- Arithmetic functions:

  `+`, `-`, `*`, `/`, `%`

  `uppercase:` , `lowercase:`
- Additional options to comparison predicates using the string or <, <=, =, >=, >, != operator types:

  `[n]ormalized`

  `[l]locale sensitive`

To learn more, see NSExpression.h.

### Spotlight Integration in OS X

Support for integration with Spotlight has been expanded for non-Document based applications in OS X.

Core Data helps you to manage a graph of objects in your program and to save the graph to a persistent store file. Spotlight is a fast desktop search technology that allows users to organize and search for files based on metadata. To integrate a Core Data-based program with Spotlight, you have to provide the Spotlight indexer with information about the data in your persistent store. Document-based Core Data applications should continue to use the mechanisms introduced in Mac OS 10.5, mainly, associating spotlight indexing information with the store file.

For non-Document based applications, you now have the option of mirroring Core Data records into external files, to be indexed independently by Spotlight. You still need to write a Spotlight importer, but you'll now be indexing the individual record files. An expanded Xcode Application Template (non-Document based Core Data Application) gets you started.

To lean more, consult the new _[Core Data Spotlight Integration Programming Guide](../../documentation/Cocoa/Core%20Data%20Spotlight%20Integration%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrv)_.

### Other New API

The following classes also provide new API—see the API reference documentation for more details.

- `NSManagedObjectContext`

  [existingObjectWithID:error:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506686-existingobject)
- `NSManagedObject`

  [contextShouldIgnoreUnmodeledPropertyChanges](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506727-contextshouldignoreunmodeledprop)

  [awakeFromSnapshotEvents:](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506861-awakefromsnapshotevents)

  [prepareForDeletion](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506674-preparefordeletion)
- `NSFetchRequest`

  [returnsDistinctResults](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506344-returnsdistinctresults)
- `NSPersistentStoreCoordinator`

  [NSSQLiteManualVacuumOption](https://developer.apple.com/documentation/coredata/nssqlitemanualvacuumoption)
