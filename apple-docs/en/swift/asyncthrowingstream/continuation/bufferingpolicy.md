---
title: AsyncThrowingStream.Continuation.BufferingPolicy
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingstream/continuation/bufferingpolicy
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/bufferingpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/continuation/bufferingpolicy.json'
content_hash: 'sha256:ae5eeffc0410e49a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncThrowingStream](../../asyncthrowingstream.md) · [Continuation](../continuation.md)

# AsyncThrowingStream.Continuation.BufferingPolicy

<sub>Enumeration</sub>

A strategy that handles exhaustion of a buffer’s capacity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum BufferingPolicy
```

## Relationships

- **Conforms To**: [Sendable](../../sendable.md), [SendableMetatype](../../sendablemetatype.md)

## Topics

### Buffering Policies

- [AsyncThrowingStream.Continuation.BufferingPolicy.unbounded](bufferingpolicy/unbounded.md) — Continue to add to the buffer, without imposing a limit on the number of buffered elements.
- [AsyncThrowingStream.Continuation.BufferingPolicy.bufferingOldest(_:)](<bufferingpolicy/bufferingoldest(__).md>) — When the buffer is full, discard the newly received element.
- [AsyncThrowingStream.Continuation.BufferingPolicy.bufferingNewest(_:)](<bufferingpolicy/bufferingnewest(__).md>) — When the buffer is full, discard the oldest element in the buffer.

## See Also

### Creating a Continuation-Based Stream

- [init(_:bufferingPolicy:_:)](<../init(__bufferingpolicy___).md>) — Constructs an asynchronous stream for an element type, using the specified buffering policy and element-producing closure.
- [Continuation](../continuation.md) — A mechanism to interface between synchronous code and an asynchronous stream.
