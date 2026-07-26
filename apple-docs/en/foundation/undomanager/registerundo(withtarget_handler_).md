---
title: 'registerUndo(withTarget:handler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/undomanager/registerundo(withtarget:handler:)'
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/registerundo(withtarget:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/registerundo%28withtarget%3Ahandler%3A%29.json'
content_hash: 'sha256:8b21ebae46c669cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# registerUndo(withTarget:handler:)

<sub>Instance Method</sub>

Registers the specified closure to implement a single undo operation that the target receives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func registerUndo<TargetType>(withTarget target: TargetType, handler: @escaping @MainActor (TargetType) -> Void) where TargetType : AnyObject
```

## Parameters

- `target` — The target of the undo operation. The undo manager maintains an unowned reference to the `target` to prevent retain cycles.

- `handler` — A closure to execute when an operation is undone. The closure takes a single argument, the target of the undo operation.

## Discussion

Use [registerUndo(withTarget:handler:)](<registerundo(withtarget_handler_).md>) to register a closure as an undo operation on the undo stack. The registered closure is then executed when `undo` is called and the undo operation occurs. The target needs to be a reference type so that its state can be undone or redone by the undo manager.

The following example demonstrates how you can use this method to register an undo operation that adds an element back into a mutable array.

```swift
var manager = UndoManager()
var bouquetSelection: NSMutableArray = ["lilac", "lavender"]
func pull(flower: String) {
    bouquetSelection.remove(flower)
    manager.registerUndo(withTarget: bouquetSelection) { $0.add(flower) }
}
pull(flower: "lilac")
// bouquetSelection == ["lavender"]
manager.undo()
// bouquetSelection == ["lavender", "lilac"]
```

To avoid retain cycles with the target, operate on the closure parameter rather than on variables in an outer scope that reference the same target. For example, in the code listing above, the closure operates on the `$0` parameter rather than directly on `bouquetSelection`.

## See Also

### Related Documentation

- [Introduction to Undo Architecture](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UndoArchitecture/UndoArchitecture.html#//apple_ref/doc/uid/10000010)

### Registering undo operations

- [- registerUndoWithTarget:selector:object:](<registerundo(withtarget_selector_object_).md>) — Registers the selector of the specified target to implement a single undo operation that the target receives.
- [- prepareWithInvocationTarget:](<prepare(withinvocationtarget_).md>) — Prepares the undo manager for invocation-based undo with the given target as the subject of the next undo operation.
