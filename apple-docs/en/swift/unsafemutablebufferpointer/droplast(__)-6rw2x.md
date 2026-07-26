---
title: 'dropLast(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablebufferpointer/droplast(_:)-6rw2x'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/droplast(_:)-6rw2x'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/droplast%28_%3A%29-6rw2x.json'
content_hash: 'sha256:8d03ba30df589aff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# dropLast(_:)

<sub>Instance Method</sub>

Returns a subsequence containing all but the specified number of final elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dropLast(_ k: Int = 1) -> Self.SubSequence
```

## Parameters

- `k` — The number of elements to drop off the end of the collection. `k` must be greater than or equal to zero.

## Return Value

A subsequence that leaves off the specified number of elements at the end.

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
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_n_), where _n_ is the length of the collection.
