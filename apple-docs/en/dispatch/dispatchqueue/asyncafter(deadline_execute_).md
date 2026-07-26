---
title: 'asyncAfter(deadline:execute:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/asyncafter(deadline:execute:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/asyncafter(deadline:execute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/asyncafter%28deadline%3Aexecute%3A%29.json'
content_hash: 'sha256:3bf3deddae898648'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# asyncAfter(deadline:execute:)

<sub>Instance Method</sub>

Schedules a work item for execution at the specified time, and returns immediately.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func asyncAfter(deadline: DispatchTime, execute: DispatchWorkItem)
```

## Parameters

- `deadline` — The time at which to schedule the work item for execution. Specifying the current time is less efficient than calling the [async(execute:)](<async(execute_).md>) method directly. Do not specify the value in [distantFuture](../dispatchtime/distantfuture.md); doing so is undefined.

- `execute` — The work item containing the task to execute. For information on how to create this work item, see [DispatchWorkItem](../dispatchworkitem.md).

## See Also

### Executing Tasks Asynchronously

- [async(execute:)](<async(execute_).md>) — Schedules a work item for immediate execution, and returns immediately.
- [asyncAfter(deadline:qos:flags:execute:)](<asyncafter(deadline_qos_flags_execute_).md>) — Schedules a block for execution using the specified attributes, and returns immediately.
- [asyncAfter(wallDeadline:execute:)](<asyncafter(walldeadline_execute_).md>) — Schedules a work item for execution after the specified time, and returns immediately.
- [asyncAfter(wallDeadline:qos:flags:execute:)](<asyncafter(walldeadline_qos_flags_execute_).md>) — Schedules a block for execution using the specified attributes, and returns immediately.
