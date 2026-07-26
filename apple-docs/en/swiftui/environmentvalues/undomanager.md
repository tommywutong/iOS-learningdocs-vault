---
title: undoManager
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/undomanager
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/undomanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/undomanager.json'
content_hash: 'sha256:5ad8ca8a9c4cf443'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# undoManager

<sub>Instance Property</sub>

The undo manager used to register a view’s undo operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var undoManager: UndoManager? { get }
```

## Discussion

This value is `nil` when the environment represents a context that doesn’t support undo and redo operations. You can skip registration of an undo operation when this value is `nil`.

## See Also

### Accessing document configuration

- [documentConfiguration](documentconfiguration.md) — The configuration of a document in a [DocumentGroup](../documentgroup.md).
- [DocumentConfiguration](../documentconfiguration.md) — The configuration of a document in a [DocumentGroup](../documentgroup.md).
