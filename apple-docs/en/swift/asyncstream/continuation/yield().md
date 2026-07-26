---
title: yield()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncstream/continuation/yield()
source_url: 'https://developer.apple.com/documentation/swift/asyncstream/continuation/yield()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncstream/continuation/yield%28%29.json'
content_hash: 'sha256:101bdb749e36d9c7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncStream](../../asyncstream.md) · [Continuation](../continuation.md)

# yield()

<sub>Instance Method</sub>

Resume the task awaiting the next iteration point by having it return normally from its suspension point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func yield() -> AsyncStream<Element>.Continuation.YieldResult where Element == ()
```

## Return Value

A `YieldResult` that indicates the success or failure of the yield operation.

## Discussion

Use this method with `AsyncStream` instances whose `Element` type is `Void`. In this case, the `yield()` call unblocks the awaiting iteration; there is no value to return.

If you call this method repeatedly, each call returns immediately, without blocking for any awaiting consumption from the iteration.

## See Also

### Producing Elements

- [yield(_:)](<yield(__).md>) — Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given element.
- [yield(with:)](<yield(with_).md>) — Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given result’s success value.
- [YieldResult](yieldresult.md) — A type that indicates the result of yielding a value to a client, by way of the continuation.
