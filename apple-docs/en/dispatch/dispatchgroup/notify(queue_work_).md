---
title: 'notify(queue:work:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchgroup/notify(queue:work:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchgroup/notify(queue:work:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchgroup/notify%28queue%3Awork%3A%29.json'
content_hash: 'sha256:ba414cc10ae19442'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchGroup](../dispatchgroup.md)

# notify(queue:work:)

<sub>Instance Method</sub>

Schedules the submission of a block to a queue when all tasks in the current group have finished executing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func notify(queue: DispatchQueue, work: DispatchWorkItem)
```

## Parameters

- `queue` — The queue to which the supplied block is submitted when the group completes.

- `work` — The work to be performed on the dispatch queue when the group is completed.

## Discussion

This function schedules a notification block to be submitted to the specified queue when all blocks associated with the dispatch group have completed. If the group is empty (no block objects are associated with the dispatch group), the notification block object is submitted immediately. When the notification block is submitted, the group is empty.

## See Also

### Adding a Completion Handler

- [notify(qos:flags:queue:execute:)](<notify(qos_flags_queue_execute_).md>) — Schedules the submission of a block with the specified attributes to a queue when all tasks in the current group have finished executing.
