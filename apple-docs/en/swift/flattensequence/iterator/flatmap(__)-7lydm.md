---
title: 'flatMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/flattensequence/iterator/flatmap(_:)-7lydm'
source_url: 'https://developer.apple.com/documentation/swift/flattensequence/iterator/flatmap(_:)-7lydm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/flattensequence/iterator/flatmap%28_%3A%29-7lydm.json'
content_hash: 'sha256:62945428d14546b7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [FlattenSequence](../../flattensequence.md) · [Iterator](../iterator.md)

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
