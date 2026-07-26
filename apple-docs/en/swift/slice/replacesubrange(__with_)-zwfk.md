---
title: 'replaceSubrange(_:with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/replacesubrange(_:with:)-zwfk'
source_url: 'https://developer.apple.com/documentation/swift/slice/replacesubrange(_:with:)-zwfk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/replacesubrange%28_%3Awith%3A%29-zwfk.json'
content_hash: 'sha256:334f1d3b0ac084d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# replaceSubrange(_:with:)

<sub>Instance Method</sub>

Replaces the specified subrange of elements with the given collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replaceSubrange<C>(_ subRange: Range<Slice<Base>.Index>, with newElements: C) where C : Collection, Base.Element == C.Element
```

## Parameters

- `newElements` — The new elements to add to the collection.

## Discussion

This method has the effect of removing the specified range of elements from the collection and inserting the new elements at the same location. The number of new elements need not match the number of elements being removed.

In this example, three elements in the middle of an array of integers are replaced by the five elements of a `Repeated<Int>` instance.

```swift
 var nums = [10, 20, 30, 40, 50]
 nums.replaceSubrange(1...3, with: repeatElement(1, count: 5))
 print(nums)
 // Prints "[10, 1, 1, 1, 1, 1, 50]"
```

If you pass a zero-length range as the `subrange` parameter, this method inserts the elements of `newElements` at `subrange.startIndex`. Calling the `insert(contentsOf:at:)` method instead is preferred.

Likewise, if you pass a zero-length collection as the `newElements` parameter, this method removes the elements in the given subrange without replacement. Calling the `removeSubrange(_:)` method instead is preferred.

Calling this method may invalidate any existing indices for use with this collection.

> [!abstract] Complexity
> O(_n_ + _m_), where _n_ is length of this collection and _m_ is the length of `newElements`. If the call to this method simply appends the contents of `newElements` to the collection, this method is equivalent to `append(contentsOf:)`.
