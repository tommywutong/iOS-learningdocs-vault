---
title: 'prepare(withInvocationTarget:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/undomanager/prepare(withinvocationtarget:)'
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/prepare(withinvocationtarget:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/prepare%28withinvocationtarget%3A%29.json'
content_hash: 'sha256:f4e085de16bfd27f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# prepare(withInvocationTarget:)

<sub>Instance Method</sub>

Prepares the undo manager for invocation-based undo with the given target as the subject of the next undo operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prepare(withInvocationTarget target: Any) -> Any
```

## Parameters

- `target` — The target of the undo operation. The undo manager maintains a weak reference to `target`.

## Return Value

A proxy object that forwards messages to the undo manager for recording as undo actions.

## See Also

### Registering undo operations

- [registerUndo(withTarget:handler:)](<registerundo(withtarget_handler_).md>) — Registers the specified closure to implement a single undo operation that the target receives.
- [- registerUndoWithTarget:selector:object:](<registerundo(withtarget_selector_object_).md>) — Registers the selector of the specified target to implement a single undo operation that the target receives.
