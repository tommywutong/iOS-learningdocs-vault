---
title: 'prefix(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collection/prefix(_:)'
source_url: 'https://developer.apple.com/documentation/swift/collection/prefix(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/prefix%28_%3A%29.json'
content_hash: 'sha256:e759c5039dda6477'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# prefix(_:)

<sub>Instance Method</sub>

Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prefix(_ maxLength: Int) -> Self.SubSequence
```

## Parameters

- `maxLength` — The maximum number of elements to return. `maxLength` must be greater than or equal to zero.

## Return Value

A subsequence starting at the beginning of this collection with at most `maxLength` elements.

## Discussion

If the maximum length exceeds the number of elements in the collection, the result contains all the elements in the collection.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.prefix(2))
// Prints "[1, 2]"
print(numbers.prefix(10))
// Prints "[1, 2, 3, 4, 5]"
```

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_k_), where _k_ is the number of elements to select from the beginning of the collection.
