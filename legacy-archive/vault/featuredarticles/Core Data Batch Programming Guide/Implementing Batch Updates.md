---
title: Core Data Batch Programming Guide
apple_id: TP40016086
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/featuredarticles/CoreData_Batch_Guide/BatchUpdates/BatchUpdates.html
archived_at: '2026-07-18T02:28:02.032927Z'
---
> 导航：[总目录](../../README.md) · [featuredarticles](../../_indexes/featuredarticles.md) · [Core Data Batch Programming Guide](About%20Making%20Batch%20Changes.md)


[Next](Implementing%20Batch%20Deletes.md)[Previous](About%20Making%20Batch%20Changes.md)

# Implementing Batch Updates

Follow the implementation guidelines in this chapter to avoid common pitfalls and produce maintainable code. You will learn how to:

- Set up a batch update
- Execute a batch update
- Update your application after execution

Batch updates run faster than processing the Core Data entities yourself in code because they operate in the persistent store itself, at the SQL level. As part of this difference, the changes enacted on the persistent store are not reflected in the objects that are currently in memory.

After a batch update has been executed, refresh any objects that are in memory that may be affected by the changes made in the persistent store.

When you use batch updates any validation rules that are a part of the data model are not enforced when the batch update is executed. Therefore, ensure that any changes caused by the batch update will continue to pass the validation rules.

The goal of a batch update is to change one or more properties on a specific entity that is stored in a persistent store in Core Data. A batch update cannot be used to alter relationships, delete entities, or create new entities. To start a batch update, you create an `NSBatchUpdateRequest` object which has a number of similarities to an [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest).

```
let request = NSBatchUpdateRequest(entityName: "Employee")
let predicate = NSPredicate(format: "salary > %@", 10000.00)
request.predicate = predicate
```

Creating an `NSBatchUpdateRequest` is nearly identical to creating an `NSFetchRequest` because the initial actions are the same: declare what entity is being accessed, filter down to the subset of entities that need to be accessed.

Once you have declared what entities you wish to update, you need to specify what changes need to be made:

```
request.propertiesToUpdate = ["terminationDate" : NSDate()]
```

The `propertiesToUpdate` dictionary can have one or more key/value pairs so that multiple changes can be performed during one execution. These changes cannot be calculated or dynamic in any way; that is, they cannot contain any logic beyond the filtering that is available in the predicate.

After the `NSBatchUpdateRequest` is constructed, it is executed against an [NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext):

```
do {
    let result = try moc.executeRequest(request)
} catch {
    fatalError("Failed to execute request: \(error)")
}
```

The call to `executeRequest()` can throw an error and therefore requires the `try` keyword. If the call fails, the error can be reported. When the `executeRequest` completes successfully, a response is received. That response can take one of several forms. The form of the response is determined by setting the `resultType` property on the `NSBatchUpdateRequest`. The default value is `NSStatusOnlyResultType`, which returns nothing. The other two options are:

- `updatedObjectIDsResultType`, which returns an array of [NSManagedObjectID](https://developer.apple.com/documentation/coredata/nsmanagedobjectid) instances indicating which entities were updated during the execution
- `updatedObjectsCountResultType`, which returns a count of the entities that were updated during the execution

The `resultType` needs to be set prior to the execution of the `NSBatchUpdateRequest`. Regardless of which `resultType` that is set, the execution of the `NSBatchUpdateRequest` returns an `NSPersistentStoreResult` instance. If the `resultType` is set to either `NSUpdatedObjectIDsResultType` or `NSUpdatedObjectsCountResultType`, the value of the result property inside of the `NSPersistentStoreResult` instance is set.

If the entities that are being updated are not loaded into memory, then there is no need to update your application with the changes. However, if you are making changes to entities in the persistence layer and you may have those entities in memory at the same time, it is important that you notify the application that the objects in memory are stale and need to be refreshed.

To do this, you first need to make sure the `resultType` of the `NSBatchUpdateRequest` is set to `NSBatchUpdateRequestResultType.updatedObjectIDsResultType` before the request is executed. When the request has completed successfully, the resulting `NSPersistentStoreResult` instance that is returned has an array of [NSManagedObjectID](https://developer.apple.com/documentation/coredata/nsmanagedobjectid) instances referenced in the `result` property. That array of [NSManagedObjectID](https://developer.apple.com/documentation/coredata/nsmanagedobjectid) instances can then be used to update one or more [NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext) instances.

```
do {
    let result = try managedObjectContext.execute(request) as? NSBatchUpdateResult
    let objectIDArray = result?.result as? [NSManagedObjectID]
    let changes = [NSUpdatedObjectsKey : objectIDArray]
    NSManagedObjectContext.mergeChangesFromRemoteContextSave(changes, [moc])
} catch {
    fatalError("Failed to perform batch update: \(error)")
}
```

By calling `mergeChangesFromRemoteContextSave`, all of the [NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext) instances that are referenced are notified that the list of entities referenced with the [NSManagedObjectID](https://developer.apple.com/documentation/coredata/nsmanagedobjectid) array have changed and that the objects in memory are stale. This causes the referenced [NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext) instances to refresh any objects they have loaded that match the [NSManagedObjectID](https://developer.apple.com/documentation/coredata/nsmanagedobjectid) instances in the array.

[Next](Implementing%20Batch%20Deletes.md)[Previous](About%20Making%20Batch%20Changes.md)

