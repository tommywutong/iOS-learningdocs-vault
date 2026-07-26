---
title: 'perform(_:target:argument:order:modes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/runloop/perform(_:target:argument:order:modes:)'
source_url: 'https://developer.apple.com/documentation/foundation/runloop/perform(_:target:argument:order:modes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/perform%28_%3Atarget%3Aargument%3Aorder%3Amodes%3A%29.json'
content_hash: 'sha256:31f9dbe7c4cb7f67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# perform(_:target:argument:order:modes:)

<sub>Instance Method</sub>

Schedules the sending of a message on the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func perform(_ aSelector: Selector, target: Any, argument arg: Any?, order: Int, modes: [RunLoop.Mode])
```

## Parameters

- `aSelector` — A selector that identifies the method to invoke. This method should not have a significant return value and should take a single argument of type id.

- `target` — The object that defines the selector in `aSelector`.

- `arg` — The argument to pass to the method when it is invoked. Pass `nil` if the method does not take an argument.

- `order` — The priority for the message. If multiple messages are scheduled, the messages with a lower order value are sent before messages with a higher order value.

- `modes` — An array of input modes for which the message may be sent. You may specify custom modes or use one of the modes listed in `Run Loop Modes`.

## Discussion

This method sets up a timer to perform the `aSelector` message on the receiver at the start of the next run loop iteration. The timer is configured to run in the modes specified by the `modes` parameter. When the timer fires, the thread attempts to dequeue the message from the run loop and perform the selector. It succeeds if the run loop is running and in one of the specified modes; otherwise, the timer waits until the run loop is in one of those modes.

This method returns before the `aSelector` message is sent. The receiver retains the `target` and `anArgument` objects until the timer for the selector fires, and then releases them as part of its cleanup.

Use this method if you want multiple messages to be sent after the current event has been processed and you want to make sure these messages are sent in a certain order.

## See Also

### Scheduling and Canceling Tasks

- [- performBlock:](<perform(__).md>) — Schedules a block that the run loop invokes.
- [- performInModes:block:](<perform(inmodes_block_).md>) — Schedules a block that the run loop invokes when it’s running in any of the specified modes.
- [- cancelPerformSelector:target:argument:](<cancelperform(__target_argument_).md>) — Cancels the sending of a previously scheduled message.
- [- cancelPerformSelectorsWithTarget:](<cancelperformselectors(withtarget_).md>) — Cancels all outstanding ordered performs scheduled with a given target.
