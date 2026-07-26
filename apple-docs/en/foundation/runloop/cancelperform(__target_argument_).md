---
title: 'cancelPerform(_:target:argument:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/runloop/cancelperform(_:target:argument:)'
source_url: 'https://developer.apple.com/documentation/foundation/runloop/cancelperform(_:target:argument:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/cancelperform%28_%3Atarget%3Aargument%3A%29.json'
content_hash: 'sha256:fad15ccf54dde5e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# cancelPerform(_:target:argument:)

<sub>Instance Method</sub>

Cancels the sending of a previously scheduled message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancelPerform(_ aSelector: Selector, target: Any, argument arg: Any?)
```

## Parameters

- `aSelector` — The previously-specified selector.

- `target` — The previously-specified target.

- `arg` — The previously-specified argument.

## Discussion

You can use this method to cancel a message previously scheduled using the [- performSelector:target:argument:order:modes:](<perform(__target_argument_order_modes_).md>) method. The parameters identify the message you want to cancel and must match those originally specified when the selector was scheduled. This method removes the perform request from all modes of the run loop.

## See Also

### Scheduling and Canceling Tasks

- [- performBlock:](<perform(__).md>) — Schedules a block that the run loop invokes.
- [- performInModes:block:](<perform(inmodes_block_).md>) — Schedules a block that the run loop invokes when it’s running in any of the specified modes.
- [- performSelector:target:argument:order:modes:](<perform(__target_argument_order_modes_).md>) — Schedules the sending of a message on the receiver.
- [- cancelPerformSelectorsWithTarget:](<cancelperformselectors(withtarget_).md>) — Cancels all outstanding ordered performs scheduled with a given target.
