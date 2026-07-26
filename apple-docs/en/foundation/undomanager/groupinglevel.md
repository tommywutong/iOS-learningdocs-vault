---
title: groupingLevel
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/groupinglevel
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/groupinglevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/groupinglevel.json'
content_hash: 'sha256:fb430f99f460c017'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# groupingLevel

<sub>Instance Property</sub>

The number of nested undo groups (or redo groups, if redo is the most recent operation) in the current event loop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var groupingLevel: Int { get }
```

## Discussion

An integer indicating the number of nested groups. If 0 is returned, there is no open undo or redo group.

## See Also

### Related Documentation

- [levelsOfUndo](levelsofundo.md) — The maximum number of top-level undo groups the undo manager holds.

### Creating undo groups

- [- beginUndoGrouping](<beginundogrouping().md>) — Marks the beginning of an undo group.
- [- endUndoGrouping](<endundogrouping().md>) — Marks the end of an undo group.
- [groupsByEvent](groupsbyevent.md) — A Boolean value that indicates whether the manager automatically creates undo groups around each pass of the run loop.
