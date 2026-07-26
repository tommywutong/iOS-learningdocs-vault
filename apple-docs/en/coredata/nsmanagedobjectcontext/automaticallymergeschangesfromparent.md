---
title: automaticallyMergesChangesFromParent
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/automaticallymergeschangesfromparent
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/automaticallymergeschangesfromparent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/automaticallymergeschangesfromparent.json'
content_hash: 'sha256:302a64a5e141a33d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# automaticallyMergesChangesFromParent

<sub>Instance Property</sub>

A Boolean value that indicates whether the context automatically merges changes saved to its persistent store coordinator or parent context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var automaticallyMergesChangesFromParent: Bool { get set }
```

## See Also

### Managing concurrency

- [NSManagedObjectContextQueryGenerationKey](../nsmanagedobjectcontextquerygenerationkey.md) — Constant used to reference the query generation token.
- [+ mergeChangesFromRemoteContextSave:intoContexts:](<mergechanges(fromremotecontextsave_into_).md>) — Handles changes from other processes or from a serialized state.
- [concurrencyType](concurrencytype-swift.property.md) — The concurrency type for the context.
- [mergePolicy](mergepolicy.md) — The merge policy of the context.
- [queryGenerationToken](querygenerationtoken.md) — Returns the token associated with the query generation currently in use by this context.
- [transactionAuthor](transactionauthor.md) — The author for the context that is used as an identifier in persistent history transactions.
- [- mergeChangesFromContextDidSaveNotification:](<mergechanges(fromcontextdidsave_).md>) — Merges the changes specified in a given notification.
- [- setQueryGenerationFromToken:error:](<setquerygenerationfrom(__).md>) — Sets the query generation this context should use.
