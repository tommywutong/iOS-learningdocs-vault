---
title: 'async(group:qos:flags:execute:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/async(group:qos:flags:execute:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/async(group:qos:flags:execute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/async%28group%3Aqos%3Aflags%3Aexecute%3A%29.json'
content_hash: 'sha256:fccbb6ad05930d7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# async(group:qos:flags:execute:)

<sub>Instance Method</sub>

Schedules a block asynchronously for execution and optionally associates it with a dispatch group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func async(group: DispatchGroup? = nil, qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], execute work: @escaping @Sendable () -> Void)
```

## Parameters

- `group` — The dispatch group to associate with the work item. If you specify `NULL`, the block is not associated with a group.

- `qos` — The quality-of-service class to use when executing the block. This parameter determines the priority with which the block is scheduled and executed. For a list of possible values, see [DispatchQoS](../dispatchqos.md).

- `flags` — Additional attributes to apply when executing the block. For a list of possible values, see [DispatchWorkItemFlags](../dispatchworkitemflags.md).

- `work` — The block containing the work to perform. This block has no return value and no parameters.

## See Also

### Dispatching Work to Groups

- [async(group:execute:)](<async(group_execute_).md>) — Schedules a work item asynchronously for execution and associates it with the specified dispatch group.
