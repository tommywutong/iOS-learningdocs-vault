---
title: 'yield(with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncthrowingstream/continuation/yield(with:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/yield(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/continuation/yield%28with%3A%29.json'
content_hash: 'sha256:86b4bb26ac80f300'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncThrowingStream](../../asyncthrowingstream.md) · [Continuation](../continuation.md)

# yield(with:)

<sub>Instance Method</sub>

Resume the task awaiting the next iteration point by having it return normally or throw, based on a given result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func yield(with result: sending Result<Element, Failure>) -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult where Failure == any Error
```

## Parameters

- `result` — A result to yield from the continuation. In the `.success(_:)` case, this returns the associated value from the iterator’s `next()` method. If the result is the `failure(_:)` case, this call terminates the stream with the result’s error, by calling `finish(throwing:)`.

## Return Value

A `YieldResult` that indicates the success or failure of the yield operation.

## Discussion

If nothing is awaiting the next value and the result is success, this call attempts to buffer the result’s element.

If you call this method repeatedly, each call returns immediately, without blocking for any awaiting consumption from the iteration.

## See Also

### Producing Elements

- [yield(_:)](<yield(__).md>) — Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given element.
- [yield()](<yield().md>) — Resume the task awaiting the next iteration point by having it return normally from its suspension point.
- [YieldResult](yieldresult.md) — A type that indicates the result of yielding a value to a client, by way of the continuation.
