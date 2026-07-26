---
title: 'perform(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/runloop/perform(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/runloop/perform(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/perform%28_%3A%29.json'
content_hash: 'sha256:f3ee3bc72aa82d5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# perform(_:)

<sub>Instance Method</sub>

Schedules a block that the run loop invokes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func perform(_ block: @escaping @Sendable () -> Void)
```

## Parameters

- `block` — A block that the run loop invokes.

## See Also

### Scheduling and Canceling Tasks

- [- performInModes:block:](<perform(inmodes_block_).md>) — Schedules a block that the run loop invokes when it’s running in any of the specified modes.
- [- performSelector:target:argument:order:modes:](<perform(__target_argument_order_modes_).md>) — Schedules the sending of a message on the receiver.
- [- cancelPerformSelector:target:argument:](<cancelperform(__target_argument_).md>) — Cancels the sending of a previously scheduled message.
- [- cancelPerformSelectorsWithTarget:](<cancelperformselectors(withtarget_).md>) — Cancels all outstanding ordered performs scheduled with a given target.
