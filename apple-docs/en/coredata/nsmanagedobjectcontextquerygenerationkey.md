---
title: NSManagedObjectContextQueryGenerationKey
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontextquerygenerationkey
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextquerygenerationkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontextquerygenerationkey.json'
content_hash: 'sha256:6be931886d370e25'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSManagedObjectContextQueryGenerationKey

<sub>Global Variable</sub>

Constant used to reference the query generation token.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSManagedObjectContextQueryGenerationKey: String
```

## See Also

### Managing concurrency

- [+ mergeChangesFromRemoteContextSave:intoContexts:](<nsmanagedobjectcontext/mergechanges(fromremotecontextsave_into_).md>) — Handles changes from other processes or from a serialized state.
- [automaticallyMergesChangesFromParent](nsmanagedobjectcontext/automaticallymergeschangesfromparent.md) — A Boolean value that indicates whether the context automatically merges changes saved to its persistent store coordinator or parent context.
- [concurrencyType](nsmanagedobjectcontext/concurrencytype-swift.property.md) — The concurrency type for the context.
- [mergePolicy](nsmanagedobjectcontext/mergepolicy.md) — The merge policy of the context.
- [queryGenerationToken](nsmanagedobjectcontext/querygenerationtoken.md) — Returns the token associated with the query generation currently in use by this context.
- [transactionAuthor](nsmanagedobjectcontext/transactionauthor.md) — The author for the context that is used as an identifier in persistent history transactions.
- [- mergeChangesFromContextDidSaveNotification:](<nsmanagedobjectcontext/mergechanges(fromcontextdidsave_).md>) — Merges the changes specified in a given notification.
- [- setQueryGenerationFromToken:error:](<nsmanagedobjectcontext/setquerygenerationfrom(__).md>) — Sets the query generation this context should use.
