---
title: 'registerUndoWithTarget:handler:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsundomanager/registerundowithtarget:handler:'
source_url: 'https://developer.apple.com/documentation/foundation/nsundomanager/registerundowithtarget:handler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsundomanager/registerundowithtarget%3Ahandler%3A.json'
content_hash: 'sha256:bbc6b05a5c320219'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# registerUndoWithTarget:handler:

<sub>Instance Method</sub>

Records a single undo operation for a given target so that when the manager performs an undo, it executes the specified block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) registerUndoWithTarget:(id) target handler:(void (^)(id)) undoHandler;
```

## Parameters

- `target` — The target of the undo operation.

- `undoHandler` — A block to be executed when an operation is undone. The block takes a single argument, the target of the undo operation.

## See Also

### Registering undo operations

- [- registerUndoWithTarget:selector:object:](<../undomanager/registerundo(withtarget_selector_object_).md>) — Registers the selector of the specified target to implement a single undo operation that the target receives.
- [- prepareWithInvocationTarget:](<../undomanager/prepare(withinvocationtarget_).md>) — Prepares the undo manager for invocation-based undo with the given target as the subject of the next undo operation.
