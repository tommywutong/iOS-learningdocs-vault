---
title: Incremental Store Programming Guide
apple_id: TP40010706
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreData
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/IncrementalStorePG/Troubleshooting/Troubleshooting.html
archived_at: '2026-07-15T07:24:01.218653Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Incremental Store Programming Guide](About%20Incremental%20Stores.md)


[Next](Document%20Revision%20History.md)[Previous](Best%20Practices.md)

# Troubleshooting

If you have trouble getting your app to work correctly, try the problem-solving approaches described in this chapter.

If you log a managed object ID or the object ID’s `URIRepresentation` object and you get an unrecognized selector exception or it prints `<(null)>`, check that your reference object is of type `NSString` or `NSNumber`. All other types are unsupported.

If an `NSObjectInaccessibleException` exception is raised when accessing the properties on a managed object it could be for one of the following reasons:

- The managed object you are holding a reference to has been removed from the store and is no longer valid.

  This problem is most likely not in your incremental store. Make sure your Core Data stack is set up properly and that you aren’t holding references to managed objects after they have been deleted (especially when working with multiple contexts).
- `newValuesForObjectWithID:withContext:error` or `newValueForRelationship:forObjectWithID:withContext:error` are returning `nil`.

  Place a breakpoint inside of the method returning `nil`. Be sure to set the `error` parameter to an `NSError` object with useful information for future debugging. If the availability of your backing data store is volatile (for example, when interacting with a web service), communicate these availability changes to your user and provide a fallback mechanism such as a cache.

If an empty to-one relationship cannot be faulted in, return `[NSNull null]` rather than `nil` from `newValuesForObjectWithID:withContext:error:` or `newValueForRelationship:forObjectWithID:withContext:error:` to inform the persistent store coordinator that the relationship is empty. Otherwise, the persistent store coordinator assumes that an internal error occurred.

If an empty to-many relationship cannot be faulted in, you are returning `nil` in one of the two relationship fulfillment methods. Realization of to-many relationships can be deferred until `newValueForRelationship:forObjectWithID:withContext:error:`. However, when this method is called, the relationship must be fulfilled. If the relationship does not contain any objects, return an empty array rather than `nil`. Otherwise, the persistent store coordinator assumes that an internal error occurred.

If merge conflicts are not being resolved or the merge policy is failing, check that the following parts of your implementation are correct:

- The `NSError` object is properly constructed.
- The `NSMergeConflict` objects are properly constructed.
- The version numbers you provide indicate that an optimistic locking failure has occurred.

If merge conflicts are erroneously detected, ensure that you are incrementing version numbers every time records are saved.

[Next](Document%20Revision%20History.md)[Previous](Best%20Practices.md)

