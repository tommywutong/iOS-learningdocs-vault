---
title: 'removeSubrange(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/removesubrange(_:)-6t21j'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/removesubrange(_:)-6t21j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/removesubrange%28_%3A%29-6t21j.json'
content_hash: 'sha256:c961d493dfcb3b1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# removeSubrange(_:)

<sub>Instance Method</sub>

Removes the specified subrange of elements from the array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeSubrange(_ bounds: Range<Int>)
```

## Parameters

- `bounds` — The subrange of the array to remove. The bounds of the range must be valid indices of the array.

## Discussion

All the elements following the specified subrange are moved to close the resulting gap.

> [!abstract] Complexity
> O(`self.count`)
