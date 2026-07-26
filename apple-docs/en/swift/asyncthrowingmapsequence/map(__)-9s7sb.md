---
title: 'map(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncthrowingmapsequence/map(_:)-9s7sb'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingmapsequence/map(_:)-9s7sb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingmapsequence/map%28_%3A%29-9s7sb.json'
content_hash: 'sha256:c47fb0a12338b7de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingMapSequence](../asyncthrowingmapsequence.md)

# map(_:)

<sub>Instance Method</sub>

Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func map<Transformed>(_ transform: @escaping @Sendable (Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>
```

## Parameters

- `transform` — A mapping closure. `transform` accepts an element of this sequence as its parameter and returns a transformed value of the same or of a different type.

## Return Value

An asynchronous sequence that contains, in order, the elements produced by the `transform` closure.

## Discussion

Use the `map(_:)` method to transform every element received from a base asynchronous sequence. Typically, you use this to transform from one type of element to another.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `5`. The closure provided to the `map(_:)` method takes each `Int` and looks up a corresponding `String` from a `romanNumeralDict` dictionary. This means the outer `for await in` loop iterates over `String` instances instead of the underlying `Int` values that `Counter` produces:

```swift
let romanNumeralDict: [Int: String] =
    [1: "I", 2: "II", 3: "III", 5: "V"]

let stream = Counter(howHigh: 5)
    .map { romanNumeralDict[$0] ?? "(unknown)" }
for await numeral in stream {
    print(numeral, terminator: " ")
}
// Prints "I II III (unknown) V "
```
