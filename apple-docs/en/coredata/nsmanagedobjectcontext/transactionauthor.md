---
title: transactionAuthor
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/transactionauthor
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/transactionauthor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/transactionauthor.json'
content_hash: 'sha256:65d9b7f1c08b9512'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# transactionAuthor

<sub>Instance Property</sub>

The author for the context that is used as an identifier in persistent history transactions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var transactionAuthor: String? { get set }
```

## Discussion

Set a managed object context’s [transactionAuthor](transactionauthor.md) before saving it to differentiate among multiple call sites that modify the same context. Doing this records an [author](../nspersistenthistorytransaction/author.md) in subsequent transactions.

```swift
func addColor(_ name: String, in context: NSManagedObjectContext) {
    let color = Color(context: context)
    color.name = name
    color.creationDate = Date()

    // set the transaction author
    context.transactionAuthor = "addColor"
    persistentContainer.saveContext(context)
    context.transactionAuthor = nil
}
```

Reset the context’s [transactionAuthor](transactionauthor.md) to nil after the save to prevent misattribution of future transactions.

## See Also

### Managing concurrency

- [NSManagedObjectContextQueryGenerationKey](../nsmanagedobjectcontextquerygenerationkey.md) — Constant used to reference the query generation token.
- [+ mergeChangesFromRemoteContextSave:intoContexts:](<mergechanges(fromremotecontextsave_into_).md>) — Handles changes from other processes or from a serialized state.
- [automaticallyMergesChangesFromParent](automaticallymergeschangesfromparent.md) — A Boolean value that indicates whether the context automatically merges changes saved to its persistent store coordinator or parent context.
- [concurrencyType](concurrencytype-swift.property.md) — The concurrency type for the context.
- [mergePolicy](mergepolicy.md) — The merge policy of the context.
- [queryGenerationToken](querygenerationtoken.md) — Returns the token associated with the query generation currently in use by this context.
- [- mergeChangesFromContextDidSaveNotification:](<mergechanges(fromcontextdidsave_).md>) — Merges the changes specified in a given notification.
- [- setQueryGenerationFromToken:error:](<setquerygenerationfrom(__).md>) — Sets the query generation this context should use.
