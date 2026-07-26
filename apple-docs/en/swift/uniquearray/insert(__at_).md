---
title: 'insert(_:at:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/insert(_:at:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/insert(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/insert%28_%3Aat%3A%29.json'
content_hash: 'sha256:98b2af10974cc365'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# insert(_:at:)

<sub>Instance Method</sub>

Inserts a new element into the array at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func insert(_ item: consuming Element, at index: Int)
```

## Parameters

- `item` — The new element to insert into the array.

## Discussion

If the array does not have sufficient capacity to hold any more elements, then this reallocates storage to extend its capacity, using a geometric growth rate.

The new element is inserted before the element currently at the specified index. If you pass the array’s `endIndex` as the `index` parameter, then the new element is appended to the container.

All existing elements at or following the specified position are moved to make room for the new item.

> [!abstract] Complexity
> O(`self.count`)
