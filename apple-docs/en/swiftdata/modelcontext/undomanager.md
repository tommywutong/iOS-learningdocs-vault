---
title: undoManager
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelcontext/undomanager
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/undomanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/undomanager.json'
content_hash: 'sha256:1e50c802cc8269a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# undoManager

<sub>Instance Property</sub>

The object that provides undo support for the context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var undoManager: UndoManager? { get set }
```

## Discussion

Assign an instance of [UndoManager](../../foundation/undomanager.md) to this property to enable undo support for the context. The undo manager can be exclusive to the context, or an existing manager should you want to integrate this context’s undo operations with those of the rest of your app.

If the context does use an undo manager, improve performance by temporarily setting this property to `nil` when performing expensive operations, such as importing large numbers of models.

The default value is `nil`.

## See Also

### Performing undo and redo

- [processPendingChanges()](<processpendingchanges().md>) — Tells the undo manager to record any changes made to the context’s registered models.
