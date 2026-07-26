---
title: 'append(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/append(_:)'
source_url: 'https://developer.apple.com/documentation/swift/array/append(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/append%28_%3A%29.json'
content_hash: 'sha256:ef2e488224aa4105'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# append(_:)

<sub>Instance Method</sub>

Adds a new element at the end of the array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append(_ newElement: Element)
```

## Parameters

- `newElement` — The element to append to the array.

## Discussion

Use this method to append a single element to the end of a mutable array.

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.append(100)
print(numbers)
// Prints "[1, 2, 3, 4, 5, 100]"
```

Because arrays increase their allocated capacity using an exponential strategy, appending a single element to an array is an O(1) operation when averaged over many calls to the `append(_:)` method. When an array has additional capacity and is not sharing its storage with another instance, appending an element is O(1). When an array needs to reallocate storage before appending or its storage is shared with another copy, appending is O(_n_), where _n_ is the length of the array.

> [!abstract] Complexity
> O(1) on average, over many calls to `append(_:)` on the same array.

## See Also

### Adding Elements

- [insert(_:at:)](<insert(__at_).md>) — Inserts a new element at the specified position.
- [insert(contentsOf:at:)](<insert(contentsof_at_).md>) — Inserts the elements of a sequence into the collection at the specified position.
- [replaceSubrange(_:with:)](<replacesubrange(__with_).md>) — Replaces a range of elements with the elements in the specified collection.
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-7293p.md>) — Replaces the specified subrange of elements with the given collection.
- [reserveCapacity(_:)](<reservecapacity(__).md>) — Reserves enough space to store the specified number of elements.
