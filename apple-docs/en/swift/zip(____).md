---
title: 'zip(_:_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/zip(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/zip(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/zip%28_%3A_%3A%29.json'
content_hash: 'sha256:100cf5ddf9ccca63'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# zip(_:_:)

<sub>Function</sub>

Creates a sequence of pairs built out of two underlying sequences.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func zip<Sequence1, Sequence2>(_ sequence1: Sequence1, _ sequence2: Sequence2) -> Zip2Sequence<Sequence1, Sequence2> where Sequence1 : Sequence, Sequence2 : Sequence
```

## Parameters

- `sequence1` — The first sequence or collection to zip.

- `sequence2` — The second sequence or collection to zip.

## Return Value

A sequence of tuple pairs, where the elements of each pair are corresponding elements of `sequence1` and `sequence2`.

## Discussion

In the `Zip2Sequence` instance returned by this function, the elements of the _i_th pair are the _i_th elements of each underlying sequence. The following example uses the `zip(_:_:)` function to iterate over an array of strings and a countable range at the same time:

```swift
let words = ["one", "two", "three", "four"]
let numbers = 1...4

for (word, number) in zip(words, numbers) {
    print("\(word): \(number)")
}
// Prints "one: 1"
// Prints "two: 2"
// Prints "three: 3"
// Prints "four: 4"
```

If the two sequences passed to `zip(_:_:)` are different lengths, the resulting sequence is the same length as the shorter sequence. In this example, the resulting array is the same length as `words`:

```swift
let naturalNumbers = 1...Int.max
let zipped = Array(zip(words, naturalNumbers))
// zipped == [("one", 1), ("two", 2), ("three", 3), ("four", 4)]
```
