---
title: groupsByEvent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/groupsbyevent
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/groupsbyevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/groupsbyevent.json'
content_hash: 'sha256:e43d760221de8015'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# groupsByEvent

<sub>Instance Property</sub>

A Boolean value that indicates whether the manager automatically creates undo groups around each pass of the run loop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var groupsByEvent: Bool { get set }
```

## Discussion

[true](../../swift/true.md) if the manager automatically creates undo groups around each pass of the run loop, otherwise [false](../../swift/false.md).

The default is [true](../../swift/true.md). If you turn automatic grouping off, you must close groups explicitly before invoking either [- undo](<undo().md>) or [- undoNestedGroup](<undonestedgroup().md>).

## See Also

### Creating undo groups

- [- beginUndoGrouping](<beginundogrouping().md>) — Marks the beginning of an undo group.
- [- endUndoGrouping](<endundogrouping().md>) — Marks the end of an undo group.
- [groupingLevel](groupinglevel.md) — The number of nested undo groups (or redo groups, if redo is the most recent operation) in the current event loop.
