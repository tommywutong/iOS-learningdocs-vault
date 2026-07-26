---
title: spacing
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/griditem/spacing
source_url: 'https://developer.apple.com/documentation/swiftui/griditem/spacing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/griditem/spacing.json'
content_hash: 'sha256:bb9ef2760dabcb95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GridItem](../griditem.md)

# spacing

<sub>Instance Property</sub>

The spacing to the next item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var spacing: CGFloat?
```

## Discussion

If this value is `nil`, the item uses a reasonable default for the current platform.

## See Also

### Inspecting grid item properties

- [alignment](alignment.md) — The alignment to use when placing each view.
- [size](size-swift.property.md) — The size of the item, which is the width of a column item or the height of a row item.
- [Size](size-swift.enum.md) — The size in the minor axis of one or more rows or columns in a grid layout.
