---
title: 'replaceSubrange(_:copying:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/replacesubrange(_:copying:)-7599g'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/replacesubrange(_:copying:)-7599g'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/replacesubrange%28_%3Acopying%3A%29-7599g.json'
content_hash: 'sha256:3e8a57683cadf0c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# replaceSubrange(_:copying:)

<sub>Instance Method</sub>

Replaces the specified subrange of elements by copying the elements of the given collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replaceSubrange(_ subrange: Range<Int>, copying newElements: consuming some Collection<Element>)
```

## Parameters

- `subrange` — The subrange of the array to replace. The bounds of the range must be valid indices in the array.

- `newElements` — The new elements to copy into the collection.

## Discussion

This method has the effect of removing the specified range of elements from the array and inserting the new elements starting at the same location. The number of new elements need not match the number of elements being removed.

If the capacity of the array isn’t sufficient to perform the replacement, then this reallocates the array’s storage to extend its capacity, using a geometric growth rate.

If you pass a zero-length range as the `subrange` parameter, this method inserts the elements of `newElements` at `subrange.lowerBound`. Calling the `insert(copying:at:)` method instead is preferred in this case.

Likewise, if you pass a zero-length collection as the `newElements` parameter, this method removes the elements in the given subrange without replacement. Calling the `removeSubrange(_:)` method instead is preferred in this case.

> [!abstract] Complexity
> O(_n_ + _m_), where _n_ is count of this array and _m_ is the count of `newElements`.
