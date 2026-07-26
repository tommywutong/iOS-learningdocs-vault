---
title: redoActionIsDiscardable
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/redoactionisdiscardable
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/redoactionisdiscardable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/redoactionisdiscardable.json'
content_hash: 'sha256:eebe26e1b4701cfb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# redoActionIsDiscardable

<sub>Instance Property</sub>

A Boolean value that indicates whether the next redo action is discardable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var redoActionIsDiscardable: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the action is discardable; [false](../../swift/false.md) otherwise.

Specifies that the latest redo action may be safely discarded when a document can not be saved for any reason. These are typically actions that don’t affect persistent state.

An example might be an redo action that changes the viewable area of a document.

## See Also

### Using discardable undo and redo actions

- [- setActionIsDiscardable:](<setactionisdiscardable(__).md>) — Sets whether the next undo or redo action is discardable.
- [undoActionIsDiscardable](undoactionisdiscardable.md) — A Boolean value that indicates whether the next undo action is discardable.
