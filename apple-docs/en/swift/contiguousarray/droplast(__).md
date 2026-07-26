---
title: 'dropLast(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/contiguousarray/droplast(_:)'
source_url: 'https://developer.apple.com/documentation/swift/contiguousarray/droplast(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/contiguousarray/droplast%28_%3A%29.json'
content_hash: 'sha256:691d76a86b66d6ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ContiguousArray](../contiguousarray.md)

# dropLast(_:)

<sub>Instance Method</sub>

Returns a subsequence containing all but the specified number of final elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dropLast(_ k: Int) -> Self.SubSequence
```

## Parameters

- `k` — The number of elements to drop off the end of the collection. `k` must be greater than or equal to zero.

## Return Value

A subsequence that leaves off `k` elements from the end.

## Discussion

If the number of elements to drop exceeds the number of elements in the collection, the result is an empty subsequence.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.dropLast(2))
// Prints "[1, 2, 3]"
print(numbers.dropLast(10))
// Prints "[]"
```

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_k_), where _k_ is the number of elements to drop.
