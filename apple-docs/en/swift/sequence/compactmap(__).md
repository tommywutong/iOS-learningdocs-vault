---
title: 'compactMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence/compactmap(_:)'
source_url: 'https://developer.apple.com/documentation/swift/sequence/compactmap(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/compactmap%28_%3A%29.json'
content_hash: 'sha256:cdb1887884ab8703'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

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

### Transforming a Sequence

- [map(_:)](<map(__).md>) — Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [flatMap(_:)](<flatmap(__)-jo2y.md>) — Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [reduce(_:_:)](<reduce(____).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [reduce(into:_:)](<reduce(into___).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [lazy](lazy.md) — A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [flatMap(_:)](<flatmap(__)-383uq.md>)
