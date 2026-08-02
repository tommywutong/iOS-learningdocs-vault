---
title: Incremental Store Programming Guide
apple_id: TP40010706
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreData
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/IncrementalStorePG/BestPractices/BestPractices.html
archived_at: '2026-07-15T07:24:00.063113Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Incremental Store Programming Guide](About%20Incremental%20Stores.md)


[Next](Troubleshooting.md)[Previous](Implementation%20Strategy.md)

# Best Practices

Incremental stores give you the speed and memory efficiency you need to work with large, complex data stores. You can use the advanced techniques described in this chapter to improve and fine-tune the performance and memory footprint of your app. The strategies below target and optimize for specific charactertistics of your storage format, so some of these tasks may not apply to your app. The tasks in this chapter describe the best practices to use when implementing efficient, failure-tolerant incremental stores.

Your implementation should balance any special performance characteristics of your store with memory usage and network bandwidth where applicable.

__If your backing store efficiently returns unique identifiers and object values in a single request__, prefetch and cache values related to fetch requests executed on your store.

__If a single, large request is faster than multiple, smaller requests__, batch-request objects rather than create individual requests every time a fault is fired on an object. For example, the time it takes to make a request to a web service is typically longer than the time it takes for the web service to generate a response.

__If requests to your backing store are slow or if the availability of your store changes__, write the cache to disk. In this case, when your store receives an `executeRequest:withContext:error:` message, your implementation immediately returns results from the local disk cache and simultaneously triggers a fetch to your backing data store. When that fetch returns, update your local disk cache and post a notification to your user interface so that it knows to refetch.

A row cache allows you to materialize faults immediately from memory rather than refetch values from the backing data store based on the managed object context’s `stalenessInterval` or your own predetermined staleness value. This is beneficial when executing a request against your store is expensive.

