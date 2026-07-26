---
title: spacing
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/layoutsubview/spacing
source_url: 'https://developer.apple.com/documentation/swiftui/layoutsubview/spacing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layoutsubview/spacing.json'
content_hash: 'sha256:0480828858564ce6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LayoutSubview](../layoutsubview.md)

# spacing

<sub>Instance Property</sub>

The subviews’s preferred spacing values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var spacing: ViewSpacing { get }
```

## Discussion

This [ViewSpacing](../viewspacing.md) instance indicates how much space a subview in a custom layout prefers to have between it and the next view. It contains preferences for all edges, and might take into account the type of both this and the adjacent view. If your [Layout](../layout.md) type places subviews based on spacing preferences, use this instance to compute a distance between this subview and the next. See [placeSubviews(in:proposal:subviews:cache:)](<../layout/placesubviews(in_proposal_subviews_cache_).md>) for an example.

You can also merge this instance with instances from other subviews to construct a new instance that’s suitable for the subviews’ container. See [spacing(subviews:cache:)](<../layout/spacing(subviews_cache_).md>).

## See Also

### Getting subview characteristics

- [dimensions(in:)](<dimensions(in_).md>) — Asks the subview for its dimensions and alignment guides.
- [sizeThatFits(_:)](<sizethatfits(__).md>) — Asks the subview for its size.
- [priority](priority.md) — The layout priority of the subview.
