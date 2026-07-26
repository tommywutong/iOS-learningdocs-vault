---
title: 'append(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/append(_:)-1re55'
source_url: 'https://developer.apple.com/documentation/swift/array/append(_:)-1re55'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/append%28_%3A%29-1re55.json'
content_hash: 'sha256:67acfb87f0ed1e2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# append(_:)

<sub>Instance Method</sub>

Adds an element to the end of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append(_ newElement: Self.Element)
```

## Parameters

- `newElement` — The element to append to the collection.

## Discussion

If the collection does not have sufficient capacity for another element, additional storage is allocated before appending `newElement`. The following example adds a new number to an array of integers:

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.append(100)

print(numbers)
// Prints "[1, 2, 3, 4, 5, 100]"
```

> [!abstract] Complexity
> O(1) on average, over many calls to `append(_:)` on the same collection.
