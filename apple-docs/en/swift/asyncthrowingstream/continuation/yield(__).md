---
title: 'yield(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncthrowingstream/continuation/yield(_:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/yield(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/continuation/yield%28_%3A%29.json'
content_hash: 'sha256:25151524e2308165'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncThrowingStream](../../asyncthrowingstream.md) · [Continuation](../continuation.md)

# yield(_:)

<sub>Instance Method</sub>

Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func yield(_ value: sending Element) -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult
```

## Parameters

- `value` — The value to yield from the continuation.

## Return Value

A `YieldResult` that indicates the success or failure of the yield operation.

## Discussion

If nothing is awaiting the next value, the method attempts to buffer the result’s element.

This can be called more than once and returns to the caller immediately without blocking for any awaiting consumption from the iteration.

## See Also

### Producing Elements

- [yield(with:)](<yield(with_).md>) — Resume the task awaiting the next iteration point by having it return normally or throw, based on a given result.
- [yield()](<yield().md>) — Resume the task awaiting the next iteration point by having it return normally from its suspension point.
- [YieldResult](yieldresult.md) — A type that indicates the result of yielding a value to a client, by way of the continuation.
