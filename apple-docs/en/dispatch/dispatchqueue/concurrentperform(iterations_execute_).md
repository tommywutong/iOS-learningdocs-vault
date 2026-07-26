---
title: 'concurrentPerform(iterations:execute:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/concurrentperform(iterations:execute:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/concurrentperform(iterations:execute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/concurrentperform%28iterations%3Aexecute%3A%29.json'
content_hash: 'sha256:b6095ce8e7bfee43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# concurrentPerform(iterations:execute:)

<sub>Type Method</sub>

Submits a single block to the dispatch queue and causes the block to be executed the specified number of times.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency class func concurrentPerform(iterations: Int, execute work: @Sendable (Int) -> Void)
```

## Parameters

- `iterations` — The number of times to execute the block. Higher iteration values give the system the ability to balance more efficiently across multiple cores. To get the maximum benefit of this function, configure the number of iterations to be at least three times the number of available cores.

- `work` — The block to execute in parallel. This block has no return value and takes the following parameter: - **iteration** — The current iteration index.

## Discussion

This method implements an efficient parallel for-loop. The dispatch queue executes the submitted block the specified number of times and waits for all iterations to complete before returning. If the target queue is a concurrent queue, the blocks run in parallel and must therefore be reentrant-safe.
