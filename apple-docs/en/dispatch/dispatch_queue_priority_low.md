---
title: DISPATCH_QUEUE_PRIORITY_LOW
framework: Dispatch
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_queue_priority_low
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_queue_priority_low'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_queue_priority_low.json'
content_hash: 'sha256:06b9c24b97fb6d8b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DISPATCH_QUEUE_PRIORITY_LOW

<sub>Global Variable</sub>

Tasks run at a low priority, which is equivalent to the utility quality-of-service level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var DISPATCH_QUEUE_PRIORITY_LOW: Int32 { get }
```

## Discussion

Use quality-of-service constants instead. This constant maps to the `QOS_CLASS_UTILITY` class.

Items dispatched to the queue run at low priority; the queue is scheduled for execution after all default priority and high priority queues have been scheduled.

## See Also

### Priorities

- [DISPATCH_QUEUE_PRIORITY_HIGH](dispatch_queue_priority_high.md) — Tasks run at the highest priority, which is equivalent to the user-initiated quality-of-service level.
- [DISPATCH_QUEUE_PRIORITY_DEFAULT](dispatch_queue_priority_default.md) — Tasks run at the default priority, which is equivalent to the default quality-of-service.
- [DISPATCH_QUEUE_PRIORITY_BACKGROUND](dispatch_queue_priority_background.md) — Tasks run at the background priority, which is equivalent to the background quality-of-service level.
