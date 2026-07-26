---
title: 'transaction(block:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelcontext/transaction(block:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/transaction(block:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/transaction%28block%3A%29.json'
content_hash: 'sha256:9e22e5724c482659'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# transaction(block:)

<sub>Instance Method</sub>

Runs the provided closure, and once it finishes, writes any pending inserts, changes, and deletes to the persistent storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func transaction(block: () throws -> Void) throws
```

## Parameters

- `block` — The closure to run before performing a save operation.

## See Also

### Persisting unsaved changes

- [autosaveEnabled](autosaveenabled.md) — A Boolean value that indicates whether the context should automatically save any pending changes when certain events occur.
- [save()](<save().md>) — Writes any pending inserts, changes, and deletes to the persistent storage.
- [rollback()](<rollback().md>) — Discards pending inserts and deletes, restores changed models to their most recent committed state, and empties the undo stack.
