---
title: NSBatchDeleteRequest
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchdeleterequest
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchdeleterequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchdeleterequest.json'
content_hash: 'sha256:01f0076eacaed6db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSBatchDeleteRequest

<sub>Class</sub>

A request that deletes objects in the SQLite persistent store without loading them into memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSBatchDeleteRequest
```

## Overview

`NSBatchDeleteRequest` — available only when using a SQLite persistent store — deletes managed objects at the SQL level of the persistent store. This request is quicker and more efficient than using a context to fetch a large number of objects into memory, delete them, and then save those deletions back to the store. You create a request using an instance of [NSFetchRequest](nsfetchrequest.md) that identifies the objects to delete. Alternatively, you can provide an array of identifiers from specific objects of the same entity type; mixing entity types results in an error when you execute the request.

[NSManagedObjectContext](nsmanagedobjectcontext.md) doesn’t automatically merge a request’s deletions because they happen at the SQL level. Subsequently, you must remove any deleted objects from memory after the request finishes. To determine the objects a request deletes, configure it to return the [NSManagedObjectID](nsmanagedobjectid.md) of each deleted object and use those identifiers to update your contexts, as the following example shows:

```swift
// Configure the request to return the IDs of the objects it deletes.
request.resultType = .resultTypeObjectIDs

do {
    // Execute the request.
    let deleteResult = try context.execute(request) as? NSBatchDeleteResult
    
    // Extract the IDs of the deleted managed objectss from the request's result.
    if let objectIDs = deleteResult?.result as? [NSManagedObjectID] {
        
        // Merge the deletions into the app's managed object context.
        NSManagedObjectContext.mergeChanges(
            fromRemoteContextSave: [NSDeletedObjectsKey: objectIDs],
            into: [context]
        )
    }
} catch {
    // Handle any thrown errors.
}
```

Alternatively, you can use persistent history tracking to make your contexts aware of changes that happen at the persistent store level. For more information, see [Consuming relevant store changes](consuming-relevant-store-changes.md).

> [!important] Important
> Ensure that a request’s changes don’t violate the validation rules in your data model beyond basic delete rules, such as reducing a relationship count below the specified minimum. The Deny delete rule isn’t compatible with `NSBatchDeleteRequest`.

## Relationships

- **Inherits From**: [NSPersistentStoreRequest](nspersistentstorerequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Request

- [- initWithFetchRequest:](<nsbatchdeleterequest/init(fetchrequest_).md>) — Creates a request that deletes the results of the specified fetch request.
- [- initWithObjectIDs:](<nsbatchdeleterequest/init(objectids_).md>) — Creates a request that deletes the managed objects with the specified identifiers.

### Accessing the Fetch Request

- [fetchRequest](nsbatchdeleterequest/fetchrequest.md) — The fetch request that identifies the managed objects to delete.

### Configuring the Result Type

- [resultType](nsbatchdeleterequest/resulttype.md) — The type of result the request provides when it executes.
- [NSBatchDeleteRequestResultType](nsbatchdeleterequestresulttype.md) — The types of result a batch delete request can provide when it executes.

## See Also

### Data Deletion

- [NSBatchDeleteResult](nsbatchdeleteresult.md) — An object that describes the result of a batch delete request.
