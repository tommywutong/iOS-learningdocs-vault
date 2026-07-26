---
title: 'mergeChanges(fromRemoteContextSave:into:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectcontext/mergechanges(fromremotecontextsave:into:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/mergechanges(fromremotecontextsave:into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/mergechanges%28fromremotecontextsave%3Ainto%3A%29.json'
content_hash: 'sha256:015541ca2665decd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# mergeChanges(fromRemoteContextSave:into:)

<sub>Type Method</sub>

Handles changes from other processes or from a serialized state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func mergeChanges(fromRemoteContextSave changeNotificationData: [AnyHashable : Any], into contexts: [NSManagedObjectContext])
```

## Discussion

This method more efficiently merges changes into multiple contexts as well as nested contexts. The dictionary keys should be one or more from an [NSManagedObjectContextObjectsDidChange](../../foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextobjectsdidchange.md):  [NSInsertedObjectsKey](../nsinsertedobjectskey.md), [NSUpdatedObjectsKey](../nsupdatedobjectskey.md), [NSDeletedObjectsKey](../nsdeletedobjectskey.md). The values should be an [NSArray](../../foundation/nsarray.md) of either [NSManagedObjectID](../nsmanagedobjectid.md) or [NSURL](../../foundation/nsurl.md) objects conforming to valid results from [- URIRepresentation](<../nsmanagedobjectid/urirepresentation().md>).

## See Also

### Managing concurrency

- [NSManagedObjectContextQueryGenerationKey](../nsmanagedobjectcontextquerygenerationkey.md) — Constant used to reference the query generation token.
- [automaticallyMergesChangesFromParent](automaticallymergeschangesfromparent.md) — A Boolean value that indicates whether the context automatically merges changes saved to its persistent store coordinator or parent context.
- [concurrencyType](concurrencytype-swift.property.md) — The concurrency type for the context.
- [mergePolicy](mergepolicy.md) — The merge policy of the context.
- [queryGenerationToken](querygenerationtoken.md) — Returns the token associated with the query generation currently in use by this context.
- [transactionAuthor](transactionauthor.md) — The author for the context that is used as an identifier in persistent history transactions.
- [- mergeChangesFromContextDidSaveNotification:](<mergechanges(fromcontextdidsave_).md>) — Merges the changes specified in a given notification.
- [- setQueryGenerationFromToken:error:](<setquerygenerationfrom(__).md>) — Sets the query generation this context should use.
