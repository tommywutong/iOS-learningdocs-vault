---
title: 'insert(copying:at:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/insert(copying:at:)-4823q'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/insert(copying:at:)-4823q'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/insert%28copying%3Aat%3A%29-4823q.json'
content_hash: 'sha256:265e5faa463d59cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# insert(copying:at:)

<sub>Instance Method</sub>

Copies the elements of a collection into this array at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func insert(copying newElements: some Collection<Element>, at index: Int)
```

## Parameters

- `newElements` — The new elements to insert into the array.

- `index` — The position at which to insert the new elements. It must be a valid index of the array.

## Discussion

The new elements are inserted before the element currently at the specified index. If you pass the array’s `endIndex` as the `index` parameter, then the new elements are appended to the end of the array.

All existing elements at or following the specified position are moved to make room for the new item.

If the array does not have sufficient capacity to hold enough elements, then this reallocates the array’s storage to extend its capacity, using a geometric growth rate.

> [!abstract] Complexity
> O(`self.count` + `newElements.count`)
