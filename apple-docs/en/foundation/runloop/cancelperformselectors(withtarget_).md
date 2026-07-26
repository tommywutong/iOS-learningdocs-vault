---
title: 'cancelPerformSelectors(withTarget:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/runloop/cancelperformselectors(withtarget:)'
source_url: 'https://developer.apple.com/documentation/foundation/runloop/cancelperformselectors(withtarget:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/cancelperformselectors%28withtarget%3A%29.json'
content_hash: 'sha256:45901d4cc414437a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# cancelPerformSelectors(withTarget:)

<sub>Instance Method</sub>

Cancels all outstanding ordered performs scheduled with a given target.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancelPerformSelectors(withTarget target: Any)
```

## Parameters

- `target` — The previously-specified target.

## Discussion

This method cancels the previously scheduled messages associated with the target, ignoring the selector and argument of the scheduled operation. This is in contrast to [- cancelPerformSelector:target:argument:](<cancelperform(__target_argument_).md>), which requires you to match the selector and argument as well as the target. This method removes the perform requests for the object from all modes of the run loop.

## See Also

### Scheduling and Canceling Tasks

- [- performBlock:](<perform(__).md>) — Schedules a block that the run loop invokes.
- [- performInModes:block:](<perform(inmodes_block_).md>) — Schedules a block that the run loop invokes when it’s running in any of the specified modes.
- [- performSelector:target:argument:order:modes:](<perform(__target_argument_order_modes_).md>) — Schedules the sending of a message on the receiver.
- [- cancelPerformSelector:target:argument:](<cancelperform(__target_argument_).md>) — Cancels the sending of a previously scheduled message.
