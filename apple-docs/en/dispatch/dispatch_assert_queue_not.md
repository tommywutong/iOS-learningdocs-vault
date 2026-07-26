---
title: dispatch_assert_queue_not
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_assert_queue_not
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_assert_queue_not'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_assert_queue_not.json'
content_hash: 'sha256:7da9a367c9a1beb6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_assert_queue_not

<sub>Function</sub>

Generates an assertion if the current block is executing on the specified dispatch queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_assert_queue_not(dispatch_queue_t queue);
```

## Parameters

- `queue` — The dispatch queue where the block must not be running. This parameter must not be NULL.

## Discussion

Use this function to verify that a block is not running on a specific dispatch queue. For example, you might pass the main queue in the queue parameter to verify that the block is not running on the app’s main thread. If you submitted the current block synchronously, the function recurisvely checks the context of the submitting block to ensure that it is also not running on the expected dispatch queue. If the block is running on the specified queue, this function asserts, logs an explanation to the system log, and terminates the app.

This function evaluates where the block is actually executing. For example, if you submit the block to a dispatch queue that targets a different queue, the block is considered to be running on the target queue.

Calling this function outside of a block running on a dispatch queue is a programmer error. If you do so, the function asserts and terminates your app.

## See Also

### Testing the Execution Context

- [dispatch_assert_queue](dispatch_assert_queue.md) — Generates an assertion if the current block is not running on the specified dispatch queue.
- [dispatch_assert_queue_barrier](dispatch_assert_queue_barrier.md) — Generates an assertion if the current block is not running as a barrier on the specified dispatch queue.
