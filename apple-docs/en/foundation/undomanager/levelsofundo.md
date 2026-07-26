---
title: levelsOfUndo
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/levelsofundo
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/levelsofundo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/levelsofundo.json'
content_hash: 'sha256:c5a1f9ce8a6a35e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# levelsOfUndo

<sub>Instance Property</sub>

The maximum number of top-level undo groups the undo manager holds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var levelsOfUndo: Int { get set }
```

## Discussion

An integer specifying the number of undo groups. A limit of `0` indicates no limit, so the manager never drops old undo groups.

When ending an undo group results in the number of groups exceeding this limit, the manager drops the oldest groups from the stack. The default is `0`.

If you change the limit to a level below the prior limit, the manager immediately drops old undo groups.

## See Also

### Related Documentation

- [- enableUndoRegistration](<enableundoregistration().md>) — Enables the recording of undo operations.

### Managing undo and redo stack depth

- [undoCount](undocount.md) — The number of times you can invoke undo before there are no actions left to undo.
- [redoCount](redocount.md) — The number of times you can invoke redo before there are no actions left to redo.
