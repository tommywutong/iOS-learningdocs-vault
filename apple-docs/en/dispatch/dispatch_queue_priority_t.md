---
title: dispatch_queue_priority_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_queue_priority_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_queue_priority_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_queue_priority_t.json'
content_hash: 'sha256:44899a46c52a8b20'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_queue_priority_t

<sub>Type Alias</sub>

The execution priority for tasks in a global concurrent queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef long dispatch_queue_priority_t;
```

## Discussion

In macOS 10.10 and later, use quality-of-service (QoS) classes to specify the priority of tasks instead.

## Topics

### Priorities

- [DISPATCH_QUEUE_PRIORITY_HIGH](dispatch_queue_priority_high.md) — Tasks run at the highest priority, which is equivalent to the user-initiated quality-of-service level.
- [DISPATCH_QUEUE_PRIORITY_DEFAULT](dispatch_queue_priority_default.md) — Tasks run at the default priority, which is equivalent to the default quality-of-service.
- [DISPATCH_QUEUE_PRIORITY_LOW](dispatch_queue_priority_low.md) — Tasks run at a low priority, which is equivalent to the utility quality-of-service level.
- [DISPATCH_QUEUE_PRIORITY_BACKGROUND](dispatch_queue_priority_background.md) — Tasks run at the background priority, which is equivalent to the background quality-of-service level.

## See Also

### Thread Scheduling

- [dispatch_qos_class_t](dispatch_qos_class_t.md) — Quality-of-service classes that specify the priorities for executing tasks.
- [dispatch_set_qos_class_floor](dispatch_set_qos_class_floor.md) — Specifies the minimum quality-of-service level for a dispatch queue, source, or workloop.
