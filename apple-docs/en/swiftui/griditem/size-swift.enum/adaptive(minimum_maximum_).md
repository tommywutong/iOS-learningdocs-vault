---
title: 'GridItem.Size.adaptive(minimum:maximum:)'
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/griditem/size-swift.enum/adaptive(minimum:maximum:)'
source_url: 'https://developer.apple.com/documentation/swiftui/griditem/size-swift.enum/adaptive(minimum:maximum:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/griditem/size-swift.enum/adaptive%28minimum%3Amaximum%3A%29.json'
content_hash: 'sha256:3651501b294d3449'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GridItem](../../griditem.md) · [Size](../size-swift.enum.md)

# GridItem.Size.adaptive(minimum:maximum:)

<sub>Case</sub>

Multiple items in the space of a single flexible item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case adaptive(minimum: CGFloat, maximum: CGFloat = .infinity)
```

## Discussion

This size case places one or more items into the space assigned to a single `flexible` item, using the provided bounds and spacing to decide exactly how many items fit. This approach prefers to insert as many items of the `minimum` size as possible but lets them increase to the `maximum` size.

## See Also

### Getting the sizes

- [GridItem.Size.fixed(_:)](<fixed(__).md>) — A single item with the specified fixed size.
- [GridItem.Size.flexible(minimum:maximum:)](<flexible(minimum_maximum_).md>) — A single flexible item.
