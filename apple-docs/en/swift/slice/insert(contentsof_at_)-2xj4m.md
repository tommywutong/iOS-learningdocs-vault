---
title: 'insert(contentsOf:at:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/insert(contentsof:at:)-2xj4m'
source_url: 'https://developer.apple.com/documentation/swift/slice/insert(contentsof:at:)-2xj4m'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/insert%28contentsof%3Aat%3A%29-2xj4m.json'
content_hash: 'sha256:0a2eddf8d0a536f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# insert(contentsOf:at:)

<sub>Instance Method</sub>

Inserts the elements of a sequence into the collection at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func insert<C>(contentsOf newElements: C, at i: Self.Index) where C : Collection, Self.Element == C.Element
```

## Parameters

- `newElements` — The new elements to insert into the collection.

- `i` — The position at which to insert the new elements. `index` must be a valid index of the collection.

## Discussion

The new elements are inserted before the element currently at the specified index. If you pass the collection’s `endIndex` property as the `index` parameter, the new elements are appended to the collection.

Here’s an example of inserting a range of integers into an array of the same type:

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.insert(contentsOf: 100...103, at: 3)
print(numbers)
// Prints "[1, 2, 3, 100, 101, 102, 103, 4, 5]"
```

Calling this method may invalidate any existing indices for use with this collection.

> [!abstract] Complexity
> O(_n_ + _m_), where _n_ is length of this collection and _m_ is the length of `newElements`. If `i == endIndex`, this method is equivalent to `append(contentsOf:)`.
