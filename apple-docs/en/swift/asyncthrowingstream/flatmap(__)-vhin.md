---
title: 'flatMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncthrowingstream/flatmap(_:)-vhin'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/flatmap(_:)-vhin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/flatmap%28_%3A%29-vhin.json'
content_hash: 'sha256:2c7c017e1ea756ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingStream](../asyncthrowingstream.md)

# flatMap(_:)

<sub>Instance Method</sub>

Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func flatMap<SegmentOfResult>(_ transform: @escaping @Sendable (Self.Element) async throws -> SegmentOfResult) -> AsyncThrowingFlatMapSequence<Self, SegmentOfResult> where SegmentOfResult : AsyncSequence
```

## Parameters

- `transform` — An error-throwing mapping closure. `transform` accepts an element of this sequence as its parameter and returns an `AsyncSequence`. If `transform` throws an error, the sequence ends.

## Return Value

A single, flattened asynchronous sequence that contains all elements in all the asynchronous sequences produced by `transform`. The sequence ends either when the last sequence created from the last element from base sequence ends, or when `transform` throws an error.

## Discussion

Use this method to receive a single-level asynchronous sequence when your transformation produces an asynchronous sequence for each element.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `5`. The transforming closure takes the received `Int` and returns a new `Counter` that counts that high. For example, when the transform receives `3` from the base sequence, it creates a new `Counter` that produces the values `1`, `2`, and `3`. The `flatMap(_:)` method “flattens” the resulting sequence-of-sequences into a single `AsyncSequence`. However, when the closure receives `4`, it throws an error, terminating the sequence.

```swift
do {
    let stream = Counter(howHigh: 5)
        .flatMap { (value) -> Counter in
            if value == 4 {
                throw MyError()
            }
            return Counter(howHigh: value)
        }
    for try await number in stream {
        print(number, terminator: " ")
    }
} catch {
    print(error)
}
// Prints "1 1 2 1 2 3 MyError() "
```

## See Also

### Transforming a Sequence

- [map(_:)](<map(__)-4a4ke.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [map(_:)](<map(__)-58nrj.md>) — Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [compactMap(_:)](<compactmap(__)-7mgih.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [compactMap(_:)](<compactmap(__)-944nt.md>) — Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [reduce(_:_:)](<reduce(____).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [reduce(into:_:)](<reduce(into___).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.
