---
title: Core Data Release Notes for OS X v10.7 and iOS 5.0
apple_id: TP40010637
resource_type: Release Note
platform: iOS|macOS
topic: Data Management
technology: CoreData
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/releasenotes/DataManagement/RN-CoreData/index.html
archived_at: '2026-07-18T02:50:23.624849Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Core Data Release Notes for OS X v10.7 and iOS 5.0

This document describes the main new areas of functionality in Core Data in OS X v10.7 and iOS 5.0.

#### Contents:

- [Concurrency Support for Managed Object Contexts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmmzxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Nested Managed Object Contexts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmmzxfvbuqmjnknltc)
- [Incremental Store](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmmzxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Managed Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmmzxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [Fetch Requests](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmmzxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6na)
- [Managed Documents](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmmzxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ni)

### Concurrency Support for Managed Object Contexts

[NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext) now provides structured support for concurrent operations. When you create a managed object context using [initWithConcurrencyType:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506709-init), you have three options for its thread (queue) association

- Confinement ([NSConfinementConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/confinementconcurrencytype)).

  This is the default. You promise that context will not be used by any thread other than the one on which you created it. (It’s exactly the same threading requirement that you’ve used in previous releases.) This is the default for backwards compatibility. In general, to make the behavior explicit you’re encouraged to use one of the other types instead.

  You cannot use this concurrency type in conjunction with the new nested contexts feature (see [Nested Managed Object Contexts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmmzxfvbuqmjnknltc)).
- Private queue ([NSPrivateQueueConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/nsprivatequeueconcurrencytype)).

  The context creates and manages a private queue.
- Main queue ([NSMainQueueConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/nsmainqueueconcurrencytype)).

  The context is associated with the main queue, and as such is tied into the application’s event loop, but it is otherwise similar to a private queue-based context. You use this queue type for contexts linked to controllers and UI objects that are required to be used only on the main thread.

You can use contexts using the confinement pattern just as you have prior to OS X v10.7 and iOS 5. You send the contexts messages directly; it’s up to you to ensure that you send the messages from the right queue.

You use contexts using the queue-based concurrency types in conjunction with two new methods: [performBlock:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506578-performblock) and [performBlockAndWait:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506364-performblockandwait). You group “standard” messages to send to the context (including initialization such as setting the persistent store coordinator and so on) within a block to pass to one of these methods. The one exception is: if your code is executing on the main thread, you can invoke methods on the main queue style contexts directly instead of using the block based API.

`performBlock:` and `performBlockAndWait:` ensure the block operations are executed on the queue specified for the context. The `performBlock:` method returns immediately and the context executes the block methods on its own thread. With the `performBlockAndWait:` method, the context still executes the block methods on its own thread, but the method doesn’t return until the block is executed.

It’s important to appreciate that blocks are executed as a distinct body of work. As soon as your block ends, anyone else can enqueue another block, undo changes, reset the context, and so on. Thus blocks may be quite large, and typically end by invoking [save:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506866-save).

```
__block NSError *error;
__block BOOL savedOK = NO;
[myMOC performBlockAndWait:^{
    // Do lots of things with the context.
    savedOK = [myMOC save:&error];
}];
```

You can also perform other operations, such as:

```
NSFetchRequest *fr = [NSFetchRequest fetchRequestWithEntityName:@"Entity"];
__block NSUInteger rCount = 0;

[context performBlockAndWait:^() {
    NSError *error;
    rCount = [context countForFetchRequest:fr error:&error];
    if (rCount == NSNotFound) {
        // Handle the error.
    }
}];

NSLog(@"Retrieved %d items", (int)rCount);
```


### Nested Managed Object Contexts

Rather than specifying a persistent store coordinator for a managed object context, you can now specify a parent managed object context using `setParentContext:`. This means that fetch and save operations are mediated by the parent context instead of a coordinator. This pattern has a number of usage scenarios, including:

- Performing background operations on a second thread or queue.
- Managing discardable edits, such as in an inspector window or view.

As the first scenario implies, a parent context can service requests from children on different threads. You cannot, therefore, use parent contexts created with the thread confinement type (see [Concurrency Support for Managed Object Contexts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmmzxfvbuqmjnknltc)).

When you save changes in a context, the changes are only committed “one store up.” If you save a child context, changes are pushed to its parent. These changes are not saved to the _persistent store_ until the _root_ context is saved. (A root managed object context is one whose parent is `nil`.) In addition, a parent does not pull changes from children before it saves. You _must_ save a child contexts if you want ultimately to commit the changes.

Nested contexts make it more important than ever that you adopt the “pass the baton” approach of accessing a context (by passing a context from one view controller to the next) rather than retrieving it directly from the application delegate.

### Incremental Store

Core Data provides two new classes, [NSIncrementalStore](https://developer.apple.com/documentation/coredata/nsincrementalstore) and [NSIncrementalStoreNode](https://developer.apple.com/documentation/coredata/nsincrementalstorenode), that you can use to implement support for non-atomic persistent stores. The store does not have to be a relational database—for example, you could use a web service as the back end.

Core Data supports faulting and other aspects of object graph management and other aspects of object graph management in the domain of the NSManagedObjectContext. The interface from the persistent store coordinator to a custom incremental store is through [NSPersistentStoreRequest](https://developer.apple.com/documentation/coredata/nspersistentstorerequest) objects. It does not provide SQL generation, predicate interpretation, or any other amenities of the public framework vended stores.

Core Data sends instructions to retrieve from the store and save data to the store using persistent store requests. [NSPersistentStoreRequest](https://developer.apple.com/documentation/coredata/nspersistentstorerequest) is a new class that now serves as the superclass of [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest) and another new class, [NSSaveChangesRequest](https://developer.apple.com/documentation/coredata/nssavechangesrequest). [NSPersistentStoreRequest](https://developer.apple.com/documentation/coredata/nspersistentstorerequest) provides attributes that indicate which stores are affected by the request, and whether it’s a save or a fetch request. A save changes request specifies which managed objects are inserted, deleted, and updated, and those that were flagged for optimistic locking.

When you implement a store, you don't have to support all forms of fetch request if your application doesn't need to. Indeed, `NSFetchRequest` is so powerful, you are encouraged to consider starting by only supporting pre-canned requests in your incremental store specific to your application's needs.

### Managed Objects

Managed objects support two significant new features: ordered relationships, and external storage for attribute values.

- Ordered relationships are represented by instances of [NSOrderedSet](https://developer.apple.com/documentation/foundation/nsorderedset) rather than `NSSet`. `NSOrderedSet` does not inherit from `NSSet`. You use `mutableOrderedSetValueForKey:` instead of [mutableSetValueForKey:](https://developer.apple.com/documentation/coredata/nsmanagedobject/1807259-mutablesetvalueforkey) to retrieve a mutable proxy for the relationship.

  Although ordered relationships are easy to specify and use, they are significantly less efficient to use than unordered relationships. You should use them only if a relationship has intrinsic ordering that is critical to its own representation—such as the steps in a recipe. You thus need to differentiate actual values from presentation of the values. If the user can change the order of presentation of elements in a relationship by, for example, setting a sort ordering in a table view, then the relationship shouldn’t be ordered.
- Small data values like image thumbnails may be efficiently stored in a database, but large photos or other media are best handled directly by the file system. You can now specify that the value of a managed object attribute may be stored as an external record—see [setAllowsExternalBinaryDataStorage:](https://developer.apple.com/documentation/coredata/nsattributedescription/1498295-allowsexternalbinarydatastorage). When enabled, Core Data heuristically decides on a per-value basis if it should save the data directly in the database or store a URI to a separate file which it manages for you. You cannot query based on the contents of a binary data property if you use this option.

### Fetch Requests

You can specify the name of the entity you want to fetch as a string by initializing a fetch request using [initWithEntityName:](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506802-init). This is typically easier than using [setEntity:](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506979-entity) and having to retrieve the appropriate [NSEntityDescription](https://developer.apple.com/documentation/coredata/nsentitydescription) object from the model. It does mean, however, that the request’s [entity](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506979-entity) remains “in limbo” until you actually execute the request, at which point the entity description is retrieved via the context’s persistent store coordinator and set as the value. If you invoke [entity](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506979-entity) before using the request, Core Data throws an exception.

You can use [setShouldRefreshRefetchedObjects:](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506440-shouldrefreshrefetchedobjects) to configure a fetch to get the most recent values for the managed objects it retrieves. Previously, you had to either [reset](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506807-reset) the context or explicitly refresh individual managed objects using [refreshObject:mergeChanges:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506224-refreshobject). Otherwise, if you fetched the same object over and over again, it would contain the same property values even if the corresponding record had changed in the persistent store.

If you’re using the SQLite store and you configure a fetch request to return values as dictionaries ([NSDictionaryResultType](https://developer.apple.com/documentation/coredata/nsfetchrequestresulttype/1506237-dictionaryresulttype)), you can group the results using [setPropertiesToGroupBy:](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506191-propertiestogroupby). This lets you perform aggregate operations—for example, you can group employees by department. If you specify properties to group by, you can also specify a “having predicate” ([setHavingPredicate:](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506429-havingpredicate)) to filter the groups being returned.

### Managed Documents

Core Data provides integration with the iOS document architecture and so with cloud storage. [UIManagedDocument](https://developer.apple.com/documentation/uikit/uimanageddocument) is a concrete subclass of [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) that uses a Core Data persistent store for document data storage. When you initialize a managed document, you specify the URL for the document location. The document object then creates a Core Data stack to use to access the document’s persistent store using managed object model from the application’s main bundle.

`UIManagedDocument` performs all the basic set-up you need for Core Data. You can, though, supply configuration options for the creation of the coordinator and for the model. You can perform additional customization by creating a subclass of `UIManagedDocument`.
