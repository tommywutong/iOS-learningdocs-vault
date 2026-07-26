---
title: 'sync(execute:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/sync(execute:)-3segw'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/sync(execute:)-3segw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/sync%28execute%3A%29-3segw.json'
content_hash: 'sha256:3b06686c2d607e32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# sync(execute:)

<sub>Instance Method</sub>

Submits a block object for execution and returns after that block finishes executing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sync(execute block: () -> Void)
```

## Parameters

- `block` — The block that contains the work to perform. This block has no return value and no parameters. This parameter cannot be `NULL`.

## Discussion

This function submits a block to the specified dispatch queue for synchronous execution. Unlike [dispatch_async](../dispatch_async.md), this function does not return until the block has finished. Calling this function and targeting the current queue results in deadlock.

Unlike with [dispatch_async](../dispatch_async.md), no retain is performed on the target queue. Because calls to this function are synchronous, it “borrows” the reference of the caller. Moreover, no `Block_copy` is performed on the block.

As a performance optimization, this function executes blocks on the current thread whenever possible, with one exception: Blocks submitted to the main dispatch queue always run on the main thread.

## See Also

### Executing Tasks Synchronously

- [sync(execute:)](<sync(execute_)-2fzvo.md>) — Submits a work item for execution on the current queue and returns after that block finishes executing.
- [sync(execute:)](<sync(execute_)-20xby.md>) — Submits a work item for execution and returns the results from that item after it finishes executing.
- [sync(flags:execute:)](<sync(flags_execute_).md>) — Submits a work item for execution using the specified attributes and returns the results from that item after it finishes executing.
- [dispatch_async_and_wait](<asyncandwait(execute_)-1udeu.md>) — Submits a work item for execution and returns only after it finishes executing.
