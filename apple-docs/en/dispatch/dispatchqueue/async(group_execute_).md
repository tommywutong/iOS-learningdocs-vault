---
title: 'async(group:execute:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/async(group:execute:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/async(group:execute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/async%28group%3Aexecute%3A%29.json'
content_hash: 'sha256:1be2d47ee8775eb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# async(group:execute:)

<sub>Instance Method</sub>

Schedules a work item asynchronously for execution and associates it with the specified dispatch group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func async(group: DispatchGroup, execute workItem: DispatchWorkItem)
```

## Parameters

- `group` — The dispatch group to associate with the work item. This parameter cannot be `NULL`.

- `workItem` — The work item containing the task to execute. For information on how to create this work item, see [DispatchWorkItem](../dispatchworkitem.md).

## Discussion

This method adds the work item to the group before scheduling it on the current queue.

## See Also

### Dispatching Work to Groups

- [async(group:qos:flags:execute:)](<async(group_qos_flags_execute_).md>) — Schedules a block asynchronously for execution and optionally associates it with a dispatch group.
