---
title: 'insert(_:at:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/arrayslice/insert(_:at:)'
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/insert(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/insert%28_%3Aat%3A%29.json'
content_hash: 'sha256:aa0492633d34a201'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ArraySlice](../arrayslice.md)

# insert(_:at:)

<sub>Instance Method</sub>

Inserts a new element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func insert(_ newElement: Element, at i: Int)
```

## Parameters

- `newElement` — The new element to insert into the array.

- `i` — The position at which to insert the new element. `index` must be a valid index of the array or equal to its `endIndex` property.

## Discussion

The new element is inserted before the element currently at the specified index. If you pass the array’s `endIndex` property as the `index` parameter, the new element is appended to the array.

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.insert(100, at: 3)
numbers.insert(200, at: numbers.endIndex)

print(numbers)
// Prints "[1, 2, 3, 100, 4, 5, 200]"
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the array. If `i == endIndex`, this method is equivalent to `append(_:)`.
