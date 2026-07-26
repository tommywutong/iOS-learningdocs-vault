---
title: save()
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelcontext/save()
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/save()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/save%28%29.json'
content_hash: 'sha256:83347117c8a7e7f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# save()

<sub>Instance Method</sub>

Writes any pending inserts, changes, and deletes to the persistent storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func save() throws
```

## Discussion

> [!important] Important
> Use the [hasChanges](haschanges.md) property to determine whether the context has uncommitted changes before invoking this method. Otherwise, SwiftData may perform unnecessary work.

## See Also

### Persisting unsaved changes

- [autosaveEnabled](autosaveenabled.md) — A Boolean value that indicates whether the context should automatically save any pending changes when certain events occur.
- [transaction(block:)](<transaction(block_).md>) — Runs the provided closure, and once it finishes, writes any pending inserts, changes, and deletes to the persistent storage.
- [rollback()](<rollback().md>) — Discards pending inserts and deletes, restores changed models to their most recent committed state, and empties the undo stack.
