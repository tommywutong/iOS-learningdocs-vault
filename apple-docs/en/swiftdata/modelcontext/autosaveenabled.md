---
title: autosaveEnabled
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelcontext/autosaveenabled
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/autosaveenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/autosaveenabled.json'
content_hash: 'sha256:68eecb218e07dce3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# autosaveEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the context should automatically save any pending changes when certain events occur.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var autosaveEnabled: Bool { get set }
```

## Discussion

When `true`, the context calls [save()](<save().md>) after you make changes to any inserted or registered models. The context also calls `save()` at various times during the lifecycle of windows, scenes, views, and sheets.

The default value is `false`. SwiftData automatically sets this property to `true` for the model container’s [mainContext](../modelcontainer/maincontext.md).

## See Also

### Persisting unsaved changes

- [save()](<save().md>) — Writes any pending inserts, changes, and deletes to the persistent storage.
- [transaction(block:)](<transaction(block_).md>) — Runs the provided closure, and once it finishes, writes any pending inserts, changes, and deletes to the persistent storage.
- [rollback()](<rollback().md>) — Discards pending inserts and deletes, restores changed models to their most recent committed state, and empties the undo stack.
