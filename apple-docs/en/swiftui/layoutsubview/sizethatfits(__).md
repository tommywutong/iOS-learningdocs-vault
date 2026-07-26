---
title: 'sizeThatFits(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/layoutsubview/sizethatfits(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/layoutsubview/sizethatfits(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layoutsubview/sizethatfits%28_%3A%29.json'
content_hash: 'sha256:47c6bd886b1f3b1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LayoutSubview](../layoutsubview.md)

# sizeThatFits(_:)

<sub>Instance Method</sub>

Asks the subview for its size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sizeThatFits(_ proposal: ProposedViewSize) -> CGSize
```

## Parameters

- `proposal` — A proposed size for the subview. In SwiftUI, views choose their own size, but can take a size proposal from their parent view into account when doing so.

## Return Value

The size that the subview chooses for itself, given the proposal from its container view.

## Discussion

Use this method as a convenience to get the [width](../viewdimensions/width.md) and [height](../viewdimensions/height.md) properties of the [ViewDimensions](../viewdimensions.md) instance returned by the [dimensions(in:)](<dimensions(in_).md>) method, reported as a [CGSize](../../corefoundation/cgsize.md) instance.

## See Also

### Getting subview characteristics

- [dimensions(in:)](<dimensions(in_).md>) — Asks the subview for its dimensions and alignment guides.
- [spacing](spacing.md) — The subviews’s preferred spacing values.
- [priority](priority.md) — The layout priority of the subview.