With a row cache, you retrieve the existing node from your cache and use the `NSIncrementalStoreNode` class’s [updateWithValues:version:](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506721-updatewithvalues) method to update the node’s values. Without a row cache, you create and return a new [NSIncrementalStoreNode](https://developer.apple.com/documentation/coredata/nsincrementalstorenode) object whenever a fault is fired and your [newValuesForObjectWithID:withContext:error:](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506729-newvaluesforobjectwithid) method is invoked. Creating an incremental store node has considerable overhead, so caching your incremental store nodes is preferrable.

Design a class that caches incremental store nodes with retrieval timestamps and “reference counts”. The reference count is simply an integer you increment each time a managed object context begins using an object and decrement when a managed object context finishes using an object. When a fault is fired and the node is out of date compared to the context’s staleness interval, refetch the values and update the node rather than just returning it from the row cache. Likewise, if the reference count reaches zero, purge the node from your cache.

`NSIncrementalStore` provides two methods, `managedObjectContextDidRegisterObjectsWithIDs:` and `managedObjectContextDidUnregisterObjectsWithIDs:`, that you use to track which managed objects are currently in use by your Core Data stack. As a result, your store can flush data as it becomes unused. Your store need not keep strong references to any data backing objects that are in use—you must balance the I/O cost of re-retrieving data with the cost of maintaining it in memory. The default implementations of these methods do nothing; they can be overridden by store implementers so that their stores can maintain resources that are in use and dispose of resources that are no longer needed.

When you receive a request with a result type of `NSManagedObjectResultType` or `NSManagedObjectIDResultType`, fetch both the unique identifiers and the object attributes from your backing store and insert the values into your row cache. Do not prepopulate managed objects returned as part of an `NSManagedObjectResultType``resultType` collection. When Core Data faults in attributes on your managed objects, you use `newValuesForObjectWithID:withContext:error:` to return unexpired prefetched values from your row cache rather than retrieving records from the backing store.

You use a disk cache to return the results of a fetch immediately from a local store rather than block while your store executes a long-running network or disk operation.

Back your incremental store with an `NSSQLiteStoreType` type persistent store on an entirely separate Core Data stack. An added benefit is that the persistent store can parse both scope modifiers and sort descriptors in a fetch request for you. You can ignore sort descriptors and scope modifiers when you fetch from the backing data store, and then take advantage of the SQLite persistent store’s extensive built-in fetch request parsing mechanism.

When your incremental store recieves fetch requests, forward the requests to the backing persistent store and return the results.

Optimistic locking is a mechanism in Core Data that gives the persistent store coordinator the ability to detect when in-memory conflicts occur and also handle when your incremental store detects that another client has made changes the backing store.

Core Data manages multiple in-memory snapshots of your data, holding each snapshot inside a managed object context. When you insert, update, or delete managed objects in one context, that change is not reflected in other contexts. This allows you to do work on multiple contexts in different threads simultaneously without worrying about merge conflicts. Merging is deferred until the contexts are saved to the store. At that point, the merge policy you specify is applied by the persistent store coordinator.

To facilitate the persistent store coordinator’s in-memory locking mechanism, your store should store a version number for each record in the backing store and increment it every time that record is saved.

A conflict in the backing data store happens when records in the backing data store are changed by another persistent store coordinator or another client. Detecting conflicts in the backing store is the responsibility of your custom incremental store.

Optimistic locking failures are encountered when processing a save request inside `executeRequest:withContext:error:`. To report an optimistic locking failure in the backing data store, construct `NSMergeConflict` objects for each conflicting object in the save request, set the error parameter, and return `nil` from the method. You should not attempt to partially fulfill the save request. See the _[NSMergeConflict Class Reference](https://developer.apple.com/documentation/coredata/nsmergeconflict)_ for more information.

For example, a client could fetch data from a web service and modify it. In the meantime, another client could fetch data from the web service, modify the records, and save. When the first client goes to save, your incremental store compares the optimistic locking version number of the incremental store node and the version number in the backing store and reports the conflict to the persistent store coordinator. The coordinator detects a merge conflict and applies your merge policy.

When you create an incremental store that interfaces with a web service, you must take into account several unique factors: latency, network availability, and conflict management. Use your app requirements, use cases, and the Instruments app to choose what matters most and then profile until your store meets your needs.

When fetch and save requests are executed by managed object contexts on different threads, the persistent store coordinator collects the requests into a serial queue and dispatches each request to a single instance of your incremental store in the order in which they were received. Because the persistent store coordinator requires that results be returned immediately (rather than by a deferred callback mechanism), your store must synchronously return data from the backing data store. If your backing data store supports concurrent read and/or write operations, for optimal performance consider using multiple persistent store coordinators when designing your Core Data stack.

A predicate is a scope modifier that filters the results of a fetch request. Represented by the abstract `NSPredicate` class, a predicate is made up of a left-hand value, a right-hand value, and a comparison operator — or it is made up of two or more nested predicates and a join operator. For example, `age == 40` is a simple comparison predicate, and `(age == 40) AND (name == "Jack")` is a simple compound predicate.

Whereas most predicates are straightforward, compound predicates may be nested to create extremely complicated, challenging-to-parse filters. Unless _absolutely_ necessary, avoid attempting to handle every predicate. Instead define a subset of predicates that your incremental store will support, based on the requirements of your app and the backing data store.

For more information about predicates, see _[Predicate Programming Guide](../../Cocoa/Predicate%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoobz)_ as well as _[NSPredicate Class Reference](https://developer.apple.com/documentation/foundation/nspredicate)_, _[NSCompoundPredicate Class Reference](https://developer.apple.com/documentation/foundation/nscompoundpredicate)_, _[NSComparisonPredicate Class Reference](https://developer.apple.com/documentation/foundation/nscomparisonpredicate)_, and _[NSExpression Class Reference](https://developer.apple.com/documentation/foundation/nsexpression)_.

[Next](Troubleshooting.md)[Previous](Implementation%20Strategy.md)

