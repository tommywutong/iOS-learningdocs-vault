---
title: undoNestedGroup()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/undonestedgroup()
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/undonestedgroup()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/undonestedgroup%28%29.json'
content_hash: 'sha256:ef55d35b23d7952b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# undoNestedGroup()

<sub>Instance Method</sub>

Performs the undo operations in the last undo group (whether top-level or nested), recording the operations on the redo stack as a single group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func undoNestedGroup()
```

## Discussion

Raises an `NSInternalInconsistencyException` if any undo operations have been registered since the last [- enableUndoRegistration](<enableundoregistration().md>) message.

This method posts an [NSUndoManagerCheckpointNotification](../nsnotification/name-swift.struct/nsundomanagercheckpoint.md) and [NSUndoManagerWillUndoChangeNotification](../nsnotification/name-swift.struct/nsundomanagerwillundochange.md) before it performs the undo operation, and it posts an [NSUndoManagerDidUndoChangeNotification](../nsnotification/name-swift.struct/nsundomanagerdidundochange.md) after it performs the undo operation.

## See Also

### Performing undo and redo

- [- undo](<undo().md>) — Closes the top-level undo group if necessary, and then performs undo operations on the group.
- [- redo](<redo().md>) — Performs the operations in the last group on the redo stack, if there are any, recording them on the undo stack as a single group.
