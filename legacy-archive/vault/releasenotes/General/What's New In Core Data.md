---
title: What's New In Core Data
apple_id: TP40017342
resource_type: Release Note
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/WhatNewCoreData2016/ReleaseNotes.html
archived_at: '2026-07-18T02:54:45.098787Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# What's New in Core Data in macOS 10.12, iOS 10.0, tvOS 10.0, and watchOS 3.0

This document describes the new areas of functionality in Core Data in macOS 10.12, iOS 10.0, tvOS 10.0, and watchOS 3.0. Please note that many Swift APIs are renamed in accordance with Swift 3 API design guidelines. Please refer to Swift Evolution document SE-0023, "API Design Guidelines."

The [NSPersistentStoreCoordinator](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator) now maintains a small connection pool that allows concurrent database operations for [NSSQLiteStoreType](https://developer.apple.com/documentation/coredata/nssqlitestoretype) persistent stores. An [NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext) (that is not nested) can now fetch and fault concurrently with other peer `NSManagedObjectContext` instances. For persistent stores using WAL `journal_mode` (the default in Core Data), the `NSPersistentStoreCoordinator` also supports 1 writer concurrently with multiple readers. For example, a UI context can fetch data concurrently with a single background context importing changes. Connection pooling uses less memory and generally out performs multiple separate `NSPersistentStoreCoordinator` instances to the same file.

This behavior is enabled for all existing Core Data clients. The default number of connections varies by platform but is greater than 1. You can adjust the behavior with the `NSPersistentStoreConnectionPoolMaxSizeKey` in your options dictionary when adding the store to the coordinator. `NSPersistentStoreCoordinator` briefly dispatches requests through its own queue, and custom code in blocks passed to `NSPersistentStoreCoordinator.perform` or `NSPersistentStoreCoordinator.performAndWait` will block the `NSPersistentStoreCoordinator` from routing future requests until they complete. Nested `NSManagedObjectContext` instances still serialize requests against their parent context as before.

`NSPersistentContainer` is a new class that simplifies creating a new Core Data stack. It maintains references to your `NSManagedObjectModel`, `NSPersistentStoreCoordinator`, and other resources. `NSPersistentContainer` uses a new class `NSPersistentStoreDescription` to describe the configuration information to pass to `NSPersistentStoreCoordinator` when adding a persistent store. `NSPersistentStoreDescription` defaults to an `NSSQLiteStoreType` with automatic light weight migration enabled. The Xcode new project assistant for creating new iOS projects (but not macOS) that use Core Data now uses `NSPersistentContainer` in the `AppDelegate`. An example:

```
let container = NSPersistentContainer(name: "myAppName")
container.loadPersistentStores(completionHandler: { (storeDescription, error) in
    if let error = error {
        fatalError("Unresolved error \(error), \(error.userInfo)")
    }
    container.viewContext.perform({
        // actions upon the NSMainQueueConcurrencyType NSManagedObjectContext for this container
    })
})
```

This will find a model resource in the main bundle named after "myAppName", load it, create a new `NSPersistentStoreCoordinator`, and add a persistent store with the same name in the `defaultDirectoryURL`. The configuration details can be changed on the `NSPersistentContainer` before calling `loadPersistentStores`.

NSPersistentContainer also has a few amenities for working with `NSManagedObjectContext` instances, including a single main queue context suitable for use with the view layer and factory methods for background contexts. You can also just give a block to the `NSPersistentContainer` which will asynchronously complete the task.

```
let container = NSPersistentContainer.persistentContainerWithName("myApp")
container.performBackgroundTask() { (moc) in
    // use moc to do asynchronous work
}
```


Core Data now supports pinning an `NSManagedObjectContext` to a specific query generation (database transaction) for arbitrarily many operations. A new class `NSQueryGenerationToken` represents an object that can be used to specify a pinning behavior or a specific version from another context. You can ask a context for its current `queryGenerationToken` or set one with `setQueryGenerationFromToken(:)` A `nil` token represents unpinned, which is the default behavior. Unpinned is the same `NSManagedObjectContext` behavior as previous releases. `currentQueryGenerationToken` is a token that can be passed to a context to tell it to lazily retrieve the most recent version on its next read operation (fetching or faulting) and then pin itself to that point in time. Calling `save()`, `reset()`, [mergeChangesFromContextDidSaveNotification:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506606-mergechanges), or `mergeChangesFromRemoteContextSave(:intoContexts:)` on any pinned context will automatically advance it to the most recent version for the operation and then reset its query generation to `currentQueryGenerationToken`.

The persistent store must be an `NSSQLiteStoreType` in WAL `journal_mode` (the default). Query generations expire if no contexts refer to them or the process terminates.

As an example:

```
try container.viewContext.setQueryGenerationFromToken(NSQueryGenerationToken.currentQueryGenerationToken)
let request = NSFetchRequest(entityName:"Animal")
request.fetchBatchSize = 10
let results = try container.viewContext.executeFetchRequest(request)
let first = results.first
var aname = first.name // pull in the first batch's row data

let moc = container.newBackgroundContext

moc.performBlockAndWait() {
    let update = NSBatchUpdateRequest(entityName:"Animal")
    update.resultsType = .UpdatedObjectsCountResultType
    update.propertiesToUpdate = ["name" : NSExpression(forConstantValue:"Cat")]
    do {
        let result = try moc.executeRequest(update)
    } catch {
        print("Error executing update: \(error)")
    }
}

var next = results[100]
aname = next.name // new reads from the batched fetch result still pull the previous verison's data

try container.viewContainer.setQueryGenerationFromToken(NSQueryGenerationToken.currentQueryGenerationToken)

next = results[200]
aname = next.name //now new reads from the batching result pull in the new Cat data
```


If there is a 1:1 mapping between [NSEntityDescription](https://developer.apple.com/documentation/coredata/nsentitydescription) instances and custom [NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject) subclasses defined in your data model, Core Data will provide strongly typed conveniences on `NSManagedObject` subclasses in lieu of the string based `NSEntityDescription` class methods. These include the following new methods on `NSManagedObject`:

```swift
public class func entity() -> NSEntityDescription
public class func fetchRequest() -> NSFetchRequest<NSFetchRequestResult>
public convenience init(context moc: NSManagedObjectContext)
```

The binding between entities and subclasses happens when the [NSManagedObjectModel](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel) is first used to initialize an `NSPersistentStoreCoordinator`. If the mapping between `NSEntityDescription` instances and subclasses is ambiguous, the functionality is disabled. You should avoid creating new copies of the same `NSManagedObjectModel` by reloading it from disk repeatedly.

[NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest) is now a parameterized type based on a new `NSFetchRequestResult` protocol. Several Core Data APIs now refer to the parameterized `NSFetchRequest` in both Objective-C and Swift.

Additionally in Swift, `NSManagedObjectContext` offers parameterized variants of `fetch(:)`, the Swift 3 name for [executeFetchRequest:error:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506672-fetch), and `count(:)`.

```swift
public func fetch<T : NSFetchRequestResult>(_ request: NSFetchRequest<T>) throws -> [T]
public func count<T : NSFetchRequestResult>(for request: NSFetchRequest<T>) throws -> Int
```

Bringing these changes together, in Swift 2 you might have had something like:

```swift
func findAnimals() {
    let request = NSFetchRequest(entityName:”Animal")
        do {
        guard let searchResults = try context.executeFetchRequest(request) as? [Animal] else {
        print("Results were not of the expected structure")
        }
        ... use(searchResults) ...
        } catch {
        print("Error ocurred during execution: \(error)")
    }
}
```

and in Swift 3:

```swift
func findAnimals() {
    let request: NSFetchRequest<Animal> = Animal.fetchRequest
    do {
        let searchResults = try context.fetch(request)
        ... use(searchResults) ...
    } catch {
        print("Error with request: \(error)")
    }
}
```

`NSFetchRequest` also offers a new method `execute()` which can only be called within the scope of an `NSManagedObjectContext` instance's `perform` or `performAndWait` block's lexical scope. `execute()` directs that `NSManagedObjectContext` to execute the fetch request like:

```swift
func findAnimals() {
    context.performAndWait({
        let request : NSFetchRequest<Animal> = Animal.fetchRequest
        do {
            let searchResults = try request.execute()
            ... use(searchResults) ...
        } catch {
            print("Error with request: \(error)")
        }
    })
}
```


The [NSFetchedResultsController](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller) is now available on macOS 10.12. As with `NSFetchRequest`, it has become a parameterized type which it carries through to collections and methods derived from the `NSFetchRequest` that defines it.

Xcode now supports automatic generation of `NSManagedObject` subclasses in the modeling tool. In the entity inspector:

- Manual/None is the default, and previous behavior; in this case you should implement your own subclass or use `NSManagedObject`.
- Category/Extension generates a class extension in a file named like ClassName+CoreDataGeneratedProperties. You need to declare/implement the main class (if in Obj-C, via a header the extension can import named ClassName.h).
- Class Definition generates subclass files named like ClassName+CoreDataClass as well as the files generated for Category/Extension.

The generated files are placed in DerivedData and rebuilt on the first build after the model is saved. They are also indexed by Xcode, so command-clicking on references and fast-opening by filename works.

As of macOS v10.12 and iOS 10.0; Core Data's iCloud integration feature has been deprecated. Apps will continue to work. There are no changes to or removal of the functionality in macOS 10.12 and iOS 10. Historically, deprecated symbols in Cocoa remain functional for a considerable period of time before removal. Only the client side Core Data iCloud API symbols are deprecated. Core Data with iCloud is built on top of the iCloud Drive service. The service pieces are not effected in any way. If and when the deprecated APIs are disabled in some future OS version, applications running on iOS 9 or 10 will continue to work.

- `NSManagedObjectContext` now provides a property `automaticallyMergesChangesFromParent` that causes it to automatically register as an observer of [NSManagedObjectContextDidSaveNotification](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextdidsavenotification) posted by its parent store and call one of the mergeChanges methods upon itself.
- `NSPersistentStoreCoordinator` provides a new `addPersistentStoreWithDescription(:completionHandler:)` method that takes an `NSPersistentStoreDescription` and uses it to call, optionally asynchronously, [addPersistentStoreWithType:configuration:URL:options:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468860-addpersistentstore).

Core Data has changed two behaviors for applications built with a minimum deployment target of macOS 10.12, iOS 10.0, tvOS 10.0, or watchOS 3.0.

- [performBlockAndWait:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506364-performblockandwait) implicitly includes an autorelease pool around each block. Projects using ARC or Swift should be generally unaffected, although remember that both `NSError**` out parameters and exceptions are autoreleased and do not escape block lexical scope happily. Projects using manual retain / release will need to retain autoreleased objects, including the results of [executeFetchRequest:error:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506672-fetch) inside the block and release or autorelease them outside the block's lexical scope. For example:

```
__block id result = nil;
[context performBlockAndWait:^{
    NSError* error = nil;
    result = [context executeFetchRequest:request error:&error];
}];
return result;
```

This code works under ARC but under manual retain release must instead be:

```
__block id result = nil;
[context performBlockAndWait:^{
    NSError* error = nil;
    result = [[context executeFetchRequest:request error:&error] retain];
}];
return [result autorelease];
```

- `NSManagedObjectContext` now defaults to a `nil` [NSUndoManager](https://developer.apple.com/documentation/foundation/undomanager) on macOS. It always defaulted to `nil` on iOS.
- [NSFetchedResultsController](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller) now correctly merges changes from other context for objects it hasn’t seen in its own context
- [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest) now allows predicates to specify an entity restriction allowing fetches against entity hierarchies in which only some sub entities have the relevant property such as:

```
@“self.entity = %@ and subentityProperty = %@“ or even @“relationship.entity = %@ and relationship.onlysomedestinationsubentitiesAttribute = %@“
```

  Only one restricting entity qualifier per clause is allowed.
- Core Data has adopted the new logging infrastructure in 10.12 and iOS 10.0, and switched from using `NSLog` to `os_log` with the logging subsystem "com.apple.coredata". The output of this logging can be viewed in the Console application, or in terminal with the command:

```
log stream —predicate 'subsystem = "com.apple.coredata"'
```

  As part of this transition, Core Data honors user defaults to log to `os_log`, `stderr`, or both with ‘com.apple.CoreData.Logging.oslog’ or ‘com.apple.CoreData.Logging.stderr’. Due to a known issue in Xcode, it may be useful to toggle `stderr` logging on during debugging.
- NSManagedObject dynamic accessor generation has fixed issues to properly generate accessors for ordered to-many relationships. Core Data will generate any of the “Mutable Indexed Accessors” documented in [Key-Value Coding Accessor Methods](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/KeyValueCoding/Articles/AccessorConventions.html#//apple_ref/doc/uid/20002174-BAJEAIEE). Both ordered and unordered to-many relationships support all of the “Mutable Unordered Accessors” except intersection<Key>.

  The potentially generated accessors include a getter named exactly as the property name from the data model, or the following list where \* is the capitalized property name:

  - set\*:
  - primitive\*
  - setPrimitive\*:
  - add\*Object:
  - add\*:
  - remove\*Object:
  - remove\*:
  - removeObjectFrom\*AtIndex:
  - remove\*AtIndexes:
  - remove\*:
  - insertObject: in\*AtIndex:
  - insert\*: AtIndexes:
  - replaceObjectIn\*AtIndex: withObject:
  - replace\*AtIndexes: with\*:
  - validate\*: error:
  - willChange\*
  - didChange\*
  - willAccess\*
  - didAccess\*
- NSManagedObject will now also allow subclasses to override accessors and still invoke the implementation that otherwise would have been dynamically generated. This can be done by invoking a method named identically to the overridden method with ‘managedObjectOriginal_’ prepended. For example:

```objc
- (void)setDepartment:(Department *)value
{
    // invoke the dynamic implementation of setDepartment
    [self managedObjectOriginal_setDepartment:value];

    NSLog(@"invoked %@", NSStringFromSelector(_cmd));
}
```


