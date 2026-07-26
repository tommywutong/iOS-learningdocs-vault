---
title: 'async(execute:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/async(execute:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/async(execute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/async%28execute%3A%29.json'
content_hash: 'sha256:21eb15125ad98e3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# async(execute:)

<sub>Instance Method</sub>

Schedules a work item for immediate execution, and returns immediately.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func async(execute workItem: DispatchWorkItem)
```

## Parameters

- `workItem` — The work item containing the task to execute. For information on how to create this work item, see [DispatchWorkItem](../dispatchworkitem.md).

## See Also

### Executing Tasks Asynchronously

- [asyncAfter(deadline:execute:)](<asyncafter(deadline_execute_).md>) — Schedules a work item for execution at the specified time, and returns immediately.
- [asyncAfter(deadline:qos:flags:execute:)](<asyncafter(deadline_qos_flags_execute_).md>) — Schedules a block for execution using the specified attributes, and returns immediately.
- [asyncAfter(wallDeadline:execute:)](<asyncafter(walldeadline_execute_).md>) — Schedules a work item for execution after the specified time, and returns immediately.
- [asyncAfter(wallDeadline:qos:flags:execute:)](<asyncafter(walldeadline_qos_flags_execute_).md>) — Schedules a block for execution using the specified attributes, and returns immediately.
