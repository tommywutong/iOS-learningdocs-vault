---
title: dispatch_get_global_queue
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_get_global_queue
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_get_global_queue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_get_global_queue.json'
content_hash: 'sha256:dd85ec0b4a4a9495'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_get_global_queue

<sub>Function</sub>

Returns a system-defined global concurrent queue with the specified quality-of-service class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern dispatch_queue_global_tdispatch_get_global_queue(intptr_t identifier, uintptr_t flags);
```

## Parameters

- `identifier` — The quality of service you want to give to tasks executed using this queue. Quality-of-service helps determine the priority given to tasks executed by the queue. You may specify the values `QOS_CLASS_USER_INTERACTIVE`, `QOS_CLASS_USER_INITIATED`, `QOS_CLASS_UTILITY`, or `QOS_CLASS_BACKGROUND`. Queues that handle user-interactive or user-initiated tasks have a higher priority than tasks meant to run in the background. In OS X 10.9 or earlier, you can specify one of the dispatch queue priority values, which are found in [dispatch_queue_priority_t](dispatch_queue_priority_t.md). These values map to an appropriate quality-of-service class.

- `flags` — Flags that are reserved for future use. Always specify `0` for this parameter.

## Return Value

The requested global concurrent queue.

## Discussion

This function returns a queue suitable for executing tasks with the specified quality-of-service level. Calls to the [dispatch_suspend](<dispatchobject/suspend().md>), [dispatch_resume](<dispatchobject/resume().md>), and [dispatch_set_context](dispatch_set_context.md) functions have no effect on the returned queues.

Tasks submitted to the returned queue are scheduled concurrently with respect to one another.

## See Also

### Queues and Tasks

- [dispatch_get_main_queue](dispatch_get_main_queue.md) — Returns the serial dispatch queue associated with the application’s main thread.
- [Dispatch Queue](dispatch-queue.md) — An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [Dispatch Work Item](dispatch-work-item.md) — The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [Dispatch Group](dispatch-group.md) — A group of tasks that you monitor as a single unit.
- [Workloop](workloop.md) — A dispatch object that prioritizes the execution of tasks based on their quality-of-service (QoS) level.
