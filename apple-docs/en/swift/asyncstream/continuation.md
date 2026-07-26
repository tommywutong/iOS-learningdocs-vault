---
title: AsyncStream.Continuation
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncstream/continuation
source_url: 'https://developer.apple.com/documentation/swift/asyncstream/continuation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncstream/continuation.json'
content_hash: 'sha256:34904dcaf904bb7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncStream](../asyncstream.md)

# AsyncStream.Continuation

<sub>Structure</sub>

A mechanism to interface between synchronous code and an asynchronous stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Continuation
```

## Overview

The closure you provide to the `AsyncStream` in `init(_:bufferingPolicy:_:)` receives an instance of this type when invoked. Use this continuation to provide elements to the stream by calling one of the `yield` methods, then terminate the stream normally by calling the `finish()` method.

> [!note] Note
> Unlike other continuations in Swift, `AsyncStream.Continuation` supports escaping.

## Relationships

- **Conforms To**: [Equatable](../equatable.md), [Hashable](../hashable.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Producing Elements

- [yield(_:)](<continuation/yield(__).md>) — Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given element.
- [yield(with:)](<continuation/yield(with_).md>) — Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given result’s success value.
- [yield()](<continuation/yield().md>) — Resume the task awaiting the next iteration point by having it return normally from its suspension point.
- [YieldResult](continuation/yieldresult.md) — A type that indicates the result of yielding a value to a client, by way of the continuation.

### Finishing the Stream

- [finish()](<continuation/finish().md>) — Resume the task awaiting the next iteration point by having it return nil, which signifies the end of the iteration.

### Handling Termination

- [onTermination](continuation/ontermination.md) — A callback to invoke when canceling iteration of an asynchronous stream.
- [Termination](continuation/termination.md) — A type that indicates how the stream terminated.

### Enumerations

- [BufferingPolicy](continuation/bufferingpolicy.md) — A strategy that handles exhaustion of a buffer’s capacity.

### Default Implementations

- [Equatable Implementations](continuation/equatable-implementations.md)
- [Hashable Implementations](continuation/hashable-implementations.md)

## See Also

### Creating a Continuation-Based Stream

- [init(_:bufferingPolicy:_:)](<init(__bufferingpolicy___).md>) — Constructs an asynchronous stream for an element type, using the specified buffering policy and element-producing closure.
- [BufferingPolicy](continuation/bufferingpolicy.md) — A strategy that handles exhaustion of a buffer’s capacity.
