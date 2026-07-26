---
title: 'compactMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncsequence/compactmap(_:)-1f8zn'
source_url: 'https://developer.apple.com/documentation/swift/asyncsequence/compactmap(_:)-1f8zn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncsequence/compactmap%28_%3A%29-1f8zn.json'
content_hash: 'sha256:e8a780fcb3efe3c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncSequence](../asyncsequence.md)

# compactMap(_:)

<sub>Instance Method</sub>

Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func compactMap<ElementOfResult>(_ transform: @escaping @Sendable (Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>
```

## Parameters

- `transform` — An error-throwing mapping closure. `transform` accepts an element of this sequence as its parameter and returns a transformed value of the same or of a different type. If `transform` throws an error, the sequence ends.

## Return Value

An asynchronous sequence that contains, in order, the non-`nil` elements produced by the `transform` closure. The sequence ends either when the base sequence ends or when `transform` throws an error.

## Discussion

Use the `compactMap(_:)` method to transform every element received from a base asynchronous sequence, while also discarding any `nil` results from the closure. Typically, you use this to transform from one type of element to another.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `5`. The closure provided to the `compactMap(_:)` method takes each `Int` and looks up a corresponding `String` from a `romanNumeralDict` dictionary. Since there is no key for `4`, the closure returns `nil` in this case, which `compactMap(_:)` omits from the transformed asynchronous sequence. When the value is `5`, the closure throws `MyError`, terminating the sequence.

```swift
let romanNumeralDict: [Int: String] =
    [1: "I", 2: "II", 3: "III", 5: "V"]

do {
    let stream = Counter(howHigh: 5)
        .compactMap { (value) throws -> String? in
            if value == 5 {
                throw MyError()
            }
            return romanNumeralDict[value]
        }
    for try await numeral in stream {
        print(numeral, terminator: " ")
    }
} catch {
    print("Error: \(error)")
}
// Prints "I II III Error: MyError() "
```

## See Also

### Transforming a Sequence

- [map(_:)](<map(__)-1q1k3.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [AsyncMapSequence](../asyncmapsequence.md) — An asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [map(_:)](<map(__)-70wgb.md>) — Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [AsyncThrowingMapSequence](../asyncthrowingmapsequence.md) — An asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [compactMap(_:)](<compactmap(__)-gfdq.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [AsyncCompactMapSequence](../asynccompactmapsequence.md) — An asynchronous sequence that maps a given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [AsyncThrowingCompactMapSequence](../asyncthrowingcompactmapsequence.md) — An asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [AsyncFlatMapSequence](../asyncflatmapsequence.md) — An asynchronous sequence that concatenates the results of calling a given transformation with each element of this sequence.
- [AsyncThrowingFlatMapSequence](../asyncthrowingflatmapsequence.md) — An asynchronous sequence that concatenates the results of calling a given error-throwing transformation with each element of this sequence.
- [reduce(_:_:)](<reduce(____).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [reduce(into:_:)](<reduce(into___).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.
