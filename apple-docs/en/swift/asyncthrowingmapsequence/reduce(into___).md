---
title: 'reduce(into:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncthrowingmapsequence/reduce(into:_:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingmapsequence/reduce(into:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingmapsequence/reduce%28into%3A_%3A%29.json'
content_hash: 'sha256:f85900bfa5c40cfa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingMapSequence](../asyncthrowingmapsequence.md)

# reduce(into:_:)

<sub>Instance Method</sub>

Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func reduce<Result>(into initialResult: Result, _ updateAccumulatingResult: (inout Result, Self.Element) async throws -> Void) async rethrows -> Result
```

## Parameters

- `initialResult` — The value to use as the initial accumulating value. The `nextPartialResult` closure receives `initialResult` the first time the closure executes.

- `updateAccumulatingResult` — A closure that combines an accumulating value and an element of the asynchronous sequence into a new accumulating value, for use in the next call of the `nextPartialResult` closure or returned to the caller.

## Return Value

The final accumulated value. If the sequence has no elements, the result is `initialResult`.

## Discussion

Use the `reduce(into:_:)` method to produce a single value from the elements of an entire sequence. For example, you can use this method on a sequence of numbers to find their sum or product.

The `updateAccumulatingResult` closure executes sequentially with an accumulating value initialized to `initialResult` and each element of the sequence.

Prefer this method over `reduce(_:_:)` for efficiency when the result is a copy-on-write type, for example an `Array` or `Dictionary`.
