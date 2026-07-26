---
title: NSUndoCloseGroupingRunLoopOrdering
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsundoclosegroupingrunloopordering
source_url: 'https://developer.apple.com/documentation/foundation/nsundoclosegroupingrunloopordering'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsundoclosegroupingrunloopordering.json'
content_hash: 'sha256:55709e2bf6ff6825'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUndoCloseGroupingRunLoopOrdering

<sub>Global Variable</sub>

A priority to use when using a run loop to close an undo group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSUndoCloseGroupingRunLoopOrdering: Int { get }
```

## Discussion

Use this value as the `order` parameter if you call [- performSelector:target:argument:order:modes:](<runloop/perform(__target_argument_order_modes_).md>) to have a [RunLoop](runloop.md) perform a selector that closes an undo group.

## See Also

### Working with run loops

- [runLoopModes](undomanager/runloopmodes.md) — The modes governing the types of input to handle during a cycle of the run loop.
