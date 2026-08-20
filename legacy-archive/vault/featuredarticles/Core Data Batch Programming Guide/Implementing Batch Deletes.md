---
title: Core Data Batch Programming Guide
apple_id: TP40016086
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/featuredarticles/CoreData_Batch_Guide/BatchDeletes/BatchDeletes.html
archived_at: '2026-07-18T02:28:01.986734Z'
---
> 导航：[总目录](../../README.md) · [featuredarticles](../../_indexes/featuredarticles.md) · [Core Data Batch Programming Guide](About%20Making%20Batch%20Changes.md)


[Next](Document%20Revision%20History.md)[Previous](Implementing%20Batch%20Updates.md)

# Implementing Batch Deletes

Follow the implementation guidelines in this chapter to avoid common pitfalls and produce maintainable code. You will learn how to:

- Set up a batch delete
- Executie a batch delete
- Update your application after execution

Batch deletes run faster than deleting the Core Data entities yourself in code because they operate in the persistent store itself, at the SQL level. As part of this difference, the changes enacted on the persistent store are not reflected in the objects that are currently in memory.

After a batch delete has been executed, remove any objects in memory that have been deleted from the persistent store.

When you execute a batch delete, any validation rules that are part of the data model are not enforced. Therefore, ensure that any changes caused by the batch delete will continue to pass the validation rules. This naturally impacts validation rules on relationships.

The goal of a batch delete is to delete one or more specific entities that are stored in a SQLite persistent store. To start a batch update, you create an `NSBatchDeleteRequest` that accepts an [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest) as part of its initialization.

```
let fetch = NSFetchRequest<NSFetchRequestResult>(entityName: "Employee")
fetch.predicate = NSPredicate(format: "terminationDate < %@", NSDate())
let request = NSBatchDeleteRequest(fetchRequest: fetch)
```

When an `NSBatchDeleteRequest` is created it accepts an [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest) that describes which entities are to be deleted from the persistent store.

After the `NSBatchDeleteRequest` is constructed, it is executed against an [NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext):

```
do {
    let result = try moc.executeRequest(request)
} catch {
    fatalError("Failed to execute request: \(error)")
}
```

The call to `executeRequest()` can throw an error and therefore requires the `try` keyword. If the call fails, the error can be reported. When the `executeRequest` completes successfully, a response is received. That response can take one of two forms. The form of the response is deteremined by setting the `resultType` property on the `NSBatchDeleteRequest`. The default value is `NSStatusOnlyResultType`, which returns nothing.

The other option is `NSBatchDeleteObjectIDsResultType`, which returns an array of [NSManagedObjectID](https://developer.apple.com/documentation/coredata/nsmanagedobjectid) instances indicating which entities were deleted during the execution.

The `resultType` needs to be set prior to the execution of the `NSBatchDeleteRequest`. Regardless of the `resultType` that is set, the execution of the `NSBatchDeleteRequest` returns an `NSPersistentStoreResult` instance. If the `resultType` is set to `NSBatchDeleteObjectIDsResultType`, the value of the result property inside of the `NSPersistentStoreResult` instance is set.

If the entities that are being deleted are not loaded into memory, there is no need to update your application after the NSBatchDeleteRequest has been executed. However, if you are deleting objects in the persistence layer and those entities are also in memory, it is important that you notify the application that the objects in memory are stale and need to be refreshed.

To do this, first make sure the `resultType` of the `NSBatchDeleteRequest` is set to `NSBatchDeleteRequestResultType.resultTypeObjectIDs` before the request is executed. When the request has completed successfully, the resulting `NSPersistentStoreResult` instance that is returned will have an array of [NSManagedObjectID](https://developer.apple.com/documentation/coredata/nsmanagedobjectid) instances referenced in the result property. That array of `NSManagedObjectID` instances can then be used to update one or more `NSManagedObjectContext` instances.

```
do {
    let result = try moc.execute(request) as? NSBatchDeleteResult
    let objectIDArray = result?.result as? [NSManagedObjectID]
    let changes = [NSDeletedObjectsKey : objectIDArray]
    NSManagedObjectContext.mergeChangesFromRemoteContextSave(changes, [moc])
} catch {
    fatalError("Failed to perform batch update: \(error)")
}
```

By calling `mergeChangesFromRemoteContextSave`, all of the `NSManagedObjectContext` instances that are referenced will be notified that the list of entities referenced with the `NSManagedObjectID` array have been deleted and that the objects in memory are stale. This causes the referenced `NSManagedObjectContext` instances to remove any objects in memory that are loaded which match the `NSManagedObjectID` instances in the array.

[Next](Document%20Revision%20History.md)[Previous](Implementing%20Batch%20Updates.md)

