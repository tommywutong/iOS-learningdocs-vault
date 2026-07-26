---
title: 'flatMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/flatmap(_:)-i3m9'
source_url: 'https://developer.apple.com/documentation/swift/string/flatmap(_:)-i3m9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/flatmap%28_%3A%29-i3m9.json'
content_hash: 'sha256:4e9fd9d853656741'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# flatMap(_:)

<sub>Instance Method</sub>

Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<SegmentOfResult>(_ transform: (Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element] where SegmentOfResult : Sequence
```

## Parameters

- `transform` — A closure that accepts an element of this sequence as its argument and returns a sequence or collection.

## Return Value

The resulting flattened array.

## Discussion

Use this method to receive a single-level collection when your transformation produces a sequence or collection for each element.

In this example, note the difference in the result of using `map` and `flatMap` with a transformation that returns an array.

```swift
let numbers = [1, 2, 3, 4]

let mapped = numbers.map { Array(repeating: $0, count: $0) }
// [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4]]

let flatMapped = numbers.flatMap { Array(repeating: $0, count: $0) }
// [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
```

In fact, `s.flatMap(transform)`  is equivalent to `Array(s.map(transform).joined())`.

> [!abstract] Complexity
> O(_m_ + _n_), where _n_ is the length of this sequence and _m_ is the length of the result.

## See Also

### Transforming a String’s Characters

- [compactMap(_:)](<compactmap(__).md>) — Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](<flatmap(__)-6chuq.md>)
- [reduce(_:_:)](<reduce(____).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [reduce(into:_:)](<reduce(into___).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [lazy](lazy.md) — A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
