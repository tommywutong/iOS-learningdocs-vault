---
title: processPendingChanges()
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelcontext/processpendingchanges()
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/processpendingchanges()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/processpendingchanges%28%29.json'
content_hash: 'sha256:ef899aa802d61f70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# processPendingChanges()

<sub>Instance Method</sub>

Tells the undo manager to record any changes made to the context’s registered models.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func processPendingChanges()
```

## Discussion

In AppKit-based applications, the system invokes this method at the end of each event loop. The framework may call it more frequently if it needs to coalesce your changes before continuing. You can also invoke it manually to coalesce any pending changes.

## See Also

### Performing undo and redo

- [undoManager](undomanager.md) — The object that provides undo support for the context.
