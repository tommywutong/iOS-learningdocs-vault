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
doc_path: '/documentation/swift/asyncstream/continuation/yield(with:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncstream/continuation/yield(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncstream/continuation/yield%28with%3A%29.json'
content_hash: 'sha256:81d62b7528313538'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncStream](../../asyncstream.md) · [Continuation](../continuation.md)

# yield(with:)

<sub>Instance Method</sub>

Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given result’s success value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func yield(with result: sending Result<Element, Never>) -> AsyncStream<Element>.Continuation.YieldResult
```

## Parameters

- `result` — A result to yield from the continuation.

## Return Value

A `YieldResult` that indicates the success or failure of the yield operation.

## Discussion

If nothing is awaiting the next value, the method attempts to buffer the result’s element.

If you call this method repeatedly, each call returns immediately, without blocking for any awaiting consumption from the iteration.

## See Also

### Producing Elements

- [yield(_:)](<yield(__).md>) — Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given element.
- [yield()](<yield().md>) — Resume the task awaiting the next iteration point by having it return normally from its suspension point.
- [YieldResult](yieldresult.md) — A type that indicates the result of yielding a value to a client, by way of the continuation.
