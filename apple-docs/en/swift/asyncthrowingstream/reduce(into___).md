---
title: 'reduce(into:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncthrowingstream/reduce(into:_:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/reduce(into:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/reduce%28into%3A_%3A%29.json'
content_hash: 'sha256:764b040361ff28b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingStream](../asyncthrowingstream.md)

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

## See Also

### Transforming a Sequence

- [map(_:)](<map(__)-4a4ke.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [map(_:)](<map(__)-58nrj.md>) — Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [compactMap(_:)](<compactmap(__)-7mgih.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [compactMap(_:)](<compactmap(__)-944nt.md>) — Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [flatMap(_:)](<flatmap(__)-vhin.md>) — Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.
- [reduce(_:_:)](<reduce(____).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure.
