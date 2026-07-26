---
title: 'GridItem.Size.flexible(minimum:maximum:)'
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/griditem/size-swift.enum/flexible(minimum:maximum:)'
source_url: 'https://developer.apple.com/documentation/swiftui/griditem/size-swift.enum/flexible(minimum:maximum:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/griditem/size-swift.enum/flexible%28minimum%3Amaximum%3A%29.json'
content_hash: 'sha256:4169ecc0ff13418d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GridItem](../../griditem.md) · [Size](../size-swift.enum.md)

# GridItem.Size.flexible(minimum:maximum:)

<sub>Case</sub>

A single flexible item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case flexible(minimum: CGFloat = 10, maximum: CGFloat = .infinity)
```

## Discussion

The size of this item is the size of the grid with spacing and inflexible items removed, divided by the number of flexible items, clamped to the provided bounds.

## See Also

### Getting the sizes

- [GridItem.Size.adaptive(minimum:maximum:)](<adaptive(minimum_maximum_).md>) — Multiple items in the space of a single flexible item.
- [GridItem.Size.fixed(_:)](<fixed(__).md>) — A single item with the specified fixed size.
