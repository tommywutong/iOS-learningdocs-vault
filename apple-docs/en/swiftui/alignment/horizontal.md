---
title: horizontal
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/alignment/horizontal
source_url: 'https://developer.apple.com/documentation/swiftui/alignment/horizontal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alignment/horizontal.json'
content_hash: 'sha256:e965ae54b7f77f89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Alignment](../alignment.md)

# horizontal

<sub>Instance Property</sub>

The alignment on the horizontal axis.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var horizontal: HorizontalAlignment
```

## Discussion

Set this value when you initialize an alignment using the [init(horizontal:vertical:)](<init(horizontal_vertical_).md>) method. Use one of the built-in [HorizontalAlignment](../horizontalalignment.md) guides, like [center](../horizontalalignment/center.md), or a custom guide that you create.

For information about creating custom guides, see [AlignmentID](../alignmentid.md).

## See Also

### Creating a custom alignment

- [init(horizontal:vertical:)](<init(horizontal_vertical_).md>) — Creates a custom alignment value with the specified horizontal and vertical alignment guides.
- [vertical](vertical.md) — The alignment on the vertical axis.
