---
title: 'asyncAndWait(execute:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/asyncandwait(execute:)-1udeu'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/asyncandwait(execute:)-1udeu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/asyncandwait%28execute%3A%29-1udeu.json'
content_hash: 'sha256:167241b9b6f0d3a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# asyncAndWait(execute:)

<sub>Instance Method</sub>

Submits a work item for execution and returns only after it finishes executing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func asyncAndWait(execute block: () -> Void)
```

## Parameters

- `block` — The block that contains the work to perform. This block has no return value and no parameters. This parameter cannot be `NULL`.

## Discussion

This function submits work to the specified queue for execution. Unlike [dispatch_async](../dispatch_async.md), this function does not return until after the block finishes. Calling this function and targeting the current queue results in deadlock.

Unlike [dispatch_sync](<sync(execute_)-3segw.md>), this function respects all attributes of the queue when it executes the block. For example, it respects the quality-of-service level and autorelease frequency of the target queue.

If the runtime has already brought up a thread to service asynchronous work items, the system uses that same thread to execute any synchronous blocks you submitted using this function. If the runtime hasn’t brought up a thread to service asynchronous work items, the sytem executes these synchronous blocks on the current thread as an optimization. However, these optimizations apply only when `queue` targets a global concurrent queue. If it targets any other queue, the system executes the work on that queue’s thread. For example, if `queue` targets the main queue, the block always runs on the main thread.

Unlike with [dispatch_async](../dispatch_async.md), no retain is performed on the target queue. Because calls to this function are synchronous, it “borrows” the reference of the caller. Moreover, no `Block_copy` is performed on the block.

## See Also

### Executing Tasks Synchronously

- [sync(execute:)](<sync(execute_)-2fzvo.md>) — Submits a work item for execution on the current queue and returns after that block finishes executing.
- [dispatch_sync](<sync(execute_)-3segw.md>) — Submits a block object for execution and returns after that block finishes executing.
- [sync(execute:)](<sync(execute_)-20xby.md>) — Submits a work item for execution and returns the results from that item after it finishes executing.
- [sync(flags:execute:)](<sync(flags_execute_).md>) — Submits a work item for execution using the specified attributes and returns the results from that item after it finishes executing.
