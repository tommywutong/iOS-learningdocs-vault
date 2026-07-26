---
title: 'swapAt(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/swapat(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/swapat(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/swapat%28_%3A_%3A%29.json'
content_hash: 'sha256:5804d09ac7d2d663'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# swapAt(_:_:)

<sub>Instance Method</sub>

Exchanges the values at the specified indices of the array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func swapAt(_ i: Int, _ j: Int)
```

## Parameters

- `i` — The index of the first value to swap.

- `j` — The index of the second valud to swap.

## Discussion

Both parameters must be valid indices of the array and not equal to endIndex. Passing the same index as both `i` and `j` has no effect.

> [!abstract] Complexity
> O(1)
