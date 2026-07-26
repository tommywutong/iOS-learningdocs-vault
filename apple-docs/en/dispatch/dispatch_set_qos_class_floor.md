---
title: dispatch_set_qos_class_floor
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_set_qos_class_floor
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_set_qos_class_floor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_set_qos_class_floor.json'
content_hash: 'sha256:fd852d779d7ac9b6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_set_qos_class_floor

<sub>Function</sub>

Specifies the minimum quality-of-service level for a dispatch queue, source, or workloop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_set_qos_class_floor(dispatch_object_t object, dispatch_qos_class_t qos_class, int relative_priority);
```

## Parameters

- `object` — The [dispatch_queue_t](dispatch_queue_t.md), [dispatch_source_t](dispatch_source_t.md), or [dispatch_workloop_t](dispatch_workloop_t.md) object you want to modify. This object must be currently inactive. If you specify an object other than a dispatch queue, source, or workloop, this function terminates the current process.

- `qos_class` — The minimum quality-of-service (QoS) level to assign to the object.

- `relative_priority` — The relative priority within the QoS level. This value is a negative offset from the scheduler priority associated with the value in qos_class. This value must not be greater than `0`.

## Discussion

Use this function to enforce a minimum QoS level on all tasks you assign to the object. If the QoS level of a work item is below the specified minimum, the queue, source, or workloop elevates the priority of that work item to the minimum value. Elevation of the priority happens even if the work item doesn’t have “enforce” semantics in place.

## See Also

### Thread Scheduling

- [dispatch_qos_class_t](dispatch_qos_class_t.md) — Quality-of-service classes that specify the priorities for executing tasks.
- [dispatch_queue_priority_t](dispatch_queue_priority_t.md) — The execution priority for tasks in a global concurrent queue.
