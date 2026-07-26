---
title: 'sync(execute:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/sync(execute:)-2fzvo'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/sync(execute:)-2fzvo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/sync%28execute%3A%29-2fzvo.json'
content_hash: 'sha256:b548b205f30408b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# sync(execute:)

<sub>Instance Method</sub>

Submits a work item for execution on the current queue and returns after that block finishes executing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sync(execute workItem: DispatchWorkItem)
```

## Parameters

- `workItem` — The dispatch work item containing the task to execute. For information on how to create this work item, see [DispatchWorkItem](../dispatchworkitem.md).

## See Also

### Executing Tasks Synchronously

- [dispatch_sync](<sync(execute_)-3segw.md>) — Submits a block object for execution and returns after that block finishes executing.
- [sync(execute:)](<sync(execute_)-20xby.md>) — Submits a work item for execution and returns the results from that item after it finishes executing.
- [sync(flags:execute:)](<sync(flags_execute_).md>) — Submits a work item for execution using the specified attributes and returns the results from that item after it finishes executing.
- [dispatch_async_and_wait](<asyncandwait(execute_)-1udeu.md>) — Submits a work item for execution and returns only after it finishes executing.
