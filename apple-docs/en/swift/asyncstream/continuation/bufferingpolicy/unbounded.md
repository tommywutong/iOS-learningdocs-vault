---
title: AsyncStream.Continuation.BufferingPolicy.unbounded
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncstream/continuation/bufferingpolicy/unbounded
source_url: 'https://developer.apple.com/documentation/swift/asyncstream/continuation/bufferingpolicy/unbounded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncstream/continuation/bufferingpolicy/unbounded.json'
content_hash: 'sha256:c8de40b21ab0dcd5'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [AsyncStream](../../../asyncstream.md) · [Continuation](../../continuation.md) · [BufferingPolicy](../bufferingpolicy.md)

# AsyncStream.Continuation.BufferingPolicy.unbounded

<sub>Case</sub>

Continue to add to the buffer, without imposing a limit on the number of buffered elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case unbounded
```

## See Also

### Buffering Policies

- [AsyncStream.Continuation.BufferingPolicy.bufferingOldest(_:)](<bufferingoldest(__).md>) — When the buffer is full, discard the newly received element.
- [AsyncStream.Continuation.BufferingPolicy.bufferingNewest(_:)](<bufferingnewest(__).md>) — When the buffer is full, discard the oldest element in the buffer.
