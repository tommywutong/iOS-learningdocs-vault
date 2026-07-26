---
title: DISPATCH_QUEUE_PRIORITY_BACKGROUND
framework: Dispatch
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_queue_priority_background
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_queue_priority_background'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_queue_priority_background.json'
content_hash: 'sha256:1cefb18819bc3344'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DISPATCH_QUEUE_PRIORITY_BACKGROUND

<sub>Global Variable</sub>

Tasks run at the background priority, which is equivalent to the background quality-of-service level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var DISPATCH_QUEUE_PRIORITY_BACKGROUND: Int32 { get }
```

## Discussion

Use quality-of-service constants instead. This constant maps to the `QOS_CLASS_BACKGROUND` class.

Items dispatched to the queue run at background priority; the queue is scheduled for execution after all high priority queues have been scheduled and the system runs items on a thread whose priority is set for background status. Such a thread has the lowest priority and any disk I/O is throttled to minimize the impact on the system.

## See Also

### Priorities

- [DISPATCH_QUEUE_PRIORITY_HIGH](dispatch_queue_priority_high.md) — Tasks run at the highest priority, which is equivalent to the user-initiated quality-of-service level.
- [DISPATCH_QUEUE_PRIORITY_DEFAULT](dispatch_queue_priority_default.md) — Tasks run at the default priority, which is equivalent to the default quality-of-service.
- [DISPATCH_QUEUE_PRIORITY_LOW](dispatch_queue_priority_low.md) — Tasks run at a low priority, which is equivalent to the utility quality-of-service level.
