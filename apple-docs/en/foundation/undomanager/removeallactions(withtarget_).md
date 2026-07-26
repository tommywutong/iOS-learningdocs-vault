---
title: 'removeAllActions(withTarget:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/undomanager/removeallactions(withtarget:)'
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/removeallactions(withtarget:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/removeallactions%28withtarget%3A%29.json'
content_hash: 'sha256:803650f0fc7bedac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# removeAllActions(withTarget:)

<sub>Instance Method</sub>

Clears the undo and redo stacks of all operations involving the specified target as the recipient of the undo message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeAllActions(withTarget target: Any)
```

## Parameters

- `target` — The recipient of the undo messages to be removed.

## Discussion

Doesn’t re-enable the manager if it’s disabled.

## See Also

### Related Documentation

- [- enableUndoRegistration](<enableundoregistration().md>) — Enables the recording of undo operations.

### Clearing undo operations

- [- removeAllActions](<removeallactions().md>) — Clears the undo and redo stacks and reenables the manager.
