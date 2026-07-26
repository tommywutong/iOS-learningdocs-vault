---
title: 'AsyncThrowingStream.Continuation.YieldResult.enqueued(remaining:)'
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncthrowingstream/continuation/yieldresult/enqueued(remaining:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/yieldresult/enqueued(remaining:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/continuation/yieldresult/enqueued%28remaining%3A%29.json'
content_hash: 'sha256:6b3a63b9b0cec827'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [AsyncThrowingStream](../../../asyncthrowingstream.md) · [Continuation](../../continuation.md) · [YieldResult](../yieldresult.md)

# AsyncThrowingStream.Continuation.YieldResult.enqueued(remaining:)

<sub>Case</sub>

The stream successfully enqueued the element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case enqueued(remaining: Int)
```

## Discussion

This value represents the successful enqueueing of an element, whether the stream buffers the element or delivers it immediately to a pending call to `next()`. The associated value `remaining` is a hint that indicates the number of remaining slots in the buffer at the time of the `yield` call.

> [!note] Note
> From a thread safety perspective, `remaining` is a lower bound on the number of remaining slots. This is because a subsequent call that uses the `remaining` value could race on the consumption of values from the stream.

## See Also

### Yield Results

- [AsyncThrowingStream.Continuation.YieldResult.dropped(_:)](<dropped(__).md>) — The stream didn’t enqueue the element because the buffer was full.
- [AsyncThrowingStream.Continuation.YieldResult.terminated](terminated.md) — The stream didn’t enqueue the element because the stream was in a terminal state.
