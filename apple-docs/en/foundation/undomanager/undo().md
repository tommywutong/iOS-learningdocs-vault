---
title: undo()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/undo()
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/undo()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/undo%28%29.json'
content_hash: 'sha256:dc411faf2fbb1b6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# undo()

<sub>Instance Method</sub>

Closes the top-level undo group if necessary, and then performs undo operations on the group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func undo()
```

## Discussion

After closing the top-level undo group, this method invokes [- undoNestedGroup](<undonestedgroup().md>).

This method also invokes [- endUndoGrouping](<endundogrouping().md>) if the nesting level is 1. Raises an `NSInternalInconsistencyException` if more than one undo group is open (that is, if the last group isn’t at the top level).

This method posts an [NSUndoManagerCheckpointNotification](../nsnotification/name-swift.struct/nsundomanagercheckpoint.md).

## See Also

### Related Documentation

- [groupingLevel](groupinglevel.md) — The number of nested undo groups (or redo groups, if redo is the most recent operation) in the current event loop.
- [- enableUndoRegistration](<enableundoregistration().md>) — Enables the recording of undo operations.

### Performing undo and redo

- [- undoNestedGroup](<undonestedgroup().md>) — Performs the undo operations in the last undo group (whether top-level or nested), recording the operations on the redo stack as a single group.
- [- redo](<redo().md>) — Performs the operations in the last group on the redo stack, if there are any, recording them on the undo stack as a single group.
