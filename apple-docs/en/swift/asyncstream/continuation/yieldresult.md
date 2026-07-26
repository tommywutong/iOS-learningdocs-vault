---
title: AsyncStream.Continuation.YieldResult
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncstream/continuation/yieldresult
source_url: 'https://developer.apple.com/documentation/swift/asyncstream/continuation/yieldresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncstream/continuation/yieldresult.json'
content_hash: 'sha256:1816722c07b23c29'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncStream](../../asyncstream.md) · [Continuation](../continuation.md)

# AsyncStream.Continuation.YieldResult

<sub>Enumeration</sub>

A type that indicates the result of yielding a value to a client, by way of the continuation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum YieldResult
```

## Overview

The various `yield` methods of `AsyncStream.Continuation` return this type to indicate the success or failure of yielding an element to the continuation.

## Relationships

- **Conforms To**: [Sendable](../../sendable.md), [SendableMetatype](../../sendablemetatype.md)

## Topics

### Yield Results

- [AsyncStream.Continuation.YieldResult.enqueued(remaining:)](<yieldresult/enqueued(remaining_).md>) — The stream successfully enqueued the element.
- [AsyncStream.Continuation.YieldResult.dropped(_:)](<yieldresult/dropped(__).md>) — The stream didn’t enqueue the element because the buffer was full.
- [AsyncStream.Continuation.YieldResult.terminated](yieldresult/terminated.md) — The stream didn’t enqueue the element because the stream was in a terminal state.

## See Also

### Producing Elements

- [yield(_:)](<yield(__).md>) — Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given element.
- [yield(with:)](<yield(with_).md>) — Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given result’s success value.
- [yield()](<yield().md>) — Resume the task awaiting the next iteration point by having it return normally from its suspension point.
