---
title: 'AsyncThrowingStream.Continuation.BufferingPolicy.bufferingNewest(_:)'
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncthrowingstream/continuation/bufferingpolicy/bufferingnewest(_:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/bufferingpolicy/bufferingnewest(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/continuation/bufferingpolicy/bufferingnewest%28_%3A%29.json'
content_hash: 'sha256:062382b8d429cd4e'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [AsyncThrowingStream](../../../asyncthrowingstream.md) · [Continuation](../../continuation.md) · [BufferingPolicy](../bufferingpolicy.md)

# AsyncThrowingStream.Continuation.BufferingPolicy.bufferingNewest(_:)

<sub>Case</sub>

When the buffer is full, discard the oldest element in the buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case bufferingNewest(Int)
```

## Discussion

This strategy enforces keeping at most the specified number of newest values.

> [!note] Note
> If the specified number is zero or negative, no elements are buffered. In that case, an iterator receives an element only if it is already awaiting a value when the continuation yields.

## See Also

### Buffering Policies

- [AsyncThrowingStream.Continuation.BufferingPolicy.unbounded](unbounded.md) — Continue to add to the buffer, without imposing a limit on the number of buffered elements.
- [AsyncThrowingStream.Continuation.BufferingPolicy.bufferingOldest(_:)](<bufferingoldest(__).md>) — When the buffer is full, discard the newly received element.
