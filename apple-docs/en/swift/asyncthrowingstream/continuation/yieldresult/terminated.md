---
title: AsyncThrowingStream.Continuation.YieldResult.terminated
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingstream/continuation/yieldresult/terminated
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/yieldresult/terminated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/continuation/yieldresult/terminated.json'
content_hash: 'sha256:a64a439fdfdcdb84'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [AsyncThrowingStream](../../../asyncthrowingstream.md) · [Continuation](../../continuation.md) · [YieldResult](../yieldresult.md)

# AsyncThrowingStream.Continuation.YieldResult.terminated

<sub>Case</sub>

The stream didn’t enqueue the element because the stream was in a terminal state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case terminated
```

## Discussion

This indicates the stream terminated prior to calling `yield`, either because the stream finished normally or through cancellation, or it threw an error.

## See Also

### Yield Results

- [AsyncThrowingStream.Continuation.YieldResult.enqueued(remaining:)](<enqueued(remaining_).md>) — The stream successfully enqueued the element.
- [AsyncThrowingStream.Continuation.YieldResult.dropped(_:)](<dropped(__).md>) — The stream didn’t enqueue the element because the buffer was full.
