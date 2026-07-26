---
title: 'swapAt(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/inlinearray/swapat(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/inlinearray/swapat(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/inlinearray/swapat%28_%3A_%3A%29.json'
content_hash: 'sha256:aa496c1bdac8efb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [InlineArray](../inlinearray.md)

# swapAt(_:_:)

<sub>Instance Method</sub>

Exchanges the values at the specified indices of the array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func swapAt(_ i: InlineArray<count, Element>.Index, _ j: InlineArray<count, Element>.Index)
```

## Parameters

- `i` — The index of the first value to swap.

- `j` — The index of the second value to swap.

## Discussion

Both parameters must be valid indices of the array and not equal to `endIndex`. Passing the same index as both `i` and `j` has no effect.

> [!abstract] Complexity
> O(1)
