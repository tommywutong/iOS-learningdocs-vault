---
title: 'sync(flags:execute:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/sync(flags:execute:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/sync(flags:execute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/sync%28flags%3Aexecute%3A%29.json'
content_hash: 'sha256:1e9becd6fd722ce1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# sync(flags:execute:)

<sub>Instance Method</sub>

Submits a work item for execution using the specified attributes and returns the results from that item after it finishes executing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sync<T>(flags: DispatchWorkItemFlags, execute work: () throws -> T) rethrows -> T
```

## Parameters

- `flags` — Additional attributes to apply when executing the block. For a list of possible values, see DispatchWorkItemFlags.

- `work` — The work item containing the work to perform. The block encapsulated by the work item should return a result, which is then returned by this method. For information on how to create this work item, see [DispatchWorkItem](../dispatchworkitem.md).

## Return Value

The return value of the item in the `work` parameter.

## See Also

### Executing Tasks Synchronously

- [sync(execute:)](<sync(execute_)-2fzvo.md>) — Submits a work item for execution on the current queue and returns after that block finishes executing.
- [dispatch_sync](<sync(execute_)-3segw.md>) — Submits a block object for execution and returns after that block finishes executing.
- [sync(execute:)](<sync(execute_)-20xby.md>) — Submits a work item for execution and returns the results from that item after it finishes executing.
- [dispatch_async_and_wait](<asyncandwait(execute_)-1udeu.md>) — Submits a work item for execution and returns only after it finishes executing.
