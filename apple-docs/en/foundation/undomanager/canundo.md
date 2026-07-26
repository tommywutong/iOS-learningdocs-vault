---
title: canUndo
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/canundo
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/canundo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/canundo.json'
content_hash: 'sha256:939918ce0cb01a1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# canUndo

<sub>Instance Property</sub>

A Boolean value that indicates whether the manager has any actions to undo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var canUndo: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the manager has any actions to undo, otherwise [false](../../swift/false.md).

The return value doesn’t mean you can safely invoke [- undo](<undo().md>) or [- undoNestedGroup](<undonestedgroup().md>)—you may have to close open undo groups first.

## See Also

### Related Documentation

- [- registerUndoWithTarget:selector:object:](<registerundo(withtarget_selector_object_).md>) — Registers the selector of the specified target to implement a single undo operation that the target receives.
- [- enableUndoRegistration](<enableundoregistration().md>) — Enables the recording of undo operations.

### Checking undo ability

- [canRedo](canredo.md) — A Boolean value that indicates whether the manager has any actions to redo.
