---
title: canRedo
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/canredo
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/canredo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/canredo.json'
content_hash: 'sha256:fd8ce1f046034f7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# canRedo

<sub>Instance Property</sub>

A Boolean value that indicates whether the manager has any actions to redo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var canRedo: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the manager has any actions to redo, otherwise [false](../../swift/false.md).

Because any undo operation registered clears the redo stack, this method posts an [NSUndoManagerCheckpointNotification](../nsnotification/name-swift.struct/nsundomanagercheckpoint.md) to allow clients to apply their pending operations before testing the redo stack.

## See Also

### Related Documentation

- [- redo](<redo().md>) — Performs the operations in the last group on the redo stack, if there are any, recording them on the undo stack as a single group.

### Checking undo ability

- [canUndo](canundo.md) — A Boolean value that indicates whether the manager has any actions to undo.
