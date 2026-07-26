---
title: 'remove(at:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/remove(at:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/remove(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/remove%28at%3A%29.json'
content_hash: 'sha256:91e9cd5bad64e697'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# remove(at:)

<sub>Instance Method</sub>

Removes and returns the element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func remove(at index: Int) -> Element
```

## Return Value

The removed element.

## Discussion

All the elements following the specified position are moved to close the gap.

> [!abstract] Complexity
> O(`self.count`)
