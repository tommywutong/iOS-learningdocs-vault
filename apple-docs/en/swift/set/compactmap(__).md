---
title: 'compactMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/compactmap(_:)'
source_url: 'https://developer.apple.com/documentation/swift/set/compactmap(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/compactmap%28_%3A%29.json'
content_hash: 'sha256:e2b09acdfd26e633'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# compactMap(_:)

<sub>Instance Method</sub>

Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compactMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```

## Parameters

- `transform` — A closure that accepts an element of this sequence as its argument and returns an optional value.

## Return Value

An array of the non-`nil` results of calling `transform` with each element of the sequence.

## Discussion

Use this method to receive an array of non-optional values when your transformation produces an optional value.

In this example, note the difference in the result of using `map` and `compactMap` with a transformation that returns an optional `Int` value.

```swift
let possibleNumbers = ["1", "2", "three", "///4///", "5"]

let mapped: [Int?] = possibleNumbers.map { str in Int(str) }
// [1, 2, nil, nil, 5]

let compactMapped: [Int] = possibleNumbers.compactMap { str in Int(str) }
// [1, 2, 5]
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of this sequence.

## See Also

### Transforming a Set

- [flatMap(_:)](<flatmap(__)-i3my.md>) — Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](<flatmap(__)-6chuh.md>)
- [reduce(_:_:)](<reduce(____).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [reduce(into:_:)](<reduce(into___).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [sorted()](<sorted().md>) — Returns the elements of the sequence, sorted.
- [sorted(by:)](<sorted(by_).md>) — Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [shuffled()](<shuffled().md>) — Returns the elements of the sequence, shuffled.
- [shuffled(using:)](<shuffled(using_).md>) — Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [lazy](lazy.md) — A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
