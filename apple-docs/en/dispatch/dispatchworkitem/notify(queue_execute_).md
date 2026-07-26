---
title: 'notify(queue:execute:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchworkitem/notify(queue:execute:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchworkitem/notify(queue:execute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchworkitem/notify%28queue%3Aexecute%3A%29.json'
content_hash: 'sha256:1237e514186ea57f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchWorkItem](../dispatchworkitem.md)

# notify(queue:execute:)

<sub>Instance Method</sub>

Schedules the execution of the specified work item after the completion of the current work item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func notify(queue: DispatchQueue, execute: DispatchWorkItem)
```

## Parameters

- `queue` — The queue on which to execute the work item in the `execute` parameter.

- `execute` — The work item to execute after the completion of the current work item.

## See Also

### Adding a Completion Handler

- [notify(qos:flags:queue:execute:)](<notify(qos_flags_queue_execute_).md>) — Schedules the execution of the specified work item, with the specified quality-of-service, after the completion of the current work item.
