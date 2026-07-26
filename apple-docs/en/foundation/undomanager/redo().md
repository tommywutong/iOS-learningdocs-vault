---
title: redo()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/redo()
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/redo()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/redo%28%29.json'
content_hash: 'sha256:f34a01fafbdb79eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# redo()

<sub>Instance Method</sub>

Performs the operations in the last group on the redo stack, if there are any, recording them on the undo stack as a single group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func redo()
```

## Discussion

Raises an [NSInternalInconsistencyException](../nsexceptionname/internalinconsistencyexception.md) if the method is invoked during an undo operation.

This method posts an [NSUndoManagerCheckpointNotification](../nsnotification/name-swift.struct/nsundomanagercheckpoint.md) and [NSUndoManagerWillRedoChangeNotification](../nsnotification/name-swift.struct/nsundomanagerwillredochange.md) before it performs the redo operation, and it posts the [NSUndoManagerDidRedoChangeNotification](../nsnotification/name-swift.struct/nsundomanagerdidredochange.md) after it performs the redo operation.

## See Also

### Related Documentation

- [- registerUndoWithTarget:selector:object:](<registerundo(withtarget_selector_object_).md>) — Registers the selector of the specified target to implement a single undo operation that the target receives.

### Performing undo and redo

- [- undo](<undo().md>) — Closes the top-level undo group if necessary, and then performs undo operations on the group.
- [- undoNestedGroup](<undonestedgroup().md>) — Performs the undo operations in the last undo group (whether top-level or nested), recording the operations on the redo stack as a single group.
