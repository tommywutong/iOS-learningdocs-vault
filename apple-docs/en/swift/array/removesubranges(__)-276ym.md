---
title: 'removeSubranges(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/removesubranges(_:)-276ym'
source_url: 'https://developer.apple.com/documentation/swift/array/removesubranges(_:)-276ym'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/removesubranges%28_%3A%29-276ym.json'
content_hash: 'sha256:2346f71524e9daec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# removeSubranges(_:)

<sub>Instance Method</sub>

Removes the elements at the given indices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeSubranges(_ subranges: RangeSet<Self.Index>)
```

## Parameters

- `subranges` — The indices of the elements to remove.

## Discussion

For example, this code sample finds the indices of all the negative numbers in the array, and then removes those values.

```swift
var numbers = [5, 7, -3, -8, 11, 2, -1, 6]
let negativeIndices = numbers.indices(where: { $0 < 0 })

numbers.removeSubranges(negativeIndices)
// numbers == [5, 7, 11, 2, 6]
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.
