---
title: DISPATCH_QUEUE_PRIORITY_HIGH
framework: Dispatch
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_queue_priority_high
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_queue_priority_high'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_queue_priority_high.json'
content_hash: 'sha256:1cbfd2ff3456b47f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DISPATCH_QUEUE_PRIORITY_HIGH

<sub>Global Variable</sub>

Tasks run at the highest priority, which is equivalent to the user-initiated quality-of-service level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var DISPATCH_QUEUE_PRIORITY_HIGH: Int32 { get }
```

## Discussion

Use quality-of-service constants instead. This constant maps to the `QOS_CLASS_USER_INITIATED` class.

Items dispatched to the queue run at high priority; the queue is scheduled for execution before any default priority or low priority queue.

## See Also

### Priorities

- [DISPATCH_QUEUE_PRIORITY_DEFAULT](dispatch_queue_priority_default.md) — Tasks run at the default priority, which is equivalent to the default quality-of-service.
- [DISPATCH_QUEUE_PRIORITY_LOW](dispatch_queue_priority_low.md) — Tasks run at a low priority, which is equivalent to the utility quality-of-service level.
- [DISPATCH_QUEUE_PRIORITY_BACKGROUND](dispatch_queue_priority_background.md) — Tasks run at the background priority, which is equivalent to the background quality-of-service level.
