---
title: runLoopModes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/runloopmodes
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/runloopmodes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/runloopmodes.json'
content_hash: 'sha256:e8ed0c21d51efabe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# runLoopModes

<sub>Instance Property</sub>

The modes governing the types of input to handle during a cycle of the run loop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var runLoopModes: [RunLoop.Mode] { get set }
```

## Discussion

An array of string constants specifying the current run-loop modes.

By default, the sole run-loop mode is `NSDefaultRunLoopMode` (which excludes data from `NSConnection` objects). Some examples of other uses are to limit the input to data received during a mouse-tracking session by setting the mode to `NSEventTrackingRunLoopMode`, or limit it to data received from a modal panel with `NSModalPanelRunLoopMode`.

## See Also

### Related Documentation

- [- performSelector:target:argument:order:modes:](<../runloop/perform(__target_argument_order_modes_).md>) — Schedules the sending of a message on the receiver.

### Working with run loops

- [NSUndoCloseGroupingRunLoopOrdering](../nsundoclosegroupingrunloopordering.md) — A priority to use when using a run loop to close an undo group.
