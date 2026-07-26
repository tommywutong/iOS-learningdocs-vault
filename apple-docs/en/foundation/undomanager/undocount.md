---
title: undoCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/undocount
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/undocount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/undocount.json'
content_hash: 'sha256:9a8620a09932e2ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# undoCount

<sub>Instance Property</sub>

The number of times you can invoke undo before there are no actions left to undo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var undoCount: Int { get }
```

## Discussion

A nonzero value doesn’t imply you can safely invoke [- undo](<undo().md>) immediately, because you may have to close open undo groups first.

## See Also

### Managing undo and redo stack depth

- [levelsOfUndo](levelsofundo.md) — The maximum number of top-level undo groups the undo manager holds.
- [redoCount](redocount.md) — The number of times you can invoke redo before there are no actions left to redo.
