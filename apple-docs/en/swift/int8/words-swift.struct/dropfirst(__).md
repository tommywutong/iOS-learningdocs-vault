---
title: 'dropFirst(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int8/words-swift.struct/dropfirst(_:)'
source_url: 'https://developer.apple.com/documentation/swift/int8/words-swift.struct/dropfirst(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int8/words-swift.struct/dropfirst%28_%3A%29.json'
content_hash: 'sha256:5d41275e87a8bb1b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Int8](../../int8.md) · [Words](../words-swift.struct.md)

# dropFirst(_:)

<sub>Instance Method</sub>

Returns a subsequence containing all but the given number of initial elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dropFirst(_ k: Int = 1) -> Self.SubSequence
```

## Parameters

- `k` — The number of elements to drop from the beginning of the collection. `k` must be greater than or equal to zero.

## Return Value

A subsequence starting after the specified number of elements.

## Discussion

If the number of elements to drop exceeds the number of elements in the collection, the result is an empty subsequence.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.dropFirst(2))
// Prints "[3, 4, 5]"
print(numbers.dropFirst(10))
// Prints "[]"
```

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_k_), where _k_ is the number of elements to drop from the beginning of the collection.
