---
title: 'replaceSubrange(_:moving:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/replacesubrange(_:moving:)-6vpdp'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/replacesubrange(_:moving:)-6vpdp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/replacesubrange%28_%3Amoving%3A%29-6vpdp.json'
content_hash: 'sha256:5c17e5534c7d0104'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# replaceSubrange(_:moving:)

<sub>Instance Method</sub>

Replaces the specified range of elements by moving the contents of an output span into their place. On return, the span is left empty.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replaceSubrange(_ subrange: Range<Int>, moving items: inout OutputSpan<Element>)
```

## Parameters

- `subrange` — The subrange of the array to replace. The bounds of the range must be valid indices in the array.

- `items` — An output span whose contents are to be moved into the array.

## Discussion

This method has the effect of removing the specified range of elements from the array and inserting the new elements starting at the same location. The number of new elements need not match the number of elements being removed.

If the array does not have sufficient capacity to perform the replacement, then this reallocates the array’s storage to extend its capacity, using a geometric growth rate.

If you pass a zero-length range as the `subrange` parameter, this method inserts the elements of `newElements` at `subrange.lowerBound`. Calling the `insert(moving:at:)` method instead is preferred in this case.

Likewise, if you pass a zero-length buffer as the `newElements` parameter, this method removes the elements in the given subrange without replacement. Calling the `removeSubrange(_:)` method instead is preferred in this case.

> [!abstract] Complexity
> O(`self.count` + `items.count`)
