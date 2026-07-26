---
title: redoCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/redocount
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/redocount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/redocount.json'
content_hash: 'sha256:c435a5968a7c12ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# redoCount

<sub>Instance Property</sub>

The number of times you can invoke redo before there are no actions left to redo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var redoCount: Int { get }
```

## See Also

### Managing undo and redo stack depth

- [levelsOfUndo](levelsofundo.md) — The maximum number of top-level undo groups the undo manager holds.
- [undoCount](undocount.md) — The number of times you can invoke undo before there are no actions left to undo.
