---
title: 'asyncAfter(deadline:qos:flags:execute:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/asyncafter(deadline:qos:flags:execute:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/asyncafter(deadline:qos:flags:execute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/asyncafter%28deadline%3Aqos%3Aflags%3Aexecute%3A%29.json'
content_hash: 'sha256:cbae5b8293b9b84f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# asyncAfter(deadline:qos:flags:execute:)

<sub>Instance Method</sub>

Schedules a block for execution using the specified attributes, and returns immediately.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func asyncAfter(deadline: DispatchTime, qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], execute work: @escaping @Sendable () -> Void)
```

## Parameters

- `deadline` — The time at which to schedule the block for execution. Specifying the current time is less efficient than calling the [async(execute:)](<async(execute_).md>) method directly. Do not specify the value in [distantFuture](../dispatchtime/distantfuture.md); doing so is undefined.

- `qos` — The quality-of-service class to use when executing the block. This parameter determines the priority with which the block is scheduled and executed. For a list of possible values, see [DispatchQoS](../dispatchqos.md).

- `flags` — Additional attributes to apply when executing the block. For a list of possible values, see [DispatchWorkItemFlags](../dispatchworkitemflags.md).

- `work` — The block containing the work to perform. This block has no return value and no parameters.

## See Also

### Executing Tasks Asynchronously

- [async(execute:)](<async(execute_).md>) — Schedules a work item for immediate execution, and returns immediately.
- [asyncAfter(deadline:execute:)](<asyncafter(deadline_execute_).md>) — Schedules a work item for execution at the specified time, and returns immediately.
- [asyncAfter(wallDeadline:execute:)](<asyncafter(walldeadline_execute_).md>) — Schedules a work item for execution after the specified time, and returns immediately.
- [asyncAfter(wallDeadline:qos:flags:execute:)](<asyncafter(walldeadline_qos_flags_execute_).md>) — Schedules a block for execution using the specified attributes, and returns immediately.
