---
title: vertical
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/alignment/vertical
source_url: 'https://developer.apple.com/documentation/swiftui/alignment/vertical'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alignment/vertical.json'
content_hash: 'sha256:5959f127babaa936'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Alignment](../alignment.md)

# vertical

<sub>Instance Property</sub>

The alignment on the vertical axis.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var vertical: VerticalAlignment
```

## Discussion

Set this value when you initialize an alignment using the [init(horizontal:vertical:)](<init(horizontal_vertical_).md>) method. Use one of the built-in [VerticalAlignment](../verticalalignment.md) guides, like [center](../verticalalignment/center.md), or a custom guide that you create.

For information about creating custom guides, see [AlignmentID](../alignmentid.md).

## See Also

### Creating a custom alignment

- [init(horizontal:vertical:)](<init(horizontal_vertical_).md>) — Creates a custom alignment value with the specified horizontal and vertical alignment guides.
- [horizontal](horizontal.md) — The alignment on the horizontal axis.
