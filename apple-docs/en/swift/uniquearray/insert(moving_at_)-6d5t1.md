---
title: 'insert(moving:at:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/insert(moving:at:)-6d5t1'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/insert(moving:at:)-6d5t1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/insert%28moving%3Aat%3A%29-6d5t1.json'
content_hash: 'sha256:4ca58ea8157c9448'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# insert(moving:at:)

<sub>Instance Method</sub>

Moves the elements of an output span into this array, starting at the specified position, and leaving the span empty.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func insert(moving items: inout OutputSpan<Element>, at index: Int)
```

## Parameters

- `items` — An output span whose contents to move into the array.

- `index` — The position at which to insert the new items. `index` must be a valid index in the array.

## Discussion

All existing elements at or following the specified position are moved to make room for the new items.

If the array does not have sufficient capacity to hold the new elements, then this reallocates storage to extend its capacity, using a geometric growth rate.

> [!abstract] Complexity
> O(`self.count` + `items.count`)
