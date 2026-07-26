---
title: endUndoGrouping()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/endundogrouping()
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/endundogrouping()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/endundogrouping%28%29.json'
content_hash: 'sha256:122a8be070858e5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# endUndoGrouping()

<sub>Instance Method</sub>

Marks the end of an undo group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func endUndoGrouping()
```

## Discussion

All individual undo operations back to the matching [- beginUndoGrouping](<beginundogrouping().md>) message are grouped together and reversed by a later [- undo](<undo().md>) or [- undoNestedGroup](<undonestedgroup().md>) message. Undo groups can be nested, thus providing functionality similar to nested transactions. Raises an `NSInternalInconsistencyException` if there’s no [- beginUndoGrouping](<beginundogrouping().md>) message in effect.

This method posts an [NSUndoManagerCheckpointNotification](../nsnotification/name-swift.struct/nsundomanagercheckpoint.md) and an [NSUndoManagerDidCloseUndoGroupNotification](../nsnotification/name-swift.struct/nsundomanagerdidcloseundogroup.md) just before the group is closed.

## See Also

### Related Documentation

- [levelsOfUndo](levelsofundo.md) — The maximum number of top-level undo groups the undo manager holds.

### Creating undo groups

- [- beginUndoGrouping](<beginundogrouping().md>) — Marks the beginning of an undo group.
- [groupsByEvent](groupsbyevent.md) — A Boolean value that indicates whether the manager automatically creates undo groups around each pass of the run loop.
- [groupingLevel](groupinglevel.md) — The number of nested undo groups (or redo groups, if redo is the most recent operation) in the current event loop.
