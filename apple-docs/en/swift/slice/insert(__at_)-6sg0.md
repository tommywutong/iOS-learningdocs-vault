---
title: 'insert(_:at:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/insert(_:at:)-6sg0'
source_url: 'https://developer.apple.com/documentation/swift/slice/insert(_:at:)-6sg0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/insert%28_%3Aat%3A%29-6sg0.json'
content_hash: 'sha256:1253d5030d830547'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# insert(_:at:)

<sub>Instance Method</sub>

Inserts a new element into the collection at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func insert(_ newElement: Base.Element, at i: Slice<Base>.Index)
```

## Parameters

- `newElement` — The new element to insert into the collection.

- `i` — The position at which to insert the new element. `index` must be a valid index into the collection.

## Discussion

The new element is inserted before the element currently at the specified index. If you pass the collection’s `endIndex` property as the `index` parameter, the new element is appended to the collection.

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.insert(100, at: 3)
numbers.insert(200, at: numbers.endIndex)

print(numbers)
// Prints "[1, 2, 3, 100, 4, 5, 200]"
```

Calling this method may invalidate any existing indices for use with this collection.

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection. If `i == endIndex`, this method is equivalent to `append(_:)`.
