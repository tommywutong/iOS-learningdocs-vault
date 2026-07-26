---
title: 'notify(qos:flags:queue:execute:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchgroup/notify(qos:flags:queue:execute:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchgroup/notify(qos:flags:queue:execute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchgroup/notify%28qos%3Aflags%3Aqueue%3Aexecute%3A%29.json'
content_hash: 'sha256:0d519a10b4944c80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchGroup](../dispatchgroup.md)

# notify(qos:flags:queue:execute:)

<sub>Instance Method</sub>

Schedules the submission of a block with the specified attributes to a queue when all tasks in the current group have finished executing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func notify(qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], queue: DispatchQueue, execute work: @escaping () -> Void)
```

## Parameters

- `qos` — The quality of service class for the work to be performed.

- `flags` — Options for how the work is performed. For possible values, see [DispatchWorkItemFlags](../dispatchworkitemflags.md).

- `queue` — The queue to which the supplied block is submitted when the group completes.

- `work` — The work to be performed on the dispatch queue when the group is completed.

## Discussion

This function schedules a notification block to be submitted to the specified queue when all blocks associated with the dispatch group have completed. If the group is empty (no block objects are associated with the dispatch group), the notification block object is submitted immediately. When the notification block is submitted, the group is empty.

## See Also

### Adding a Completion Handler

- [notify(queue:work:)](<notify(queue_work_).md>) — Schedules the submission of a block to a queue when all tasks in the current group have finished executing.
