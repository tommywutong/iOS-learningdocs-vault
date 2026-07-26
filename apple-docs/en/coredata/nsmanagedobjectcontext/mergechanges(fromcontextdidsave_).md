---
title: 'mergeChanges(fromContextDidSave:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectcontext/mergechanges(fromcontextdidsave:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/mergechanges(fromcontextdidsave:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/mergechanges%28fromcontextdidsave%3A%29.json'
content_hash: 'sha256:c92535046dfa4c0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# mergeChanges(fromContextDidSave:)

<sub>Instance Method</sub>

Merges the changes specified in a given notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mergeChanges(fromContextDidSave notification: Notification)
```

## Parameters

- `notification` — An instance of an [NSManagedObjectContextDidSave](../../foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextdidsave.md) notification posted by another context.

## Discussion

This method refreshes any objects which have been updated in the other context, faults in any newly-inserted objects, and invokes [- deleteObject:](<delete(__).md>): on those which have been deleted.

You can pass a [NSManagedObjectContextDidSave](../../foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextdidsave.md) notification posted by a managed object context on another thread, however you must not use the managed objects in the user info dictionary directly. For more details, see Concurrency with Core Data.

> [!note] Note
> Objective-C uses instances of [NSManagedObjectContextDidSaveNotification](../nsmanagedobjectcontextdidsavenotification.md) instead of [NSManagedObjectContextDidSave](../../foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextdidsave.md).

## See Also

### Managing concurrency

- [NSManagedObjectContextQueryGenerationKey](../nsmanagedobjectcontextquerygenerationkey.md) — Constant used to reference the query generation token.
- [+ mergeChangesFromRemoteContextSave:intoContexts:](<mergechanges(fromremotecontextsave_into_).md>) — Handles changes from other processes or from a serialized state.
- [automaticallyMergesChangesFromParent](automaticallymergeschangesfromparent.md) — A Boolean value that indicates whether the context automatically merges changes saved to its persistent store coordinator or parent context.
- [concurrencyType](concurrencytype-swift.property.md) — The concurrency type for the context.
- [mergePolicy](mergepolicy.md) — The merge policy of the context.
- [queryGenerationToken](querygenerationtoken.md) — Returns the token associated with the query generation currently in use by this context.
- [transactionAuthor](transactionauthor.md) — The author for the context that is used as an identifier in persistent history transactions.
- [- setQueryGenerationFromToken:error:](<setquerygenerationfrom(__).md>) — Sets the query generation this context should use.
