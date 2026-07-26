---
title: beginUndoGrouping()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/beginundogrouping()
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/beginundogrouping()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/beginundogrouping%28%29.json'
content_hash: 'sha256:a69583d101c57ef6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# beginUndoGrouping()

<sub>Instance Method</sub>

Marks the beginning of an undo group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func beginUndoGrouping()
```

## Discussion

All individual undo operations before a subsequent [- endUndoGrouping](<endundogrouping().md>) message are grouped together and reversed by a later [- undo](<undo().md>) message. By default undo groups are begun automatically at the start of the event loop, but you can begin your own undo groups with this method, and nest them within other groups.

This method posts an [NSUndoManagerCheckpointNotification](../nsnotification/name-swift.struct/nsundomanagercheckpoint.md) unless a top-level undo is in progress. It posts an [NSUndoManagerDidOpenUndoGroupNotification](../nsnotification/name-swift.struct/nsundomanagerdidopenundogroup.md) if a new group was successfully created.

## See Also

### Creating undo groups

- [- endUndoGrouping](<endundogrouping().md>) — Marks the end of an undo group.
- [groupsByEvent](groupsbyevent.md) — A Boolean value that indicates whether the manager automatically creates undo groups around each pass of the run loop.
- [groupingLevel](groupinglevel.md) — The number of nested undo groups (or redo groups, if redo is the most recent operation) in the current event loop.
